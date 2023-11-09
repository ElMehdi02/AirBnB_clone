#!/usr/bin/python3
"""
This module defines the Place class, which inherits from BaseModel.

Place class represents a place that can be rented in the AirBnB clone project.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for representing places in the AirBnB clone project.

    Attributes:
        city_id (str): ID of the city where the place is located.
        user_id (str): ID of the user who owns the place.
        name (str): Name of the place.
        ...
        amenity_ids (list): List of amenity IDs associated with the place.
    """

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
    amenity_ids = []
