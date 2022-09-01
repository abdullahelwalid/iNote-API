from app import db
from datetime import datetime

class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(
        db.Integer, 
        primary_key=True
        )
    note = db.Column(
        db.String(1000)
        )
    user_id = db.Column(
        db.String(64), 
        db.ForeignKey('user.username')
        )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id")
    )
    date_time = db.Column(
        db.DateTime,
        default = datetime.now()
    )
        
    category = db.relationship("Category", backref = "note")
    def json(self):
        return {
            'user_id': self.user_id, 
            'note': self.note, 
            'note_id': self.note_id, 
            "datetime": self.date_time,
            'category': self.category.json()
            }
