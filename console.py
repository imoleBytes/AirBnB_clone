#!/usr/bin/python3

import cmd, sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	"""Prompt the user with "(hbnb)" before each command."""
	prompt = "(hbnb) "
	cmds = ["BaseModel"]

	def do_quit(self, arg):
		"""This cmd quit the console by returning True"""
		return True

                        
	def do_EOF(self, arg):                               
		"""Exit the command interpreter (Ctrl+D)"""
		print("exiting...")  # Add a newline before exiting
		sys.exit(0)

	def emptyline(self):
		"""Do nothing on empty line"""
		pass
    
	def do_create(self, arg):
			"""Creates a new instance of BaseModel and save to the Json file"""
			args = arg.split()
			if len(args) == 0:
				print("** class name missing **")
			elif args[0] not in HBNBCommand.cmds:
					print("** class doesn't exist **")
			else:
				obj = eval(args[0])()
				print(obj.id)
				storage.save()
	def do_show(self, arg):
		"""Prints the string representation of an instance based
		on the class name and id.
		Ex: $ show BaseModel 1234-1234-1234.
		  """
		args = self.validate_arg(arg)
		if not isinstance(args, list):
			return
		if len(args) == 1:
			print("** instance id missing **")
			return
		all_objts = storage.all()
		if f"{args[0]}.{args[1]}" not in all_objts:
			print("** no instance found **")
		else:
			print(all_objts[f"{args[0]}.{args[1]}"])


	@classmethod
	def validate_arg(cls, arg):
		"""validate the arguments. -1 for missing class,
		 -2 for class not exist and list of args for pass"""
		args = arg.split()
		if len(args) == 0:
			print("** class name missing **")
			return -1
		elif args[0] not in cls.cmds:
				print("** class doesn't exist **")
				return -2
		else:
			return args



if __name__ == '__main__':
    HBNBCommand().cmdloop()


