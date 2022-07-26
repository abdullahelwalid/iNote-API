from app import db
from app.models.user import User
from app.views import bp
from flask import request, abort, jsonify
from app.models.category import Category
from app.models.notes import Note
from app.views.auth import auth_required


@bp.route("/category", methods=["GET", "PUT", "DELETE", "POST"])
@auth_required
def category():
    if request.method == "GET":
        user_id = request.args.get("user_id", default=None, type=str)
        if not user_id:
            abort(400, "one or more argument is missing")
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "User doesn't exist")
        category = user.category
        print(category)
        return jsonify([category.json() for category in category if category]), 200
    if request.method == "POST":
        if not request.json:
            abort(400, "request should be body JSON")        
        _data = request.json
        def _validate(request) -> bool:
            if "user_id" not in request:
                return False
            if "category" not in request:
                return False
            return True
        if not _validate(_data):
            abort(400, "one or more field is missing")
        user_id =  _data['user_id']
        category_name = _data['category'].lower()
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        category = Category.query.filter_by(category = category_name).first()
        if category:
            abort(400, "you have category with the same name")
        new_category = Category(
            category = category_name,
            user_id = user_id
        )
        db.session.add(new_category)
        db.session.commit()
        return jsonify(new_category.json()), 201
    if request.method == "PUT":
        if not request.json:
            abort(400, "request should be body JSON")    
        _data = request.json
        def _validate(request) -> bool:
            if "user_id" not in request:
                return False
            if "category_id" not in request:
                return False
            if "category" not in request:
                return False
            return True
        if not _validate(_data):
            abort(400, "one or more field is missing")
        user_id = _data['user_id']
        category_name = _data['category']
        category_id = _data['category_id']
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        category = Category.query.filter_by(id = category_id).first()
        if not category:
            abort(404, "category not found")
        if user.username != category.user_id:
            abort(403, "unable")
        category.category = category_name
        db.session.commit()
        return jsonify(category.json()), 200
    if request.method == "DELETE":
        if not request.json:
            abort(400, "request should be body JSON")    
        _data = request.json
        def _validate(request) -> bool:
            if "user_id" not in request:
                return False
            if "category_id" not in request:
                return False
            return True
        if not _validate(_data):
            abort(400, "one or more field is missing")
        user_id = _data['user_id']
        category_id = _data['category_id']
        user = User.query.filter_by(username = user_id).first()
        if not user:
            abort(404, "user not found")
        category = Category.query.filter_by(id = category_id).first()
        if not category:
            abort(404, "category not found")
        if user.username != category.user_id:
            abort(403, "unable")
        db.session.delete(category)
        db.session.commit()
        return jsonify("deleted"), 200
