#!/usr/bin/python3
"""File storage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON&instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        """ fill dictionary with elements __objects """
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserializes the JSON file to __objects, only if the JSON exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    cls_name = obj_data['__class__']
                    if cls_name == 'BaseModel':
                        obj = BaseModel(**obj_data)
                    self.__objects[key] = obj
