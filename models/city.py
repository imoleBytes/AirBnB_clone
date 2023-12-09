#!/usr/bin/python3

from models.base_model import BaseModel
"""this contains the City Class"""


class City(BaseModel):
    """City class definition"""
    state_id = ""  # it will be the `State.id`
    name = ""
