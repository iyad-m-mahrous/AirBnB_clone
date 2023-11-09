#!/usr/bin/python3
'''Write a class User that inherits from BaseModel'''
from .base_model import BaseModel


class User(BaseModel):
    '''User Class

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    '''
    email = ''
    password = ''
    firs_name = ''
    last_name = ''
