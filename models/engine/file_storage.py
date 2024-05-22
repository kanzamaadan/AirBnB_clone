#!/usr/bin/python3
"""class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file & deserializes back to instances
    Private class attributes:
        __file_path
        __objects
    """
    __file_path = 'file.json'
    __objects = {}

    classes = {
               "BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review
               }

    def all(self):
        """instance that returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """instance that Serializes __objects
        to the JSON file (path: __file_path)"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__class__.__objects:
            json_objects[key] = self.__class__.__objects[key].to_dict()
        with open(self.__class__.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists."""
        try:
            with open(self.__class__.__file_path, 'r') as f:
                json_file = json.load(f)
                for key, value in json_file:
                    class_name = value['__class__']
                    cls = self.__class__.classes.get(class_name)
                    if cls:
                        obj = cls(**value)
                        self.__class__.__objects[key] = obj
        except FileNotFoundError:
            pass
