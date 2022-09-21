#!/usr/bin/python3
###SEPARATE ON H, M, S#####
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def prepare(files_list):
    print (files_list)
    #для варианта О0
    data_0 = [[],[]]
    for i in range(2):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_0[i].append(file.read())

    time_0 = parser_time(data_0[0])
    num_vars_0 = parser_data(data_0[1]) 
    
    #для варианта О1
    data_1 = [[],[]]
    for i in range(2,4):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_1[i-2].append(file.read())

    time_1 = parser_time(data_1[0])
    num_vars_1 = parser_data(data_1[1]) 

    #для варианта О2
    data_2 = [[],[]]
    for i in range(4,6):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_2[i-4].append(file.read())

    time_2 = parser_time(data_2[0])
    num_vars_2 = parser_data(data_2[1]) 

    draw_plot(time_0, num_vars_0,time_1, num_vars_1,time_2, num_vars_2)
    
    
def parser_time(time):
    time = time[0].split('\n')
    time.pop(-1)
    tmp = []
    for i in time:
        tmp_i = 0
        m = i.split('m')
        t = float(m[0])
        tmp_i += t*60
        m[1]=m[1].replace(',','.')
        sec = float(m[1].split('s')[0])
        #print(sec)
        tmp_i += sec
        tmp.append(tmp_i)
    time = np.array(tmp)
    return time

def parser_data(data):
    tmp = data[0].split('\n')
    tmp.pop(-1)
    #print(tmp)
    num_vars = []
    for i in range(len(tmp)):
        num_vars.append(int(tmp[i]))
    num_vars = np.array(num_vars)
    return num_vars

def draw_plot(time_0, num_vars_0,time_1, num_vars_1,time_2, num_vars_2): 
    
    name_vars='results/vars_'+str(max(num_vars_0))
    name_time='results/time_'+str(max(num_vars_0))
    np.savetxt(name_vars,num_vars_0)
    np.savetxt(name_time,time_0)
    
    name_vars='results/vars_'+str(max(num_vars_1))
    name_time='results/time_'+str(max(num_vars_1))
    np.savetxt(name_vars,num_vars_1)
    np.savetxt(name_time,time_1)
    
    name_vars='results/vars_'+str(max(num_vars_2))
    name_time='results/time_'+str(max(num_vars_2))
    np.savetxt(name_vars,num_vars_2)
    np.savetxt(name_time,time_2)
    
if __name__== '__main__':
    files_list = []
    for i in range(1, 7):
        files_list.append(sys.argv[i])
    prepare(files_list)
