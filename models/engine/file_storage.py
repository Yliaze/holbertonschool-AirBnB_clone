#!/usr/bin/python3
"""Module for FileStorage"""
import json
import os


class FileStorage:
    """Class FileStorage :
    Serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.amenity import Amenity
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                data = json.loads(file.read())
                for k in data.keys():
                    v = data[k]
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)

                return FileStorage.__objects
        except ValueError:
            return {}
