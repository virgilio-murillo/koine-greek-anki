"""Tests for anki-api. Unit tests mock AnkiConnect; integration tests require Anki running."""
import base64
import json
import tempfile
from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient

from anki_api.main import app, client
from anki_api.stable_note import StableNote
from anki_api.deck_builder import build_and_import
import genanki


@pytest.fixture
def tc():
    return TestClient(app)


@pytest.fixture
def mock_anki():
    """Mock the AnkiClient.call method."""
    with patch.object(client, "call") as m:
        yield m


# ── Health ──
class TestHealth:
    def test_health_ok(self, tc, mock_anki):
        mock_anki.return_value = 6
        r = tc.get("/health")
        assert r.status_code == 200
        assert r.json() == {"status": "ok", "ankiconnect_version": 6}

    def test_health_anki_down(self, tc, mock_anki):
        from anki_api.anki_client import AnkiConnectError
        mock_anki.side_effect = AnkiConnectError("unreachable")
        r = tc.get("/health")
        assert r.status_code == 502


# ── Decks ──
class TestDecks:
    def test_list_decks(self, tc, mock_anki):
        mock_anki.return_value = ["Default", "DVA-C02", "Koine"]
        r = tc.get("/decks")
        assert r.status_code == 200
        assert "DVA-C02" in r.json()

    def test_create_deck(self, tc, mock_anki):
        mock_anki.return_value = 1234567890
        r = tc.post("/decks", json={"name": "Test Deck"})
        assert r.status_code == 201
        assert r.json() == {"deck_id": 1234567890, "name": "Test Deck"}
        mock_anki.assert_called_with("createDeck", deck="Test Deck")

    def test_delete_deck(self, tc, mock_anki):
        mock_anki.return_value = None
        r = tc.delete("/decks/Test Deck")
        assert r.status_code == 200
        mock_anki.assert_called_with("deleteDecks", decks=["Test Deck"], cardsToo=True)


# ── Notes ──
class TestNotes:
    def test_find_notes_empty(self, tc, mock_anki):
        mock_anki.return_value = []
        r = tc.get("/notes", params={"q": "deck:Nonexistent"})
        assert r.json() == []

    def test_find_notes_with_results(self, tc, mock_anki):
        mock_anki.side_effect = [
            [111, 222],  # findNotes
            [{"noteId": 111, "fields": {}}, {"noteId": 222, "fields": {}}],  # notesInfo
        ]
        r = tc.get("/notes", params={"q": "deck:DVA"})
        assert r.status_code == 200
        assert len(r.json()) == 2

    def test_add_notes(self, tc, mock_anki):
        mock_anki.return_value = [111, 222]
        r = tc.post("/notes", json={
            "notes": [
                {"deck_name": "Test", "model_name": "Basic", "fields": {"Front": "Q1", "Back": "A1"}, "identity_key": "test:1"},
                {"deck_name": "Test", "model_name": "Basic", "fields": {"Front": "Q2", "Back": "A2"}, "identity_key": "test:2"},
            ]
        })
        assert r.status_code == 201
        assert r.json()["note_ids"] == [111, 222]

    def test_update_fields(self, tc, mock_anki):
        mock_anki.return_value = None
        r = tc.put("/notes/fields", json={"note_id": 111, "fields": {"Back": "Updated"}})
        assert r.status_code == 200
        assert r.json() == {"updated": 111}

    def test_delete_notes(self, tc, mock_anki):
        mock_anki.return_value = None
        r = tc.request("DELETE", "/notes", json={"note_ids": [111, 222]})
        assert r.status_code == 200
        assert r.json() == {"deleted": 2}


# ── Build & Import ──
class TestBuildAndImport:
    def test_build_and_import(self, tc, mock_anki):
        mock_anki.return_value = None  # importPackage returns null
        r = tc.post("/deck/build-and-import", json={
            "deck_name": "Test Build",
            "deck_id": 9999999,
            "note_model_id": 8888888,
            "note_model_name": "TestModel",
            "note_model_fields": ["Front", "Back"],
            "note_model_templates": [{"name": "Card 1", "qfmt": "{{Front}}", "afmt": "{{Back}}"}],
            "css": ".card { font-size: 14px; }",
            "notes": [
                {"identity_key": "test:build:1", "fields": ["Question 1", "Answer 1"], "tags": ["test"]},
                {"identity_key": "test:build:2", "fields": ["Question 2", "Answer 2"], "tags": []},
            ],
            "media_files": [],
        })
        assert r.status_code == 200
        assert r.json() == {"imported": 2, "deck": "Test Build"}
        mock_anki.assert_called_once()
        # Verify it called importPackage with an .apkg path
        call_args = mock_anki.call_args
        assert call_args[0][0] == "importPackage"
        assert call_args[1]["path"].endswith(".apkg")

    def test_import_existing_apkg(self, tc, mock_anki):
        mock_anki.return_value = None
        # Create a temp .apkg
        deck = genanki.Deck(1111, "Temp")
        model = genanki.Model(2222, "M", fields=[{"name": "F"}], templates=[{"name": "C", "qfmt": "{{F}}", "afmt": "{{F}}"}])
        deck.add_note(genanki.Note(model=model, fields=["hi"]))
        with tempfile.NamedTemporaryFile(suffix=".apkg", delete=False) as f:
            genanki.Package(deck).write_to_file(f.name)
            path = f.name
        r = tc.post("/deck/import", params={"path": path})
        assert r.status_code == 200
        assert "imported" in r.json()

    def test_import_nonexistent_file(self, tc, mock_anki):
        r = tc.post("/deck/import", params={"path": "/tmp/nonexistent.apkg"})
        assert r.status_code == 404


# ── Media ──
class TestMedia:
    def test_store_media_b64(self, tc, mock_anki):
        mock_anki.return_value = "test.mp3"
        data = base64.b64encode(b"fake audio data").decode()
        r = tc.post("/media", json={"filename": "test.mp3", "data_b64": data})
        assert r.status_code == 201
        assert r.json() == {"stored": "test.mp3"}

    def test_store_media_path(self, tc, mock_anki):
        mock_anki.return_value = "test.mp3"
        r = tc.post("/media", json={"filename": "test.mp3", "path": "/tmp/test.mp3"})
        assert r.status_code == 201

    def test_store_media_no_source(self, tc, mock_anki):
        r = tc.post("/media", json={"filename": "test.mp3"})
        assert r.status_code == 400


# ── Sync ──
class TestSync:
    def test_sync(self, tc, mock_anki):
        mock_anki.return_value = None
        r = tc.post("/sync")
        assert r.status_code == 200
        assert r.json() == {"status": "synced"}


# ── StableNote unit test ──
class TestStableNote:
    def test_guid_stability(self):
        model = genanki.Model(1234, "M", fields=[{"name": "F"}], templates=[{"name": "C", "qfmt": "{{F}}", "afmt": "{{F}}"}])
        n1 = StableNote(model=model, fields=["content v1"], identity_key="mykey:1")
        n2 = StableNote(model=model, fields=["content v2 CHANGED"], identity_key="mykey:1")
        # Same identity_key → same GUID even with different content
        assert n1.guid == n2.guid

    def test_different_keys_different_guids(self):
        model = genanki.Model(1234, "M", fields=[{"name": "F"}], templates=[{"name": "C", "qfmt": "{{F}}", "afmt": "{{F}}"}])
        n1 = StableNote(model=model, fields=["same"], identity_key="key:1")
        n2 = StableNote(model=model, fields=["same"], identity_key="key:2")
        assert n1.guid != n2.guid
