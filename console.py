#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''EOF to exit the program\n'''
        return True

    def emptyline(self):
        '''What happens when pressing enter\n'''
        return False

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist **")
            return
        obj = globals()[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        ''' Prints the string representation of an instance based on
        the class name and id'''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key in storage.all().keys():
            if storage.all()[key].id == args[1]:
                print(storage.all()[key])
                return
        print('** no instance found **')

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id'''

        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key in storage.all().keys():
            if storage.all()[key].id == args[1]:
                del(storage.all()[key])
                storage.save()
                return
        print('** no instance found **')

    def do_all(self, line):
        '''Prints all string representation of all instances based or not
        on the class name'''

        args = line.split()
        if (
                args and not (
                    args[0] in globals() and callable(globals()[args[0]])
                    )
                ):
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()])

    def do_update(self, line):
        ''' Updates an instance based on
        the class name and id'''
        attr_value = ''
        args = line.split('"')
        if len(args) < 2:
            args = line.split()
        else:
            attr_value = args[1]
            args = args[0]
            args = args.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if not attr_value:
            print('** value missing **')
            return
        for key in storage.all().keys():
            if storage.all()[key].id == args[1]:
                setattr(storage.all()[key], str(args[2]), str(attr_value))
                storage.save()
                return
        print('** no instance found **')

    def default(self, line):
        '''Handling other commands'''
        args = line.split('.')
        if not (len(args) == 2 and args[1] == 'all()'):
            return
        if args[0] in globals():
            print(
                    [str(obj) for obj in storage.all().values()
                        if obj.__class__.__name__ == args[0]]
                    )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
