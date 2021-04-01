import re


def validate_user_body(body):
    validate_email(body["email"])
    validate_password(body["password"])
    validate_phone_number(body["phone"])


def validate_phone_number(number):
    if not number:
        raise Exception('Invalid Phone number.')

    if number.startswith('+40') or number.startswith('07'):
        if number[0] == '+':
            number = number[1:]

        if 9 < len(number) < 15:
            if number.isdigit():
                return

    raise Exception('Invalid Phone number.')


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    res = re.search(regex, email)
    if not res:
        raise Exception('Email is not a valid email address')


def validate_password(password):
    pass


def validate_company_body(body):
    validate_name(body.get("name", ''))
    validate_country(body.get('country', ''))


def validate_company_assignment(body):
    try:
        _, __ = body['user'], body['company']
    except KeyError:
        raise Exception("You must provide a company and a user")


def validate_name(name):
    if not name:
        raise Exception("You must provide a name")


def validate_country(country):
    if not country:
        raise Exception("You must provide a country")
