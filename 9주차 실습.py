#실습과제 1

# def enterInt(data):
#     li.append(data)
#     print(li, end="")
#     print("avg = ", sum(li) / len(li))
# def removeLa():
#     del li[len(li)-1]
#     print(li, end="")
#     print("avg = ", sum(li)/len(li))
# def menu():
#     set = input("명령어를 입력하세요 : ")
#     if set == "삽입":
#         enterInt(int(input("데이터를 입력하세요 : ")))
#         menu()
#     elif set == "삭제":
#         removeLa()
#         menu()
#     else:
#         print("명령어 오류")
#         menu()
# li = []
# menu()


#실습 문제 2
# sc = []
# a=0
# for i in range(5):
#     sc.append(int(input("성적을 입력하세요 : ")))
# av = sum(sc) / len(sc)
# ma = max(sc)
# mi = min(sc)
# for i in range(len(sc)):
#     if sc[i] >= 90:
#         a += 1
# print(sc)
# print("평균 : {}".format(av))
# print("최고 점수 : {}".format(ma))
# print("최저 점수 : {}".format(mi))
# print("90 점 이상 학생 {}명".format(a))

#실습문제 3
# row = []
# data = []
def score():
    global row
    global data
    for i in range(2):
        data.append(input("학번 : "))
        data.append(input("이름 : "))
        data.append(int(input("국어 : ")))
        data.append(int(input("영어 : ")))
        data.append(int(input("수학 : ")))
        data.append(data[2]+data[3]+data[4])
        row.append(data)
        data = []
        print("======================")
        print(row)
    sort()
def sort():
    global row
    global data
    print("====이름순 정렬 ====")
    row.sort(key=lambda row : row[1])
    for i in range(len(row)):
        print(row[i])
    print("====성적순 정렬 ====")
    row.sort(key=lambda row : row[5], reverse=True)
    for i in range(len(row)):
        print(row[i])
# score()

#실습문제 4
def summ():
    a = []
    b = []
    for i in range(3):
        for j in range(3):
            b.append(int(input("데이터를 입력하세요 : ")))
        a.append(b)
        b=[]
    print(a)
    print(a[0])
    for i in range(len(a)+3, 2):

        c = [sum(a[i])]
        print(c)
        a.insert(i+1, c)
    print(a)
summ()