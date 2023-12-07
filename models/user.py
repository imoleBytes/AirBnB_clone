#!/usr/bin/python3

# models/user.py
from models.base_model  import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

def to_dict(self):
    user_dict = {
    "email": self.email
    "password": self.password
    "first_name": self.first_name
    "last_name": self.last_name
    }
    return user_dic
