#!/usr/bin/python3

from models.base_model import BaseModel
"""this contains the User Class"""

class User(BaseModel):
	"""User class definition"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""
