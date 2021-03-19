import json
from flask import Blueprint, Response, request

from src.models.user import User
from src.utils.decorators import session, is_authorized, is_admin, is_admin_or_self, http_handling, log_action

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('', methods=['GET'])
@http_handling
@session
@is_authorized
@log_action("Get users")
def get_users(context, user):
    search = request.args.get('search')
    page = request.args.get('page')
    limit = request.args.get('limit')
    res = User.get_users(context, search, page, limit)
    return Response(response=json.dumps(res), status=200)


@user_bp.route('', methods=['POST'])
@http_handling
@session
def register(context):
    User.create_user(context, request.json)
    return Response(response='Resource created', status=201)


@user_bp.route('/<int:user_id>', methods=['PUT'])
@http_handling
@session
@is_authorized
@is_admin_or_self
@log_action("PUT user")
def put_user(context, user, user_id):
    User.update_user(context, request.json, user_id)
    return Response(response='Resource updated successfully', status=200)


@user_bp.route('/<int:user_id>', methods=['PATCH'])
@http_handling
@session
@is_authorized
@is_admin_or_self
@log_action("PATCH user")
def patch_user(context, user, user_id):
    User.update_user(context, request.json, user_id)
    return Response(response='Resource update successfully', status=200)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
@http_handling
@session
@is_authorized
@is_admin
@log_action("DELETE user")
def delete_user(context,  user, user_id):
    User.deactivate_user(context, user_id)
    return Response(response='Resource deleted successfully', status=200)