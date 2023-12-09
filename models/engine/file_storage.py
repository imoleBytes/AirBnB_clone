#!/usr/bin/python3

"""This house classes that abstract the storage"""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}   # key will be <class name>.id

    def all(self):
        """returns all the objects in a dictionary, __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # FileStorage.__objects
        objects_dicts = \
            {
                i: FileStorage.__objects[i].to_dict()
                for i in FileStorage.__objects.keys()
            }

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dicts, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                # FileStorage.__objects = json.load(file)
                objectdicts = json.load(file)
                for obj in objectdicts.values():
                    class_name = obj["__class__"]
                    # del obj["__class__"]
                    self.new(eval(class_name)(**obj))
                    # eval(class_name)()here is why those classes are imported
        except FileNotFoundError:
            return
