#!/usr/bin/python3
"""
    console.py
    - Program entry point for the command interpreter
"""
import cmd
import json
from models.base_model import BaseModel
from models.__init__ import storage

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

    def emptyline(self):
        """
        Handles an empty line (do nothing)
        """
        pass

    def do_create(self, arg):
        """
        Create command to create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        All command to print string representation of all instances
        """
        args = arg.split()
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            instances = [str(instance) for key, instance in storage.all().items()
                          if not args or instance.__class__.__name__ == args[0]]
            print(instances)

    def do_update(self, arg):
        """
        Update command to update an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                setattr(instance, args[2], args[3])
                instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
