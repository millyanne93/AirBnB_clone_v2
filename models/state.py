#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    related_cities = relationship("City", cascade='all, delete, delete-orphan',
                                  backref="state")

    @property
    def cities(self):
        all_objects = models.storage.all()
        city_objects = []
        result = []
        for key in all_objects:
            key_parts = key.replace('.', ' ').split()
            if key_parts[0] == 'City':
                city_objects.append(all_objects[key])
        for elem in city_objects:
            if elem.state_id == self.id:
                result.append(elem)
        return result
