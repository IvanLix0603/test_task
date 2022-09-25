import numpy as np 
import matplotlib.pyplot as plt
import os
from poly import PolyPredict 

def preprocess_data():
    files = []
    os.chdir("1_test")########3
    time = []
    var = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' in file:
                time.append(file)
            if 'var' in file:
                var.append(file)
    return sort_data(time), sort_data(var)

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
    time, var = preprocess_data()    
    for files in zip(time, var):
        #print(files)
        data = exctract_data(files)
        lin_data = linear(data)
        calc_time = calculation_time(data[0], lin_data)
        result_data.append([calc_time, data[2]])         
    os.chdir('../')#####
    draw_plot(result_data)
    pass 


def exctract_data(files):
    time = np.loadtxt(os.path.abspath(files[0]))
    means = np.loadtxt(os.path.abspath(files[1]))
    maxi = parser_name_files(files[0]) 
    data = (time, means, maxi)
    return data

def parser_name_files(file): 
    number = file.split('_')[1] 
    return int(number)


def linear(data):
    x = data[1]
    y = data[0]
    model = PolyPredict(x, y)
    pred = model.predict()
    return abs(pred)

def calculation_time(fact_time, expect_time):    
    #print(expect_time)
    fact_time = max(fact_time)/fact_time
    expect_time = max(expect_time)/expect_time  
    prof_fact = 1/fact_time
    prof_expect = 1/expect_time
    delta_prof = abs(prof_fact - prof_expect) #############
    relation_prof = (delta_prof/prof_expect) * 100##########
    os.chdir('../')
    np.savetxt('delta_1_test.txt', relation_prof)
    os.system('cp delta_1_test.txt ../db')
    os.chdir('1_test/')
    #delta_time = abs(fact_time - expect_time) #############
    #relation_prof = ((delta_time/expect_time)) * 100##########
    #print(relation_time)
    return relation_prof

def draw_plot(data):
    #print(data[0][0][0])
    x_name= (25, 50, 100, 150, 200, 300,500, 1000, 1200)
    n_rows = len(data)
    N = np.arange(len(x_name))
    for row in range(n_rows):
        plt.bar(N[row], data[row][0])
    plt.title('Отображение результатов 1 теста')
    plt.xticks(N, x_name)
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери производительности, %')
    plt.grid()
    #plt.show()
    plt.savefig('Отображение результатов 1 теста')
    os.chdir('~/main')


if __name__=='__main__':
    main()
