from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate, migrate
from app.resources.user import UserList, UserRegister
from app.resources.note import DeleteNot, Note, NoteGet
from config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config.from_object(Config)
    
    db.init_app(app)

    migrate = Migrate(app, db)


    @app.before_first_request
    def creat_tables():
        db.create_all()
        
    api = Api(app)
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserList, '/users')
    api.add_resource(Note, '/note')
    api.add_resource(NoteGet, '/note/<int:user_id>')
    api.add_resource(DeleteNot, '/note/<int:note_id>')

    return app


    




 
    