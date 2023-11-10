#!/usr/bin/python3
'''a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes instances to a JSON file and deserializes
    JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
            <class name>.id (ex: to store a BaseModel object with id=12121212,
            the key will be BaseModel.12121212)
    '''
    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage. __objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = f'<{obj.__class__.__name__}>.{str(obj.id)}'
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        objects = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objects, file)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)'''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objects = json.load(file)
        except FileNotFoundError:
            return
        for key in objects.keys():
            cls = objects[key]['__class__']
            ret_obj = eval(cls)(**objects[key])
            self.new(ret_obj)
