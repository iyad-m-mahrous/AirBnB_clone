#!/usr/bin/python3
'''Initialization File'''
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
