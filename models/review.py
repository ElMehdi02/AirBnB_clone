#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Reiew(baseModel):
    """
    Review class for representing reviews
    of place in the AirBnB clone project.

    Attributes: 
     place_id (str): ID of the place being reviewed.
     user_id (str): ID of the user who wrote the review.
     text (str): The review text.
    """
    place_id = ""
    user_id = ""
    text = ""
