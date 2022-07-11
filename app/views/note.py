from flask import abort, request, jsonify
from app.models.user import User
from app.models.notes import Note
from app.views import bp
from app.models import db
from sqlalchemy import desc


@bp.route('/note', methods = ['POST', 'GET', 'DELETE', 'PUT'])
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

        return {
            "notes": [note.json() for note in notes]
        }, 200