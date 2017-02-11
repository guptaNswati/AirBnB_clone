#!/usr/bin/python3
"""
This is the Place class module. This module creates a Place class that inherits
from BaseModel.
"""
from models.base_model import BaseModel
import weakref

class Place(BaseModel):
    instance_list = []
    instance_count = 0
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.instance_list.append(weakref.proxy(self))
        self.__class__.instance_count += 1
