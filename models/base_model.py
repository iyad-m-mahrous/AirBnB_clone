#!/usr/bin/python3
'''a class BaseModel that defines all common
attributes/methods for other classes'''

import uuid
import datetime
import models


class BaseModel:
    '''Base Class

    Attributes:
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when
        an instance is created
        updated_at: datetime - assign with the current datetime when
        an instance is updated
    '''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            del kwargs['__class__']
            kwargs['created_at'] = \
                datetime.datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = \
                datetime.datetime.fromisoformat(kwargs['updated_at'])
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''String Presentation'''
        return (
                f'[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}'
               )

    def save(self):
        '''updates the public instance attribute updated_at with
        the current datetime'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values
        of __dict__ of the instance'''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
