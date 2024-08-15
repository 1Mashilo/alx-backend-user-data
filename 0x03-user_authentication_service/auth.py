#!/usr/bin/env python3
"""Auth module
"""

import bcrypt
from db import DB
from sqlalchemy.exc import NoResultFound 
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt and returns the hashed password.
        
        Args:
            password (str): The password to hash.
            
        Returns:
            bytes: The salted hash of the password.
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

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
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

