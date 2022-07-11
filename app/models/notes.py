from app.models import db


class NoteModel(db.Model):
    __tablename__ = 'notes'
    note_id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, note, user_id,):
        self.note = note
        self.user_id = user_id
        

    def json(self):
        return {'user_id': self.user_id, 'notes': self.note, 'note_id': self.note_id}
    
    @classmethod
    def find_note_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_note_by_note_id(cls, note_id):
        return cls.query.filter_by(note_id=note_id).first()

    def save_note_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_note_from_db(self):
        db.session.delete(self)
        db.session.commit()
