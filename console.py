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
import re


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
            if (storage.all()[key].id == args[1] and
                    storage.all()[key].__class__.__name__ == args[0]):
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
            if (storage.all()[key].id == args[1] and
                    storage.all()[key].__class__.__name__ == args[0]):
                del storage.all()[key]
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
        if args and args[0]:
            print(
                    [str(obj) for obj in storage.all().values()
                        if obj.__class__.__name__ == args[0]]
                    )
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, line):
        ''' Updates an instance based on
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
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return
        is_str = 1
        try:
            args[3] = int(args[3])
            is_str = 0
        except Exception as e:
            try:
                args[3] = float(args[3])
                is_str = 0
            except Exception as e:
                pass
        for key in storage.all().keys():
            if (storage.all()[key].id == args[1] and
                    storage.all()[key].__class__.__name__ == args[0]):
                setattr(storage.all()[key], str(args[2]), args[3])
                storage.save()
                return
        print('** no instance found **')

    def default(self, line):
        '''Handling other commands'''
        args = line.split('.')
        if not (len(args) > 1):
            return
        if args[0] in globals():
            if args[1] == 'all()':
                print(
                        [str(obj) for obj in storage.all().values()
                            if obj.__class__.__name__ == args[0]]
                        )
            if args[1] == 'count()':
                print(
                        sum(obj.__class__.__name__ == args[0]
                            for obj in storage.all().values())
                        )
            if (args[1].startswith('show("') and
                    args[1].endswith('")')):
                start_index = args[1].find('("')
                end_index = args[1].find('")')
                obj_id = args[1][start_index + 2:end_index]
                self.do_show(f'{args[0]} {obj_id}')
            if (args[1].startswith('destroy("') and
                    args[1].endswith('")')):
                start_index = args[1].find('("')
                end_index = args[1].find('")')
                obj_id = args[1][start_index + 2:end_index]
                self.do_destroy(f'{args[0]} {obj_id}')
            if (args[1].startswith('update("') and
                    args[len(args)-1].endswith(')')):
                pattern = r'(.*?)\.(.*?)\(\"(.*?)\"'
                match = re.findall(pattern, line)
                idx1 = line.find('{')
                idx2 = line.find('}')
                if (idx1 > 0 and idx2 > 0):
                    elements = line[idx1 + 1:idx2]
                    pattern = r'[^\s\'\",:]+'
                    match2 = re.findall(pattern, elements)
                    num = len(match2) / 2
                    for i in range(int(num)):
                        self.do_update(
                                f'{match[0][0]} {match[0][2]} '
                                f'{match2[i*2]} {match2[i*2+1]}'
                                )
                else:
                    pattern = r'(.*?)\.(.*?)\(\"(.*?)\",\s*\"' \
                            '(.*?)\",\s*\"?(.*?)\"?\)'
                    match = re.findall(pattern, line)
                    self.do_update(
                            f'{match[0][0]} {match[0][2]} '
                            f'{match[0][3]} {match[0][4]}'
                            )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
