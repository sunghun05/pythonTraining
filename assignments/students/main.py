def preprocessing():
    global stu_dic
    global sum_dic
    with open('data.txt', 'r') as f:
        data = f.readlines()
        line = []
        for i in range(len(data)):
            line.append(data[i].split())
        # print(line)
        stu_dic = {}
        for i in range(len(line)):
            line[i][2] = int(line[i][2])
            line[i][3] = int(line[i][3])
            line[i][4] = int(line[i][4])
            stu_dic[line[i][0]] = line[i]
            sum_dic[line[i][0]] = line[i]
            #del (stu_dic[line[i][0]][0])
            #print(sum_dic)
            # print(line[i])
            # sum_dic[line[i][0]] = sum(line[i][2:])
            stu_dic[line[i][0]] = line[i][1:]
            stu_dic[line[i][0]].append(sum(line[i][2:]))
            stu_dic[line[i][0]].append(round(stu_dic[line[i][0]][4]/3))

            #print(sum_dic[line[i][0]])
        # print(sum_dic)
        #print(stu_dic)
        #print(dict(sorted(stu_dic.items(), key=lambda x: x[1][4], reverse=True)))

    a = open('A.txt', 'w')
    b = open('B.txt', 'w')
    c = open('C.txt', 'w')
    d = open('D.txt', 'w')
    asc = open('asc.txt', 'w')
    desc = open('desc.txt', 'w')
    n20 = open('2020.txt', 'w')     #2020학번 파일 ==> n20
    n21 = open('2021.txt', 'w')
    n22 = open('2022.txt', 'w')
    n23 = open('2023.txt', 'w')
    n24 = open('2024.txt', 'w')

    a.write('')         #파일의 내용 지우기
    b.write('')
    c.write('')
    d.write('')
    asc.write('')
    desc.write('')
    n20.write('')
    n20.write('number       name   sum aver\n')
    n21.write('')
    n21.write('number       name   sum aver\n')
    n22.write('')
    n22.write('number       name   sum aver\n')
    n23.write('')
    n23.write('number       name   sum aver\n')
    n24.write('')
    n24.write('number       name   sum aver\n')

    for i in range(len(line)):
        if stu_dic[line[i][0]][5] >= 80:
            a.write(line[i][0]+ " \t"+str(stu_dic[line[i][0]][0])+'\t평균 : '+str(stu_dic[line[i][0]][5])+'\n')
        elif stu_dic[line[i][0]][5] < 80 and stu_dic[line[i][0]][5] >= 70:
            b.write(line[i][0]+ " \t"+str(stu_dic[line[i][0]][0])+'\t평균 : '+str(stu_dic[line[i][0]][5])+'\n')
        elif stu_dic[line[i][0]][5] < 70 and stu_dic[line[i][0]][5] >= 60:
            c.write(line[i][0]+ " \t"+str(stu_dic[line[i][0]][0])+'\t평균 : '+str(stu_dic[line[i][0]][5])+'\n')
        elif stu_dic[line[i][0]][5] < 60:
            d.write(line[i][0]+ " \t"+str(stu_dic[line[i][0]][0])+'\t평균 : '+str(stu_dic[line[i][0]][5])+'\n')
    # print(stu_dic)
    ascd = list(sorted(stu_dic.items(), key=lambda x: x[1][4], reverse=False))
    descd = list(sorted(stu_dic.items(), key=lambda x: x[1][4], reverse=True))
    # print(ascd)
    # print(descd)
    for j in range(len(line)):
        asc.write(str(ascd[j][1][0])+'\t평균 : '+str(ascd[j][1][5])+'\t총점 : '+str(ascd[j][1][4])+'\n')
        desc.write(str(descd[j][1][0])+'\t평균 : '+str(descd[j][1][5])+'\t총점 : '+str(descd[j][1][4])+'\n')

    for i in range(len(line)):
        # print(list(stu_dic.keys())[i][:4])
        if list(stu_dic.keys())[i][:4] == '2020':
            n20.write(str(list(stu_dic.keys())[i])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][0])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][4])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][5])+'\n')
        elif list(stu_dic.keys())[i][:4] == '2021':
            n21.write(str(list(stu_dic.keys())[i])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][0])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][4])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][5])+'\n')
        elif list(stu_dic.keys())[i][:4] == '2022':
            n22.write(str(list(stu_dic.keys())[i])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][0])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][4])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][5])+'\n')
        elif list(stu_dic.keys())[i][:4] == '2023':
            n23.write(str(list(stu_dic.keys())[i])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][0])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][4])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][5])+'\n')
        elif list(stu_dic.keys())[i][:4] == '2024':
            n24.write(str(list(stu_dic.keys())[i])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][0])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][4])+'\t'+str(stu_dic[list(stu_dic.keys())[i]][5])+'\n')
        # print(stu_dic)

    n20 = open('2020.txt','r+')
    n0s = []
    n21 = open('2021.txt','r+')
    n1s = []
    n22 = open('2022.txt','r+')
    n2s = []
    n23 = open('2023.txt','r+')
    n3s = []
    n24 = open('2024.txt','r+')
    n4s = []

    n20.readline()
    n21.readline()
    n22.readline()
    n23.readline()
    n24.readline()
    n0l = n20.readlines()
    n1l = n21.readlines()
    n2l = n22.readlines()
    n3l = n23.readlines()
    n4l = n24.readlines()

    for i in range(len(n0l)):
        n0l[i] = n0l[i].rstrip('\n')
        n0l[i] = n0l[i].split('\t')
        n1l[i] = n1l[i].rstrip('\n')
        n1l[i] = n1l[i].split('\t')
        n2l[i] = n2l[i].rstrip('\n')
        n2l[i] = n2l[i].split('\t')
        n3l[i] = n3l[i].rstrip('\n')
        n3l[i] = n3l[i].split('\t')
        n4l[i] = n4l[i].rstrip('\n')
        n4l[i] = n4l[i].split('\t')
    for j in range(len(n0l)):
        n0s.append(n0l[j][2])
        n1s.append(n1l[j][2])
        n2s.append(n2l[j][2])
        n3s.append(n3l[j][2])
        n4s.append(n4l[j][2])
    #print(n0s)
    n0Max = max(n0s)
    n0Min = min(n0s)
    # print(n0Min)
    n1Max = max(n1s)
    n1Min = min(n1s)
    n2Max = max(n2s)
    n2Min = min(n2s)
    n3Max = max(n3s)
    n3Min = min(n3s)
    n4Max = max(n4s)
    n4Min = min(n4s)

    n20.write('\n=======1등======\n')
    n21.write('\n=======1등======\n')
    n22.write('\n=======1등======\n')
    n23.write('\n=======1등======\n')
    n24.write('\n=======1등======\n')

    for i in range(len(n0l)):
        if n0Max == n0l[i][2]:
            n20.write(str(n0l[i])+'\n')
        if n1Max == n1l[i][2]:
            n21.write(str(n1l[i])+'\n')
        if n2Max == n2l[i][2]:
            n22.write(str(n2l[i])+'\n')
        if n3Max == n3l[i][2]:
            n23.write(str(n3l[i])+'\n')
        if n4Max == n4l[i][2]:
            n24.write(str(n4l[i])+'\n')
    n20.write('\n======꼴등======\n')
    n21.write('\n======꼴등======\n')
    n22.write('\n======꼴등======\n')
    n23.write('\n======꼴등======\n')
    n24.write('\n======꼴등======\n')
    # print(stu_dic)
    for j in range(len(n0l)):
        if n0Min == n0l[j][2]:
            n20.write(str(n0l[j])+'\n')
        if n1Min == n1l[j][2]:
            n21.write(str(n1l[j])+'\n')
        if n2Min == n2l[j][2]:
            n22.write(str(n2l[j])+'\n')
        if n3Min == n3l[j][2]:
            n23.write(str(n3l[j])+'\n')
        if n4Min == n4l[j][2]:
            n24.write(str(n4l[j])+'\n')
    a.close()
    b.close()
    c.close()
    d.close()
    asc.close()
    desc.close()
    n20.close()
    n21.close()
    n22.close()
    n23.close()
    n24.close()

def search() :
    global stu_dic
    res = []
    stu_li = list(stu_dic.items())
    #print(stu_li)
    while(1):
        res = []
        ser = input('학번을 입력하세요 : ')
        if len(ser) == 8:
            for i in range(len(stu_li)):
                if stu_li[i][0] == ser:
                    res.append(stu_li[i][1])

            if res == []:
                print('결과가 없습니다.')
            else :
                print('name     web programming     python      algorithm    sum        average')
                for i in range(len(res)):
                    print('{}                 {}         {}             {}     {}            {}'.format(res[i][0], res[i][1], res[i][2], res[i][3], res[i][4], res[i][5]))
        elif ser == '-1':
            print('종료합니다.')
            break
        else :
            print("올바른 학번을 입력하세요")


if __name__ == '__main__':
    stu_dic = {}
    sum_dic = {}
    preprocessing()

    search()
