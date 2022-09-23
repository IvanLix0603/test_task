import numpy as np 
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
#plot столбчатая диаграмма

def preprocess_data(dir):
    files = []
    os.chdir(dir)########3
    time = []
    var = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' in file:
                time.append(file)
            #if 'var' in file:
             #   var.append(file)
    return sort_data(time)#, sort_data(var)

def sort_data(tmp):
    tmp = np.array(tmp)
    index = np.array([])
    for i in tmp:
        m = int(i.split('_')[1])
        index = np.append(index, m)
    sor = np.argsort(index)
    tmp = tmp[sor]
    return list(tmp)

def main():
    time_prev = preprocess_data('without_user_proc')###my data
    result_data = list()
    time = preprocess_data('2_test')    
    for files in zip(time, time_prev):
        #print(files)
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1])
        result_data.append([calc_time, data[2]])         
    print(result_data[2][0])

    #plt.hist(result_data[0][0])
    os.chdir('../')#####

    pass 

def exctract_data(files):
    time = np.loadtxt(os.path.abspath(files[0]))
    time_prev = np.loadtxt(os.path.abspath(files[1]))
    maxi = parser_name_files(files[0]) 
    data = (time, time_prev, maxi)
    return data

def parser_name_files(file): 
    number = file.split('_')[1] 
    return int(number)

def calculation_time(up_time, wup_time):    
    #print(expect_time)
    delta_time = abs(up_time - wup_time) #############
    relation_time = (up_time/wup_time) * 100##########
    #print(relation_time)
    return relation_time

if __name__=='__main__':
    main()