import pytest

from src.utils.validators import validate_email


class TestUserValidation:

    def test_user_email_validation_success(self):
        email = 'serban.sandu@gmail.com'
        validate_email(email)
        assert True

    def test_user_email_validation_failed(self):
        email = 'serban.sandu@gmail.comcxzc+'
        with pytest.raises(Exception) as e:
            validate_email(email)

        print(e)
