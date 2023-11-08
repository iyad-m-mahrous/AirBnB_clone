#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class'''

    prompt = '(hbnb) '
    use_rawinput = False

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF to exit the program'''
        return True

    def emptyline(self):
        '''What happens when pressing enter'''
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
