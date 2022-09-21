from threading import Thread
import time 
import os

def test():
    os.system('bash scr2.sh')

def backup():
    os.system('yes')

if __name__ == '__main__':
    Thread(target=test).start()
    Thread(target=backup).start()
