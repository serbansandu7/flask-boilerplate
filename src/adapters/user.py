import bcrypt
import hashlib

from binascii import a2b_qp
from numpy import random


class UserAdapter:
    @staticmethod
    def to_json(results, total):
        return {
            "items": [
                {
                    'id': result.id,
                    'first_name': result.first_name,
                    'last_name': result.last_name,
                    'email': result.email,
                    'phone': result.phone,
                    'active': result.active
                } for result in results
            ],
            "total": total
        }

    def to_object(self, body):
        for key, value in body.items():
            if key == 'password':
                password, salt = self.generate_password(value)
                self.password = password
                self.salt = salt
            else:
                if hasattr(self, key):
                    setattr(self, key, value)

    @staticmethod
    def generate_password(password, salt=None):
        if not salt:
            salt = bcrypt.gensalt()
        password = bcrypt.hashpw(a2b_qp(password), salt)
        return password.decode('utf-8'), salt.decode('utf-8')


    @staticmethod
    def generate_session():
        return hashlib.sha256(random.bytes(1024)).hexdigest()
