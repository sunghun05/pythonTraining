#1
pi = 3.14
radius = float(input("원의 반지름을 입력하세요:"))
round = 2 * radius * pi
area = pi * radius * radius
print("반지름: {0:.1f} 둘레: {1:.1f} 넓이: {2:.1f}".format(radius, round, area))

#2
first = float(input("첫번째 숫자를 입력하세요"))
second = float(input("두번째 숫자를 입력하세요"))
print(first + second)
print(first - second)
print(first * second)
print(first / second)

#3
name = input("이름을 입력하세요:")
print("{0:s}님 파이썬 수업 수강을 환영합니다".format(name))
thisYear = int(input("올해의 년도를 입력하세요:"))
bornYear = int(input("태어난 연도를 입력하세요"))
print("{0:s}님은 한국 나이로 {1:d}이시군요".format(name, thisYear-bornYear))

#4
integer = int(input("정수를 입력하세요:"))
print("integer: {0:d}\n실수: {1:f}\n문자열: {2:s}\n2진수: {3:b}\n8진수: {4:o}\n16진수: {5:x},{6:X}".format(integer, float(integer), str(integer), integer, integer, integer, integer))

#5
year = 2022
month = 3
day = 15
day_week = '화'
temp = 15.3

print("{}년 {}월 {}일 은 {}요일 입니다".format())
print("한국식 표현 (년/월/일/요일): {}/{}/{}/{}".format())
print("미국식 표현 (요일/월/일/년): {}/{}/{}/{}".format())
print("영국식 표현 (요일/일/월/년): {}/{}/{}/{}".format())

print("{y}년 {m}월 {d}은 {dw}요일 입니다.".format(m=month, d=day, dw=day_week))
print("{0:02d}월 {1}은 {2}요일은 온도가 {3:.2f}도 입니다.".format(month, day, day_week, temp))

#6
num = 12345
print("출력 연습 0000000000")
print("좌측정렬:{0<10}".format(num))
print("중앙정렬:{0^10}".format(num))
print("우측정렬:{0>10}".format(num))

