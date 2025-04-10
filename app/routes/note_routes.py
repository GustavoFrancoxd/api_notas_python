from flask import Blueprint, request, jsonify, render_template
from app.controllers.note_controller import NoteController
from app.models.note import Note

# Crear un Blueprint para las rutas de notas
notes_bp = Blueprint('notes', __name__)


# Obtener todas las notas (GET)
@notes_bp.route('/', methods=['GET'])
def get_all_notes():
    notes = NoteController.get_all_notes()
    return jsonify([note.to_dict() for note in notes]), 200


# Crear una nueva nota (POST)
@notes_bp.route('/', methods=['POST'])
def create_note():
    data = request.get_json()

    # Validación simple
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Faltan campos 'title' o 'content'"}), 400

    try:
        new_note = NoteController.create_note(data)
        return jsonify(new_note.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtener una nota por ID (GET)
@notes_bp.route('/<int:note_id>', methods=['GET'])
def get_note(note_id):
    try:
        note = NoteController.get_note_by_id(note_id)
        return jsonify(note.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Nota no encontrada"}), 404


# Actualizar una nota (PUT/PATCH)
@notes_bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    try:
        updated_note = NoteController.update_note(note_id, data)
        return jsonify(updated_note.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Eliminar una nota (DELETE)
@notes_bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        deleted_note = NoteController.delete_note(note_id)
        return jsonify({"message": "Nota eliminada", "note": deleted_note.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Nota no encontrada"}), 404


# Nueva ruta para servir el template
@notes_bp.route('/template')
def show_template():
    return render_template('index.html')  # Buscará en app/templates/