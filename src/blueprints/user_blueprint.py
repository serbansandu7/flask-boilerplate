from flask import Blueprint, Response, request

from ..utils.database_utils import get_database_session
from ..models.user import User

import json

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api/v1/users')


@user_blueprint.route('/', methods=['GET'])
def get_users():
    user_list = get_database_session().query(User).all()
    return Response(response=json.dumps({'items': user_list}), content_type='application/json')


@user_blueprint.route('/{user_id}', methods=['GET'])
def get_user_profile():
    authorization = request.headers['Authorization']
    user = get_database_session().query(User).filter_by(password=authorization).first()
    return Response(response=json.dumps({
        'id': user.user_id,
        'email': user.email,
        'role': user.role,
        'full_name': user.user_full_name
    }))
