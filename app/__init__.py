from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.models import db
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
from app.views import bp
app.register_blueprint(bp)
