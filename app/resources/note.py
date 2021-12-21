from flask_restful import Resource, reqparse
from app.models.notes import NoteModel

class Note(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'note',
        type=str,
        required=True,
        help="Please insert your note"
    )
    parser.add_argument(
        'user_id',
        type=int,
        required=True,
        help="Enter user ID"
    )
    
    
    def post(self):
        data = Note.parser.parse_args()
        note = NoteModel(**data)
        note.save_note_to_db()
        return {'message': 'note added successfuly'}, 201

    




class NoteGet(Resource):
    def get(self, user_id):
        note = NoteModel.find_note_by_user_id(user_id)
        if note:
            return {"notes": [notes.json() for notes in note]}
        return {'message': 'You have no notes in records please add a note.'}, 404
    

class DeleteNot(Resource):
    def delete(self, note_id):
        note = NoteModel.find_note_by_note_id(note_id)
        if note:
            note.delete_note_from_db()
            return {'message': 'Note deleted successfuly'}