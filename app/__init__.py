from flask import Flask
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
from app.views import bp
app.register_blueprint(bp)
