#!/usr/bin/python3
'''Write a class User that inherits from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City Class

    Attributes:
        Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''
    state_id = ''
    name = ''
