"""Genanki Note subclass with stable GUIDs for idempotent imports."""
import genanki


class StableNote(genanki.Note):
    """Note whose GUID is derived from a stable identity key, not field content."""

    def __init__(self, *args, identity_key: str, **kwargs):
        super().__init__(*args, **kwargs)
        self._identity_key = identity_key

    @property
    def guid(self):
        return genanki.guid_for(self._identity_key)
