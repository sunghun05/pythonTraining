import math
#실습문제 1
PI = 3.141592653589793

radius = float(input("please input the radius of the circle: "))
volumn = (4/3)*PI*radius**3
print("The volume of the circle is ", volumn)

#실습문제 2
_x = int(input("x의 값을 입력하세요"))
_f = 2 * _x ** 3 + 3 * _x ** 2 + 7 * _x + 10
print(_f)

#실습문제 3
year = int(input("예금 경과 년수를 입력하세요 : "))
ir = float(input("예금 금리를 입력하세요 : "))
op = float(input("예금 원금을 입력하세요 : "))
total = op * (1 + ir / 100) ** float(year)

#실습문제 4
money = int(input("지폐로 교환할 돈을 입력하세요 : "))
yellowMoney = money // 50000
money %= 50000
greenMoney = money // 10000
money %= 10000
orangeMoney = money // 5000
money %= 5000
blueMoney = money // 1000
money %= 1000
remainMoney = money
print(yellowMoney)
print(greenMoney)
print(orangeMoney)
print(blueMoney)
print(remainMoney)

#실습문제 5
_x = float(input("x값을 입력하시오: "))
_y = float(input("y값을 입력하시오: "))
_z = float(input("z값을 입력하시오: "))
first = 2 * _x ** 3 + 3 * _x ** 2 * _y ** 2 + 7 * _x * _z ** 3 - 5 * _y
second = (_x + _y) / (_x * _y * 2)
print(first)
print(second)

#실습문제 6
_x1 = float(input("x1좌표 :"))
_y1 = float(input("y1좌표 :"))
_x2 = float(input("x2좌표 :"))
_y2 = float(input("y2좌표 :"))
length = ((_x2 - _x1)**2 + (_y2 - _y1)**2)**(1/2)
#length = math.sqrt(length)
print(length)

#실습문제 7
x = int(input("x: "))
y = int(input("y: "))
print("x: ", bin(x))
print("y: ", bin(y))

result_and = x & y
result_or = x | y
result_xor = x ^ y

print("&: ", bin(result_and), "=>", result_and)
print("|: ", bin(result_or), "=>", result_or)
print("^: ", bin(result_xor), "=>", result_xor)