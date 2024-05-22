#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
import shlex
import re
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"

    classes = {
               "BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review
               }

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: create BaseModel"""

        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesnt't exist **")
            return
        new = BaseModel()
        models.storage.save()
        print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id.
        Ex: show BaseModel 1234-1234-123"""

        if not arg:
            print("** class name missing **")
            return
        arg = arg.split(" ")
        class_name = arg[0]
        if class_name not in ["BaseModel"]:
            print("** class doesnt't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1].strip('"\'')
        key = "{} {}".format(class_name, obj_id)
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instace found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if arg == 0:
            print("** class name missing **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1]
        key = "{} {}".format(class_name, obj_id)
        obj_dict = models.storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[key]
        models.storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class namei"""
        obj_list = []

        if arg:
            arg = arg.split(" ")
            class_name = arg[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            obj_dict = models.storage.all()
            for key, value in obj_dict.items():
                obj_list.append(str(value))
        else:
            obj_dict = model.storage.all()
            for value in obj_dict.values():
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        <class name>.update("<id>", "<attribute name>", "<attribute value>")
        Parameters:
            arg (str): The name of the class followed by the instance ID,
            attribute name, and new value separated by spaces.
        Returns:
            None
        Raises:
            ValueError: If there is an error parsing the argument string.
            ValueError: If the class name is missing.
            ValueError: If the instance ID is missing.
            ValueError: If the attribute name is missing.
            ValueError: If the value is missing.
            ValueError: If the class does not exist.
            ValueError: If no instance is found.
            ValueError: If the attribute does not exist.
            ValueError: If the value is of an invalid type.
        """
        arg = arg.split(" ")
        class_name = arg[0]
        try:
            arg = shlex.split(arg)
        except ValueError:
            print("** value error **")
            return

        if len(arg) < 1:
            print("** class name missing **")
            return
        match = re.search(r'\{.*\}', arg)
        obj_dict = models.storage.all()
        obj_id = re.sub(r'[",]', '', arg[1])

        if match:
            extracted_dic_str = match.group(0)
            dict_update = eval(extracted_dic_str)

            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
                return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[1]
        all_obj = models.storage.all()
        key = "{} {}".format(class_name, obj_id)
        if key not in all_obj.items():
            print("** no instance found **")
            return
        obj = obj_dict[key]

        for attr, value in dict_update.items():
            if hasattr(obj, attr):
                attr_type = type(getattr(obj, attr))
                try:
                    value = attr_type(value)
                except ValueError:
                    print("** invalid value type **")
                    continue

            else:
                try:
                    if isinstance(value, str):
                        value = eval(value)
                    elif isinstance(value, (int, float, bool)):
                        pass
                    elif isinstance(value, (list, dict)):
                        value = eval(str(value))
                    else:
                        print("**  invalid value type **")
                        continue
                except (NameError, SyntaxError):
                    pass
            setattr(obj, attr, value)
            obj.updated_at = datetime.now()
            models.storage.save()

        else:
            if len(arg) < 4:
                if arg[0] not in ["BaseModel"]:
                    print("** class doesn't exist **")
                elif key not in obj_dict:
                    print("** no instance found **")
                elif len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                    return

            obj_attr = re.sub(r'[",]', '', arg[2])
            obj_value = re.sub(r'[",]', '', arg[3])
            obj = obj_dict[key]
            if hasattr(obj, obj_attr):
                attr_type = type(getattr(obj, obj_attr))
                try:
                    obj_value = attr_type(obj_value)
                except ValueError:
                    print("** invalid value type **")
                    return
                else:
                    try:
                        obj_value = eval(obj_value)
                    except (NameError, SystemError):
                        pass
                setattr(obj, obj_attr, obj_value)
            obj.save()
            models.storage.save()

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
