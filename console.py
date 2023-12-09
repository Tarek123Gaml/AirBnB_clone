#!/usr/bin/python3
"""
    console.py
    - Program entry point for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand
    - Class implementing the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
