#!/usr/bin/python3

"""
This module defines the State class, which inherits from BaseModel.

State class represents a state in the AirBnB clone project.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing states in the AirBnB clone project.

    Attributes:
        name (str): Name of the state.
    """
    name = ""
