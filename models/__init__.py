#!/usr/bin/python3
"""init file for the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()


