#!/usr/bin/env python3
"""
This module provides a function to hash passwords using bcrypt.
"""

import bcrypt

def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password.
    
    Args:
        password (str): The password to hash.
        
    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
