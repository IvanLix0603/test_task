import numpy as np 
import matplotlib.pyplot as plt
import os
from poly import PolyPredict

def preprocess_data(dir):
    os.chdir(dir)########3
    time = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' in file:
                time.append(file)
            #if 'var' in file:
             #   var.append(file)
    os.chdir('../')
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
    time_prev = preprocess_data('1_test')###my data
    result_data = list()
    time = preprocess_data('4_test')   
    for files in zip(time, time_prev):
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1])
        result_data.append([calc_time, data[2]])         
    draw_plot(result_data)
    pass 

def exctract_data(files):
    os.chdir('4_test')
    time = np.loadtxt(os.path.abspath(files[0]))
    os.chdir('../1_test')
    time_prev = np.loadtxt(os.path.abspath(files[1]))
    os.chdir('../')
    maxi = parser_name_files(files[0]) 
    data = (time, time_prev, maxi)
    return data

def parser_name_files(file): 
    number = file.split('_')[1] 
    return int(number)

def calculation_time(up_time, wup_time):    
    prof_up = 1/up_time
    prof_wup = 1/wup_time
    delta_prof = abs(prof_up - prof_wup) #############
    relation_prof = (delta_prof/prof_wup) * 100##########
    return relation_prof

def draw_plot(data): 
    
    x_name= (25, 50, 100, 150, 200, 300,500,1000, 1200)
    n_rows = len(data)
    N = np.arange(len(x_name))
    for row in range(n_rows):
        plt.bar(N[row], data[row][0])
    plt.xticks(N, x_name)
    plt.title('Отображение резултатов 4 теста')
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери производительности, %')
    plt.grid()
    plt.show()
    plt.savefig("Отображение резултатов 4 теста")


if __name__=='__main__':
    main()