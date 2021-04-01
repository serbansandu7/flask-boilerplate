import json

from flask import Blueprint, Response, request

from src.models.email_token import EmailToken
from src.models.user import User
from src.utils.decorators import http_handling, session

email_bp = Blueprint('email', __name__, url_prefix='')


@email_bp.route('/email-confirmation', methods=['GET'])
@http_handling
@session
def validate_email(context):
    email_token = EmailToken.get_email_token(context, request.args.get('token'))
    User.activate_user(context, email_token.user_id)
    return Response(status=200, response=json.dumps({'message': 'Email confirmed successfully.'}))
