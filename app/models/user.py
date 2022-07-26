from app import db
import jwt
import datetime
from app import app


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(
        db.Integer, 
        primary_key=True
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

    notes = db.relationship('Note', lazy='dynamic', backref="user")
    

    def encode_jwt(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload = payload,
                key = app.config.get('SECRET_KEY'),
                algorithm="HS256"
            )
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            decode_data = jwt.decode(jwt=auth_token, \
                                    key=app.config.get('SECRET_KEY'), algorithms="HS256")
            return decode_data['sub']
        except Exception as e:
            message = f"Token is invalid --> {e}"
            return False


    def json(self):
        return {'ID': self.id, 'username': self.username, 'password': self.password}
