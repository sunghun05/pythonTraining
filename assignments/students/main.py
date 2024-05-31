#웹프 파이썬 알고리즘

def preprocessing():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        line = []
        for i in range(len(data)):
            # data[i].rstrip
            line.append(data[i].split())
        #print(line)
        name = []
        stu_dic = {}
        for i in range(len(line)):
            name.append([line[i][0], line[i][1]])
            stu_dic[i] = name[i]

        web = {}
        for i in range(len(line)):
            web[i] = int(line[i][2])
        
        
        python = {}
        for i in range(len(line)):
            python[i] = int(line[i][3])
        #print(python)
        
        
        algo = {}
        for i in range(len(line)):
            algo[i] = int(line[i][4])
        algo = sorted(algo.items())
        print(algo)
        
        #print(stu_dic)
        
preprocessing()