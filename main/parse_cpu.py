import os
def main():
    os.system('lscpu > lscpuf')
    f = 'lscpuf'
    with open(f, 'r') as f:
        lis = list()
        for line in f:
            l = line.split(':')[1]
            lis.append(l)
    res = {'Arch':lis[0], 'cpus':lis[3], 'threads per core': lis[5], 
           'cpu MHz': lis[14], 'cpu max MHz':lis[15], 'cpu min MHz':lis[16],
           'Virt VT-X':lis[18], 'L1d cashe':lis[19], 'L1i cashe':lis[20],
           'L2 cashe':lis[21], 'L3 cashe':lis[22]}
    
    f = open('db/cpuinfo.txt', 'w')
    f.write(str(res))
    os.system('rm lscpuf')
if __name__ == '__main__':
    main()
