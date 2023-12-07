#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Prompt the user with "(hbnb)" before each command."""
    prompt = "(hbnb)"

    def to_quit(self, arg):
        return True
                        
    def do_EOF(self, arg):                               
        """Exit the command interpreter (Ctrl+D)"""
        print("exiting...")  # Add a newline before exiting
        sys.exit(0)

    def emptyline(self):
        """Do nothing on empty line"""
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()


def do_show_user(self,arg):
    """Implement the Showing of all users who have access to the system """

def do_creat_user(self,arg):
    """Implement the Adding new of user to the system"""

def do_destroy_user(self,arg):
    """Implement the Deleting of some previous users from the system"""

def do_update_user(self,arg):
    """Implement update of current user"""



