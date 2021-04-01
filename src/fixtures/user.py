import pytest

from src.models.user import User


@pytest.fixture
def test_user():
    user = User()
    entry = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'noreply+john.doe@organization.com',
        'phone': '074' * 5,
        'active': True
    }
    return user.to_object(entry)
