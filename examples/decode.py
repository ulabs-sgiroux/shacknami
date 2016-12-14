import os
from pyvit.file.db.jsondb import JsonDbParser
from pyvit.hw import socketcan

parser = JsonDbParser()
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example_db.json')
b = parser.parse(file_path)

help(b)