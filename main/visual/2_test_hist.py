import numpy as np 
import matplotlib.pyplot as plt
import os

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
    result_data = dict()
    time_0, time_1 = preprocess_data('2_test')    
    for files in zip(time_0, time_1):
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1])
        result_data[data[2]] = calc_time  ###################      
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
    del_null = lambda x: x+0.0001
    time_0 = del_null(time_0)
    time_1 = del_null(time_1)
    time_0 = max(time_0)/time_0
    time_1 = max(time_1)/time_1
    prof_t0 = 1/time_0
    prof_t1 = 1/time_1
    delta_prof = abs(prof_t1 - prof_t0)+0.00001 #############
    relation_prof = (delta_prof/prof_t1) * 100##########
    os.chdir('../')
    np.savetxt('delta_2_test.txt', relation_prof)
    os.system('cp delta_2_test.txt ../db')
    os.chdir('2_test/')
    os.chdir('~/main')
    #print(relation_time)
    return relation_prof

def draw_plot(data): 
    x_name= [25, 50, 100, 150, 200]
    N = np.arange(len(x_name))
    for i, n in enumerate(x_name):
        plt.bar(N[i], data[n])
    plt.xticks(N, x_name)
    plt.title('Отображение резултатов 2 теста')
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери производительности, %')
    plt.grid()
    #plt.show()
    plt.savefig("Отображение резултатов 2 теста")
    os.chdir('~/main')


if __name__=='__main__':
    main()
