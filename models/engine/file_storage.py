#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""

import json


class FileStorage:
    """
    Private class attributes:
        __file_path
        __objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """instance that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """instance that Serializes __objects to the JSON file (path: __file_path)"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists."""
        try:
            with open(self.__file_path, 'r') as file:
                json_file = json.load(file)
                for key, value in json_file.items():
                    class_name, obj_id = key.split(',')
                    module = __import__('models', + class_name, fromlist=[class_name])
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            return
