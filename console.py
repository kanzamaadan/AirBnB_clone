#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: create BaseModel"""
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesnt't exist **")
            return
        new = BaseModel()
        storage.save()
        print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id. Ex: show BaseModel 1234-1234-123"""
        if not arg:
            print("** class name missing **")
            return
        arg = args.split(" ")
        class_name = arg[0]
        if clas_name not in ["BaseModel"]:
            print("** class doesnt't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1].strip('"\'')
        key = "{} {}".format(class_name, obj_dict)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instace found **")
            return
        print(all_objs[key])

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        quit()

    def emptyline(self):
        """Empty line command to do nothing\n"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
