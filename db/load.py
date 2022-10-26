import sqlite3 as sql3
import sys
import json
import os
import numpy as np


def parse_cpu(file):
    f = open(file, 'r')
    data = json.load(f)
    f.close()
    print(data)
    #task = [f'{data["Architecture"]}, {data["CPU(s):"]}, {data["CPU MHz"]}, {data["CPU max MHz"]}, {data["CPU min MHz:"]}, {data["L1d cache"]}, {data["L1i cache"]}, {data["L2 cache"]}, {data["L3 cache"]}, {bool(1)}'
    task = [data["Architecture"], data["CPU(s)"], data["CPU MHz"], data["CPU max MHz"], data["CPU min MHz"], data["L1d cache"], data["L1i cache"], data["L2 cache"], data["L3 cache"], bool(1)]
    return task

def parse_delta(file) -> tuple :
    task_n = file.split('_')[-1].split(".")[0]
    print(task_n)
    data = np.loadtxt(os.path.abspath(file))
    task_delta = data#del
    print(task_delta)#del
    return task_delta, task_n


def mainly(test):
    conn = sql3.connect('data.db')
    cursor = conn.cursor()
    if test == '2':
         print("HIIIIIIII")
         files = ['cpuinfo.json', f'delta_{test}_test_25.txt',  
            f'delta_{test}_test_50.txt', f'delta_{test}_test_100.txt',
            f'delta_{test}_test_150.txt', f'delta_{test}_test_200.txt']

    else:
        files = ['cpuinfo.json', f'delta_{test}_test_25.txt',  
            f'delta_{test}_test_50.txt', f'delta_{test}_test_100.txt',
            f'delta_{test}_test_150.txt', f'delta_{test}_test_200.txt', 
            f'delta_{test}_test_300.txt', f'delta_{test}_test_500.txt',
            f'delta_{test}_test_1000.txt', f'delta_{test}_test_1200.txt']
    
    task_cpu = parse_cpu(files[0]) 
    for i in files[1:]:
        task_delta, task_n = parse_delta(i)
        task_delta = str(task_delta)
        task_n = str(task_n)
        task_test = str(test)
        if test == 2:
            task_O1 = str(0)
            task_O2 = str(1)
        else:
            task_O1 = str(1)
            task_O2 = str(0)
        sql = 'INSERT INTO results(arch, cpus, CPU_MHz, CPU_max_MHz, CPU_min_MHz, L1d_cashe, L1i_cashe, L2_cashe, L3_cashe, hyper_thread, N, O1, O2, test_number, loss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        #task =  (task_cpu + ', ' + task_n + ', ' + task_O1 + ', ' + task_O2 + ', ' +task_test + ', ' + task_delta)
        task = [*task_cpu, task_n, task_O1, task_O2, task_test, task_delta]
        print(task)
        #conn = sql3.connect('data.db')
        #cursor = conn.cursor()
        cursor.execute(sql, task)
    conn.commit()
    conn.close()
    os.system('cp data.db ../nn')

        
            

if  __name__== '__main__':
    mainly(sys.argv[1])
