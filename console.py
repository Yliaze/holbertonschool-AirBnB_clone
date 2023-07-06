#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
