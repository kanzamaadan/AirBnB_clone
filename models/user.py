#!/usr/bin/python3
"""Representation of user in the application."""
from models.base_models import BaseModel

class User(BaseModel):
    """User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
