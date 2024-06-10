#!/usr/bin/python3
""" holds class biddoc"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Biddoc(BaseModel, Base):
    """Representation of biddoc """
    if models.storage_t == "db":
        __tablename__ = 'biddocs'
        name = Column(String(128), nullable=False)
        url = Column(Text, nullable=True)
        codetext = Column(Text, nullable=True)
    else:
        name = ""
        url = ""

    def __init__(self, *args, **kwargs):
        """initializes bid docs"""
        super().__init__(*args, **kwargs)
