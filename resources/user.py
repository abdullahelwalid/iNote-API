from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', 
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_user_by_name(data['username']):
            return {'message': 'User already exists'}, 400
        user = UserModel(**data)
        user.save_data_to_db()
        return {'message': 'Thank you for creating an account'}, 201

class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}, 201