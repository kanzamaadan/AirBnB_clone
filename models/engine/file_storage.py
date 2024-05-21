#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from modesl.user import User


class FileStorage:
    """
    serializes instances to a JSON file & deserializes back to instances
    Private class attributes:
        __file_path
        __objects
    """
    classes = {"user": User}


    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """instance that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """instance that Serializes __objects to the JSON file (path: __file_path)"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in FileStorge.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_file = json.load(f)
                for key, value in json_file:
                    class_name, obj_id = key.split(',')
                    module = __import__('models', + class_name, fromlist=[class_name])
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
