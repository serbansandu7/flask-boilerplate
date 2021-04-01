import pytest

from src.utils.validators import validate_phone_number


class TestPhoneValidation:

    def test_phone_number_validation_success(self):
        phone_number = '+40757999999'
        validate_phone_number(phone_number)
        assert True

    def test_phone_number_validation_failed(self):
        phone_number = '+407579999991x'
        with pytest.raises(Exception) as e:
            validate_phone_number(phone_number)
