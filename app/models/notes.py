from app.models import db
from datetime import datetime

class Note(db.Model):
    __tablename__ = 'notes'
    note_id = db.Column(
        db.Integer, 
        primary_key=True
        )
    note = db.Column(
        db.String(1000)
        )
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id')
        )
    date_time = db.Column(
        db.DateTime,
        default = datetime.now()
    )

    user = db.relationship('User')

    def __init__(self, note, user_id,):
        self.note = note
        self.user_id = user_id
        

    def json(self):
        return {'user_id': self.user_id, 'notes': self.note, 'note_id': self.note_id}
