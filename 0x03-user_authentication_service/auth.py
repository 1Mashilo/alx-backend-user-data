#!/usr/bin/env python3

"""Auth module
"""
import bcrypt
from db import DB
from sqlalchemy.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string and returns it in bytes form
    Args:
        password (str): password in string format
    """
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with the provided email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the provided email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
