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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                self.__object = json.load(f)
                return self.__object
            
