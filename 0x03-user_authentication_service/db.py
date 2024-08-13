#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm import sessionmaker, Session
from user import Base, User


class DB:
    """DB class for interacting with the database."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Create a User object and save it to the database.
        
        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.
        
        Returns:
            User: The newly created User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.
        
        Args:
            **kwargs: Arbitrary keyword arguments for filtering.
        
        Returns:
            User: The first user found matching the filter criteria.
        
        Raises:
            NoResultFound: If no user is found matching the filter criteria.
            InvalidRequestError: If invalid arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except AttributeError as e:
            # Handle cases where an invalid attribute is provided
            raise InvalidRequestError from e
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
