#!python3

import sys
import string, requests
import webbrowser
from os import system
from urllib.request import build_opener
from urllib.error import HTTPError
from random import choice

class Rangur:

    def rand_img_url(self):
        chars = string.ascii_letters + string.digits #chars holds all the possible characters an imgur ID can be
        # imgID = ''
        # for j in range(5):
        #     imgID += choice(chars)
        # ^ this is slow, see: http://docs.python-guide.org/en/latest/writing/structure/
        tempchar = [choice(chars) for n in range(5)]
        imgID = "".join(tempchar)
        url = "http://i.imgur.com/" + imgID
        return url
    
    def main(self):
        if len(sys.argv) >= 2:
            num_pics = int(sys.argv[1])
        else:
            num_pics = 3
    
        self.grab_some_images(num_pics)

                
class Logger(object): #this class will write all stdout to both stdout and a log file
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('stdout.log', "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): # for the python 3 flush command
        pass

if __name__ == '__main__':
    sys.stdout = Logger() #use Logger
    Rangur(False).main()
