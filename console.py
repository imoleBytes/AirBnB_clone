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
			else:
				if args[0] not in HBNBCommand.cmds:
					print("** class doesn't exist **")
				else:
					obj = eval(args[0])()
					print(obj.id)
					storage.save()
					
	





if __name__ == '__main__':
    HBNBCommand().cmdloop()


