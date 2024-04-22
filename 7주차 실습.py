#실습문제 1
def func(num):
    a = []
    for i in range(1,num+1):
        if (i % 2 == 1):
            a.append(i)
    return sum(a)

# n = int(input("enter a number"))
# print(func(n))

#실습문제 2
def func2(c):
    name = []
    for i in range(c):
        name.append(input("장군의 이름을 입력하세요"))
    for j in range(len(name)):
        print("{}: {} 장군님 반갑습니다!".format(j+1, name[j]))
# func2(int(input("몇명의 장군을 입력하시겠습니까? : ")))

#실습문제 3
def func3():
    print("======================================================구구단 출력=====================================================")
    for i in range(2, 10):
        print(" {} 단 ".format(i))
        for j in range(1, 10):
            print("{} * {} = {}".format(i, j, (i)*j))
        print("")

#실습문제 4

def func4(a, w):
    if a % 2 == 0:
        print("enter odd numbers")
        func4(int(input("enter your number : ")),input("enter your character : "))
    else:
        for i in range(1,a,2):
            print(" "*((a-i)//2), end="")
            print("{}". format(w)*i)
        for j in range(a,0, -2):
            print(" " * ((a - j) // 2), end="")
            print("{}". format(w)*j)
# func4(int(input("enter your number : ")), input("enter your character : "))

#실습문제 5
def fac(a):
    k = 1
    for i in range(a):
        k *= (i+1)
    print("{}! = {}".format(a, k))
# fac(int(input("enter your number : ")))

#실습문제 6
import random

def func6():
    num = random.randrange(1, 100)
    tr = 0
    while tr <= 10:
        an = int(input("숫자를 맞춰보시오 (1~100) : "))
        tr += 1
        if an < num:
            print("Up")
        elif an > num:
            print("Down")
        elif an == num:
            print("정답")
            print("{} 번 시도로 맞췄습니다.".format(tr))
            break
    print("10번 시도했습니다. 정답은 {} 입니다".format(num))
#func6()

#실습문제 7
def func7():
    import random
    score = 0
    while True:
        room = random.randint(1, 3)
        n = int(input("room number"))

        if room == n :
            print("범인검거")
            score += 100
            break
        elif n > 3:
            print("{} 에는 존재하지 않습니다".format(n))
            score -= 10
        else:
            print("{} 에는 범인이 없습니다".format(n))
            score -= 10
    print("게임종류 점수 {}점".format(score))
# func7()

#실습문제 8
def func8():
    num = int(input("자연수를 입력하세요 : "))

    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")

# func8()

def find_prime(n):
    a = []
    i = 2
    while True:
        if n % i == 0 :
            n = n//i
            a.append(i)
            print(i)
            i = 2
        elif n % i != 0:
            if n // i == 0:
                break
            else:
                i += 1

    # print(a)

find_prime(int(input("값을 입력하세요 : ")))