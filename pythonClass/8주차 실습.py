"""definition"""
import math


def twoNum(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return "n1 = n2"
# print(twoNum(int(input("1:")), int(input("2:"))))


"""global"""
def area(radius):
    global pi
    a = pi * radius**2
    return a
pi = 3.14
# print(area(float(input("반지름 값: "))))

"""default argument"""

def sum1(start, end, step=1):
    for i in range(start, end+1, step):
        start += step
    return start
# print(sum1(int(input("start: ")), int(input("end: ")), int(input("step: "))))

"""important :::: 인수와 매개변수의 차이, 어떻게 전달. 전역변수 사용법"""

"""실습"""

#실습1
def trans(inc, mi):
    return inc*2.54, mi * 1.61

# inch = float(input("인치를 입력: "))
# mile =  float(input("마일을 입력: "))
# a = trans(inch, mile)
# print("{}인치 = {}센티미터".format(inch, a[0]))
# print("{}마일 = {}킬로미터".format(mile, a[1]))

#실습 2

def isCr(x1, y1, x2, y2, r1, r2):
    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if dis > r1+r2:
        print("점 ({},{})와 점 ({},{}) 사이의 거리 : {}\n 두 원 서로 떨어져 있습니다.".format(x1, y1, x2, y2, dis))
    elif dis <= r1+r2:
        print("점 ({},{})와 점 ({},{}) 사이의 거리 : {}\n 두 원 서로 충돌하였습니다.".format(x1, y1, x2, y2, dis))
# isCr(int(input("첫번째 원 중점의 x 좌표")), int(input("첫번째 원 중점의 y 좌표")), int(input("두번째 원 중점의 x 좌표")), int(input("번째 원 중점의 y 좌표")), int(input("첫번째 원의 반지름")), int(input("두번째 원의 반지름")))

#실습 3


def numTok(num):
    c = []
    c1 = [" ", "십", "백", "천", "만", "십만", "백만", "천만", "억"]
    c2 = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    for i in range(1, len(str(num))+1):
        c.append(str(num % 10**i)[0]+":"+c2[int(str(num % 10**i)[0])-1]+c1[i-1])
        print(c[i-1])

# num1 = int(input("금액을 숫자로 입력: "))
# numTok(num1)

#실습 4
def find_prime(n):
    a = []

    for i in range(2, n+1):
        b = True
        for j in range(2, i):
            if i % j == 0:
                b = False
            # else: break
        if b == True:
            a.append(i)
    return a


# print(find_prime(int(input("1부터 어느 범위까지의 소수를 찾고 싶으신가요? : "))))

#실습 5

def cal(nums):
    num = nums.split(" ")
    for i in range(len(num)):
        num[i] = int(num[i])
    s = sum(num)
    av = s/len(num)
    max = 0

    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    min = max
    for i in range(len(num)):
        if num[i] < min:
            min = num[i]
    print("평균 : {:.2f} \n최대 : {} \n최소 : {}".format(av, max,min))

# cal(input("숫자를 입력하세요 (공백으로 구분) : "))

#실습 6

def read_data(pyth_list, data_list, comp_list):
    pyth_list.append(input("파이썬 점수 : "))
    data_list.append(input("자료구조 점수 : "))
    comp_list.append(input("컴퓨터개론 점수 : "))
def compute_data(pyth_list, data_list, comp_list, tot_list, score_list, st_num):
    for i in range(st_num):
        tot = int(pyth_list[i]) + int(data_list[i]) + int(comp_list[i])
        tot_list.append(tot)
        avg = tot / 3
        score_list.append(decide_score(avg))
def print_data(pyth_list, data_list, comp_list, tot_list, score_list, st_num):
    print("번호  파이썬  자료구조  컴퓨터개론  총점  학점")
    print("=====================================")
    for i in range(st_num):
        print("%4s %6s %8s %10s %4s %4s" % (i+1, pyth_list[i], data_list[i], comp_list[i], tot_list[i], score_list[i]))
    print("____________________________________")
def decide_score(avg_score):
    if avg_score >= 90:
        return 'A'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 60:
        return 'D'
    else:
        return 'F'

# pyth_list = []
# data_list = []
# comp_list = []
# tot_list = []
# score_list = []
# st_num = 5

# for i in range(st_num):
#     print("===%d번 학생 점수 입력===" % (i+1))
#     read_data(pyth_list, data_list, comp_list)
# compute_data(pyth_list, data_list, comp_list, tot_list, score_list, st_num)
# print_data(pyth_list, data_list, comp_list, tot_list, score_list, st_num)

