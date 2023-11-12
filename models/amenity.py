#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.

Amenity class represents an amenity that can be
associated with a place in the AirBnB clone project.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing the amenities in the AirBnB clone project.

    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
