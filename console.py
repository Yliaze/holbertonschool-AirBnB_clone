#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine import file_storage
from models import storage


class HBNBCommand(cmd.Cmd):
    """command line interpreter"""

    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "State", "City",
                 "Place", "Amenity", "Review"]

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
            try:
                obj = globals()[list_arg[0]]()
                obj.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, args):
        list_arg = args.split()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif list_arg[1] == "":
            print("** instance id missing **")
        else:
            try:
                instance = storage.all()
                concat = list_arg[0] + '.' + list_arg[1]
                print(instance[concat])
            except:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
