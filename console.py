#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"

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
