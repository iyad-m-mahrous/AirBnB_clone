#!/usr/bin/python3
'''a class BaseModel that defines all common
attributes/methods for other classes'''

import uuid
import datetime


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
        '''Startup function'''
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.updated_at = self.create_at

    def __str__(self):
        '''String Presentation'''
        return (f'[{type(self).__name__}] ({self.id}) {str(self.__dict__)}')
