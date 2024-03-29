from flask import abort, request, jsonify
from app.models.user import User
from app.models.notes import Note
from app.models.category import Category
from app.views import bp
from app import db
from sqlalchemy import desc, and_
from app.views.auth import auth_required
import datetime
from flask_cors import cross_origin

@bp.route('/note', methods = ['POST', 'GET', 'DELETE', 'PUT'])
@cross_origin(origins="*")
@auth_required
def note():
    if request.method == 'GET':
        user_id = request.args.get('user_id', type=str)
        if not user_id:
            abort(400, "missing user_id")
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        notes = db.session.query(Note).order_by(desc(Note.date_time)).filter(
            Note.user_id == user_id
        )

        return jsonify([note.json() for note in notes]), 200
    
    if request.method == 'POST':
        if not request.json:
            abort(400, "request should be body json")
        data = request.json
        def _validate(request) -> bool:
            if 'user_id' not in request:
                return False
            if 'note_content' not in request:
                return False
            if 'category_id' not in request:
                return False
            return True
        if not _validate(data):
            abort(400, "one or more field is missing")
        user_id = data['user_id']
        note_content = data['note_content']
        category_id = data['category_id']

        if not note_content or len(note_content) < 1:
            abort(400, "note can't be empty")
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        if category_id:
            category = Category.query.filter(and_(
                Category.id == category_id,
                Category.user_id == user_id
            )).first()
            if not category:
                abort(404, "category not found")
            
        note = Note(
            user_id = user_id,
            note = note_content,
            category_id = category_id,
            date_time = datetime.datetime.utcnow()
        )
        db.session.add(note)
        db.session.commit()
        return jsonify(note.json()), 201

    if request.method == "DELETE":
        if not request.json:
            abort(400, "request should be body JSON")
        data = request.json
        def _validate(request) -> bool:
            if "user_id" not in request:
                return False
            if "note_id" not in request:
                return False
            return True
        if not _validate(data):
            abort(400, "one or more data field is missing")
        user_id = data['user_id']
        note_id = data['note_id']
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        note = Note.query.filter_by(note_id = note_id).first()
        if not note:
            abort(404, "note not found")
        if note.user_id != user_id:
            abort(401, "user can't delete others notes")
        db.session.delete(note)
        db.session.commit()
        return jsonify("deleted"), 200

    if request.method == "PUT":
        if not request.json:
            abort(400, "request should be body JSON")
        data = request.json
        def _validate(request) -> bool:
            if "user_id" not in request:
                return False
            if "note_id" not in request:
                return False
            if "note_content" not in request:
                return False
            return True
        if not _validate(data):
            abort(400, "one or more field is missing")
        user_id = data['user_id']
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        note_id = data['note_id']
        note = Note.query.filter_by(note_id = note_id).first()
        if not note:
            abort(404, "note not found")
        note_content = data['note_content']
        note.note = note_content
        note.date_time = datetime.datetime.utcnow()
        db.session.commit()
        return jsonify("note updated successfully"), 200