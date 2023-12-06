#!/usr/bin/python3

"""This house classes that abstract the storage"""
import json



class FileStorage:
	"""This class serializes instances to a JSON file
	and deserializes JSON file to instances.
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""returns all the objects in a dictionary, __objects"""
		return FileStorage.__objects
	
	def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})
	
	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		
		objects_dicts = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
		
		
		with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
			json.dump(objects_dicts, file)
	
	def reload(self):
		"""deserializes the JSON file to __objects
		(only if the JSON file (__file_path) exists;
		otherwise, do nothing. If the file doesn’t exist,
		no exception should be raised)"""
		try:
			with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
				FileStorage.__objects = json.load(file)
		except FileNotFoundError:
			return
		

		