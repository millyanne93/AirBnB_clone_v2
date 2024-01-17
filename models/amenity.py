#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = Table(
            'place_amenity',
            Base.metadata)
=======
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class for amenities"""
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
>>>>>>> 7316985866ff340629b0bdc6fd1d5083350932e3
