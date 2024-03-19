#!/usr/bin/python3
"""
    Method for models directory, which initializes the package.

"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
