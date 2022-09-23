import numpy as np 
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
#plot столбчатая диаграмма

def preprocess_data(dir):
    files = []
    os.chdir(dir)########3
    time_0 = []
    time_1 = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' and '_O0' in file:
                time_0.append(file)
            if 'time' and '_O1' in file:
                time_1.append(file)
    return sort_data(time_0), sort_data(time_1)

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
    result_data = list()
    time_0, time_1 = preprocess_data('2_test')    
    for files in zip(time_0, time_1):
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1])
        result_data.append([calc_time, data[2]])   ###################      
    os.chdir('../')
    draw_plot(result_data)
    #plt.hist(result_data[0][0])
   #####

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

def calculation_time(time_0, time_1):    
    #print(expect_time)
    delta_time = abs(time_0 - time_1) #############
    relation_time = (delta_time/time_1) * 100##########
    #print(relation_time)
    return relation_time

def draw_plot(data): 
    
    x_name= (25, 50, 100, 150, 200)
    n_rows = len(data)
    N = np.arange(len(x_name))
    for row in range(n_rows):
        plt.bar(N[row], data[row][0])
    plt.xticks(N, x_name)
    plt.title('Отображение резултатов 2 теста')
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери производительности, %')
    plt.grid()
    plt.show()
    plt.savefig("Отображение резултатов 2 теста")


if __name__=='__main__':
    main()