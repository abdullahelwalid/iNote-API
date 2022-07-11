from app.models import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(
        db.Integer, 
        primary_key = True
        )

    username = db.Column(
        db.String(64), 
        unique=True,
        nullable = False
        )
    firstname = db.Column(
        db.String(64)
    )
    lastname = db.Column(
        db.String(64)
    )
    password = db.Column(
        db.String(64)
        )

    email = db.Column(
        db.String(256)
    )

    notes = db.relationship('Note', lazy='dynamic')
        
    def json(self):
        return {'ID': self.id, 'username': self.username, 'password': self.password}
