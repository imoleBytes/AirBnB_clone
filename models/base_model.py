"""This module house the BaseModel Class on which other classes inherit from"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""BaseModel defines all common attributes/methods for other classes"""
	def __init__(self) -> None:
		"""initializes attributes
		Args:
			id - an uuid when an instance is created.
			created_at: the current datetime when an instance is created.
			updated_at: the current datetime when an instance is created
			and it will be updated every time you change your object.
		"""
		self.id = str(uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()

	def __str__(self) -> str:
		"""returns the string representio of the object"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""updates `updated_at` with the current datetime"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""returns a dictionary containing all keys/values of the instance"""
		self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
		self.__dict__["__class__"] = self.__class__.__name__
		return self.__dict__
