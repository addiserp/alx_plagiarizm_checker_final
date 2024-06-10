#!/usr/bin/python3
""" holds class User"""

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5
import models
from models.base_model import BaseModel, Base


class Utype(BaseModel, Base):
    """Representation of user type """
    if models.storage_t == 'db':
        __tablename__ = 'utypes'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes user type"""
        super().__init__(*args, **kwargs)
