#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel 


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
        try:
            obj = globals()[args[0]]()
        except Exception as e:
            print("** class doesn't exist *")
            return
        obj.save()
        print(obj.id)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
