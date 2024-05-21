#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in 'created_at' or key in 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs or "__class__" not in kwargs:
            models.storage.new(self)

    def __str__(self):
        """A description of the entire function,
        its parameters, and its return"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
