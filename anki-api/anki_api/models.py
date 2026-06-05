"""Request/response models."""
from pydantic import BaseModel


class NoteCreate(BaseModel):
    deck_name: str
    model_name: str
    fields: dict[str, str]
    identity_key: str
    tags: list[str] = []


class NotesBatchCreate(BaseModel):
    notes: list[NoteCreate]


class FieldsUpdate(BaseModel):
    note_id: int
    fields: dict[str, str]


class NotesDelete(BaseModel):
    note_ids: list[int]


class DeckCreate(BaseModel):
    name: str


class MediaStore(BaseModel):
    filename: str
    data_b64: str | None = None
    path: str | None = None


class DeckBuildImport(BaseModel):
    deck_name: str
    deck_id: int
    note_model_id: int
    note_model_name: str
    note_model_fields: list[str]
    note_model_templates: list[dict[str, str]]
    css: str = ""
    notes: list[dict]  # Each: {identity_key: str, fields: [str,...], tags: [str,...]}
    media_files: list[str] = []
