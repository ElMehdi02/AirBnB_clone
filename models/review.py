#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing reviews
    of places in the AirBnB clone project.

    Attributes:
        place_id (str): ID of the place being reviewed.
        user_id (str): ID of the user who wrote the review.
        text (str): The review text.
    """
    place_id = ""
    user_id = ""
    text = ""
