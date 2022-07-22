from datetime import datetime
from unicodedata import category
from app.models import db


class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(
        db.Integer,
        primary_key = True
    )

    category = db.Column(
        db.String(126)
    )

    user_id = db.Column(
        db.String(64),
        db.ForeignKey('user.username')
    )
    date_time = db.Column(
        db.DateTime,
        default = datetime.utcnow()
    )

    user = db.relationship("User", backref = "category")

    def json(self):
        return {
            "id": self.id,
            "category": self.category,
            "user_id": self.user_id,
            "datetime": self.date_time
        }