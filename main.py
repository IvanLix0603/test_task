import os
import sqlite3 

class Manager():
    def __init__(self):
        pass

    def launch_test(self, test):
        os.chdir(f'big_test/{test}_test')
        print("in launch\n")
        os.system('pwd')
        signal = os.system('bash scr2.sh')
        if signal == 0:
            os.chdir('../../')
            return signal  
    
    def visual_test(self, test):
        print("in visual\n")
        os.chdir(f'visual/')
        os.system('pwd')
        signal = os.system(f'python3 {test}_test_hist.py')
        if signal == 0:
            os.chdir('../')
            return signal 
   
    def load_to_db(self, test):
        print("in load_to_bd\n")
        os.chdir('db')
        #os.chdir('../db/')
        signal = os.system(f'python3 load.py  {test}')
        if signal == 0:
            os.chdir('../')
            return signal
        
def clear_DB():
    os.chdir('db/')
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    task = '''DELETE from results'''
    cur.execute(task)
    con.commit()
    cur.close()
    os.chdir('../')



def manage():
    os.system('pwd')
    os.system('python3 parse_cpu.py')
    tests = [2,3,4]
    manager = Manager()
    for i in tests:
        #os.system('pwd')
        _= manager.launch_test(i)
        #os.system('clear')
        os.system('pwd')
        _= manager.visual_test(i)
        #os.system('clear')
        os.system('pwd')
        _= manager.load_to_db(i)
       # os.system('clear')
        os.system('pwd')

    
    

if __name__ == '__main__':
    manage()
