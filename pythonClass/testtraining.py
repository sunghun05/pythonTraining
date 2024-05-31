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

# find_prime(int(input("값을 입력하세요 : ")))

print("%d %x %o" %(100, 100, 100))

print("%d / %d = %1.1f" %(100, 80, 100/80))

print("\t hello")
print("\b hello")

print("rmfwk\"rkld\"dkls")
print("//")
print(r"\n \t \ \\djlfk;a")

print(0b010100101010101010101010)
print(int('0100101011001010101010101010',2))
print(int('010101001010101010101010101010',2))
print(0x100101001010010)
print(bin(23))  #2진
print(oct(23))  #8진
print(hex(23))  #16진

a = 0b0010 << 2
print(a)

# 비트 논리곱 & (곱)
#비트 논리합 | ( 합 )
#비트 배타적 논리합 ^ (xor)
#비트 부정 ~ (not)

#복소수 class 'complex'
#복소수 허수 부분 j 로 표현

s = "hello python"
print(s[0:7])

import time
now = time.time()
thisYear = int(1970 + now//(365*24*60*60))
print(thisYear)

data = [1,2,3,4,5,6,7,8,9]
print(data * 2)

import random
for i in range(1, 11):
    b = random.randrange(0, 1000)
    print(b)

bool = random.choice([True, False])
print(bool)

num = 1234512345
print("{0:=^100}".format(num))