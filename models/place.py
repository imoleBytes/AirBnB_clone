#!/usr/bin/python3

from models.base_model import BaseModel
"""this contains the Place Class"""


class Place(BaseModel):
    """Place class definition"""
    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id later
