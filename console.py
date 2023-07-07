#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
import cmd
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
        """create an instance"""
        list_arg = args.split()
        if not list_arg:
            print("** class name missing **")
        else:
            try:
                obj = globals()[list_arg[0]]()
                obj.save()
                print(obj.id)
            except ValueError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """print objects infos"""
        list_arg = args.split()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 2:
            try:
                instance = storage.all()
                concat = list_arg[0] + '.' + list_arg[1]
                print(instance[concat])
            except ValueError:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, args):
        """destroy an object"""
        list_arg = args.split()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 2:
            try:
                dictionnary = storage.all()
                del dictionnary[list_arg[0] + '.' + list_arg[1]]
                storage.save()
            except ValueError:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, args):
        """list all objects"""
        dictionnary = storage.all()
        new_list = []
        if args == "":
            for value in dictionnary:
                new_list.append(str(dictionnary[value]))
            print(new_list)
        else:
            if args not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for value in dictionnary:
                    new_list.append(str(dictionnary[value]))
                print(new_list)

    def do_update(self, args):
        """ Update an instance """
        list_arg = args.split(" ")
        my_dictionnary = storage.all()
        try:
            concat = str(list_arg[0]) + "." + str(list_arg[1])
        except ValueError:
            concat = "None"
            list_arg.append("")

        if list_arg[0] == "":
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif list_arg[1] == "":
            print("** instance id missing **")
        elif concat not in my_dictionnary:
            print("** no instance found **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")

        elif len(list_arg) == 4:
            concat = list_arg[0] + '.' + list_arg[1]
            for k, v in my_dictionnary.items():
                if k == concat:
                    setattr(v, list_arg[2], list_arg[3])
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
