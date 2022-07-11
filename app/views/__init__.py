from flask import Blueprint

bp = Blueprint('views', __name__)

from app.views import note, user