from threading import Thread
import time 
import os

def test():
    sig=os.system('bash scr2.sh')

def backup():
    os.system('yes > /dev/null 2>&1 &')

if __name__ == '__main__':
    Thread(target=test).start()
    Thread(target=backup).start()

