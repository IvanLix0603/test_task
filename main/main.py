'''
1) Launch 1_test
2) Visual result 1_test
3) launch n_test, n = 1..4
4) visual result n_test.
5) load to db
6) load to NN
'''

import os

class Manager():
    def __init__(self, test):
        self.test = test

    def launch_test(self, test):
        os.chdir(f'big_test/{test}_test')
        try:
            signal = os.system('scr2.sh')
            if signal == 0:
                os.chdir('~/main')
            return signal 
        except OSError as e:
            print(f"PROGRAMM STOPED on launch by {e}")
             
    
    def visual_test(self, test):
        os.chdir(f'visual/{test}_test')
        try:
            signal = os.system(f'python3 {test}_test_hist.py')
            if signal == 0:
                os.chdir('~/main')
            return signal 
        except OSError as e:
            print(f"PROGRAMM STOPED on visual by {e}")
        
    def load_to_db(self, test):
        os.chdir('db/')
        try:
            signal = os.system(f'python3 {test}_result.txt')
            if signal == 0:
                os.chdir('~/main')
            return signal 
        except OSError as e:
            print(f"PROGRAMM STOPED on load data to db by {e}")
        
def manage():
    tests = [1, 2, 3, 4]
    manager = Manager()
    for i in tests:
        _= manager.launch(i)
        _= manager.visual(i)
        _= manager.load_to_db(i)
    
    

if __name__ == '__main__':
    manage()
