import re


def validate_user_body(body):
    validate_email(body["email"])
    validate_password(body["password"])


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    res = re.search(regex, email)
    if not res:
        raise ValidationError('Email is not a valid email address')


def validate_password(password):
    pass
