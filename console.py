#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command line interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Print an empty line\n"""
        pass

    def do_create(self, args=None):
        list_arg = args.split()
        if not list_arg:
            print("** class name missing **")
        else:
            print(list_arg[0])
            try:
                obj = globals()[list_arg[0]]()
                obj.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
