from flask import Flask
from flask_restful import Api, Resource
from resources.user import UserList, UserRegister
from db import db
from resources.note import DeleteNot, Note, NoteGet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Abdullah'
api = Api(app)


api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(Note, '/note')
api.add_resource(NoteGet, '/note/<int:user_id>')
api.add_resource(DeleteNot, '/note/<int:note_id>')


@app.before_first_request
def creat_tables():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)