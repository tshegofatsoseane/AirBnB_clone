#!/usr/bin/python3
"""Defines User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents User.

    Attributes:
        email (str): Email of user.
        password (str): Password of user.
        first_name (str): First name of user.
        last_name (str): Last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
