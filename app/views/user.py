from app.views import bp
from flask import request, abort, jsonify
from app.models.user import User
from app.views.helper import validate_input
from app.models import db
import hashlib


@bp.route('/sign-up', methods = ['POST'])
def user():
    if not request.json:
        abort(400, "request should be body JSON")
    data = request.json

    def _validate(request) -> bool:
        if "username" not in request:
            return False
        if "email" not in request:
            return False
        if "firstname" not in request:
            return False
        if "lastname" not in request:
            return False
        if "password" not in request:
            return False
        return True
    
    if not _validate(data):
        abort(400, "one or more field is missing")
    username = None if len(data['username']) < 3 else data['username'].lower()
    email = None if len(data['email']) < 6 else data['email'].lower()
    firstname = None if len(data['firstname']) < 1 else data['firstname'].lower()
    lastname = None if len(data['lastname']) < 1 else data['lastname'].lower()
    password = None if len(data['password']) < 7 else data['password']

    if not validate_input(username, email, firstname, lastname, password):
        abort(400, "invalid data")
    password = hashlib.sha256(password.encode()).hexdigest()
    user_name = User.query.filter_by(username = username).first()
    if user_name:
        abort(400, "user already exist")
    user_email = User.query.filter_by(email = email).first()
    if user_email:
        abort(400, "email already exist")
    user = User(
        username = username,
        email = email,
        firstname = firstname,
        lastname = lastname,
        password = password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.json()), 201


@bp.route("/sign-in", methods=["POST"])
def sign_in():
    if not request.json:
        abort(400, "request should be body JSON")
    data = request.json
    def _validate(request) -> bool:
        if "user_id" not in request:
            return False
        if "password" not in request:
            return False
        return True
    if not _validate(data):
        abort(400, "one or more data field is missing")
    user_id = data['user_id']
    password = data['password']