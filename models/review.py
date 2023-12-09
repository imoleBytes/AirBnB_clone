#!/usr/bin/python3

from models.base_model import BaseModel
"""this contains the Review Class"""


class Review(BaseModel):
    """Review class definition"""
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
