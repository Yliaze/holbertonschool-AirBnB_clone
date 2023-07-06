#!/usr/bin/python3
import cmd

"""contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """command line interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        'Quit command to exit the program\n'
        return True

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
