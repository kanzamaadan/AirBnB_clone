#!!/usr/bin/python3

import json


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj, file)

    def reload(self):
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
