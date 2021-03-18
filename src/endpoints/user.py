import json
from flask import Blueprint, Response, request

from src.models.user import User
from src.utils.decorators import session

user_bp = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')


@user_bp.route('', methods=['GET'])
@session
def get_users(context):
    res = User.get_users(context)
    return Response(response=json.dumps(res), status=200)


@user_bp.route('', methods=['POST'])
@session
def register(context):
    User.create_user(context, request.json)
    return Response(response='Resource created', status=201)

@user_bp.route('', methods=['PUT'])
def put_user(context, user, id):
    pass


@user_bp.route('', methods=['PATCH'])
def patch_user(context, user, id):
    pass


@user_bp.route('', methods=['DELETE'])
def delete_user(context, user, id):
    pass

