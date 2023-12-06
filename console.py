#!/usr/bin/python3

import cmd

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


