import os
import sys
class Logger(object):
    def __init__(self, filename = "Default.log", mode = 'w', encoding = 'utf-8'):
        self.terminal = sys.stdout
        self.log = open(filename, mode, encoding = encoding)

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass