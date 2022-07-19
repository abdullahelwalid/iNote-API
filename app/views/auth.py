from app.models.user import User
import jwt
from flask import abort, request
import functools


def auth_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or len(token) < 10:
            abort(401, "Invalid token")
        
        token = token.split(" ")[1]
        resp = User.decode_auth_token(token)
        def _validate():
            if request.json:
                if "user_id" in request.json:
                    return request.json['user_id']
            if request.args.get("user_id", type=str, default=None):
                return request.args.get("user_id", type=str, default=False)
            return False
        if not _validate():
            abort(401, "Authentication is unsuccessful")
        if not isinstance(resp, bool):
            user_id = _validate()
            if user_id != resp:
                abort(401, "Unauthorized")
            user = User.query.filter_by(username=resp).first()
            if user:
                return f(*args, **kwargs)
        abort(401, "Authentication failed")
    return wrapper

