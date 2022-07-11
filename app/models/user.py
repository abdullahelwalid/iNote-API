import hashlib
from app.models import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(
        db.Integer, 
        primary_key=True
        )

    username = db.Column(
        db.String(64), 
        unique=True
        )

    password = db.Column(
        db.String(64)
        )

    email = db.Column(
        db.String(256)
    )

    notes = db.relationship('Note', lazy='dynamic', )


    def __init__(self, username, password, email):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.email = email
        
        

    def json(self):
        return {'ID': self.id, 'username': self.username, 'password': self.password}

    def save_data_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_user_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_user_by_name(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.find_by(id=_id)
        

