from app.models.note import Note
from app import db

class NoteController:
    @staticmethod
    def get_all_notes():
        return Note.query.all()

    @staticmethod
    def create_note(data):
        note = Note(title=data['title'], content=data['content'])
        db.session.add(note)
        db.session.commit()
        return note

    @staticmethod
    def get_note_by_id(note_id):
        return Note.query.get_or_404(note_id)

    @staticmethod
    def update_note(note_id, data):
        note = Note.query.get_or_404(note_id)
        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)
        db.session.commit()
        return note

    @staticmethod
    def delete_note(note_id):
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        return note