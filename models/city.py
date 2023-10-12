#!/usr/bin/python3
"""Defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents city.

    Attributes:
        state_id (str): State id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
