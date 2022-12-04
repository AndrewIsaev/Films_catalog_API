import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    """
    Class with User`s CRUD
    """

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        """
        Return all users
        """
        return self.dao.get_all()

    def get_one(self, uid: int) -> UserDAO:
        """
        Return user by id
        """
        return self.dao.get_one(uid)

    def get_by_email(self, email: str) -> UserDAO:
        """
        Return User by email
        """
        return self.dao.get_by_email(email)

    def create(self, user_data: dict) -> UserDAO:
        """
        Create user with hash password
        """
        user_data["password"] = self.get_hash(user_data.get("password"))
        return self.dao.create(user_data)

    def update(self, user_data: dict) -> UserDAO:
        """
        Update user`s data
        """
        self.dao.update(user_data)
        return self.dao

    def update_password(self, user_data: dict):
        """
        Update user password
        """
        email = user_data.get("email")
        user = self.get_by_email(email)
        password_1 = user_data.get("password_1")
        password_2 = user_data.get("password_2")
        if self.compare_passwords(password_1, user.password):
            user_data["password_2"] = self.get_hash(password_2)
            return self.dao.update_password(user_data), 201

    def get_hash(self, password: str) -> bytes:
        """
        Hash user password
        """
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password: str, hash_password: bytes) -> bool:
        """
        Compare passwords
        """
        return hmac.compare_digest(hash_password, base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )))
