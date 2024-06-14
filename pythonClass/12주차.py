import os
class box():
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.size = width*length*height

    def __str__(self):
        _say = "상자의 부피는 : " + str(self.size)
        return _say

# aBox = box(100, 100, 100)
# print(aBox)

class cir():
    def __init__(self, rad):
        self.__radius = rad
        self.__area = self.__radius * self.__radius * 3.14
    def getRadius(self):
        return self.__radius
    def getArea(self):
        return self.__area
    def setRadius(self, rad):
        self.__radius = rad
        self.__area = self.__radius * self.__radius * 3.14

# aCir = cir(100)
# print(aCir.getArea())
# aCir.setRadius(2)
# print(aCir.getRadius())
# print(aCir.getArea())

class bank:

    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액이 부족합니다.")
        else :
            if input("거래 전 잔액 : {} --> 거래 후 잔액 : {}\n거래 하시겠습니까? (y/n) ".format(self.__balance, self.__balance-amount)).lower() == "y":
                self.__balance -= amount
                print("잔액 : ", self.__balance)

    def deposit(self, amount):
        if input("거래 전 잔액 : {} --> 거래 후 잔액 : {}\n거래 하시겠습니까? (y/n) ".format(self.__balance, self.__balance+amount)).lower() == "y":
            self.__balance += amount
            print("잔액 : ", self.__balance)
    def __str__(self):
        say = "현재 잔액 : "+str(self.__balance)
        return say

# k = bank()
# k.withdraw(10000)
#
# k.deposit(10000)
# k.withdraw(10000)
# print(k)

class dog :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        say = "이름 : " + str(self.name) + "\n나이 : " + str(self.age)
        return say

# miky = dog("Miky", 3)
# amy = dog("Amy", 4)
# print(miky)
# print(amy)

class Car:
    __dirty = 0
    __isOn = False
    def __init__(self, make : str, year : str, color : str):
        self.make = make
        self.year = year
        self.color = color
        self.__speed = 0
        self.__lev = 0
        self.__fuel = 100
    def __str__(self):
        say = ("make : "+str(self.make)+"\nyear : "+str(self.year)+"\ncolor : "+str(self.color)
               +"\nnow speed : "+str(self.__speed)+"\nlevel : "+str(self.__lev)+"\nfuel : "+str(self.__fuel))
        return say
    def start(self):
        if self.__isOn == False:
            self.__isOn = True
            print("car is started. fuel is: "+str(self.__fuel))
        else :
            print("car is elrady running")
    def finish(self):
        if self.__isOn == True :
            self.__isOn = False
            print("car is finished. fuel is: "+str(self))
        else :
            print("start car first")
    def spUp(self, amount):
        if self.__fuel <= 0:
            print("연료가 부족합니다.")
        elif self.__isOn == False :
            print("시동을 켜세요.")
        else :
            self.__speed += amount
            if self.__speed <= 0 :
                print("정지")
                self.__lev = 0
                self.__speed = 0
            if self.__speed >= 20 :
                self.__lev = 2
            if self.__speed >= 40 :
                self.__lev = 3
            if self.__speed >= 60 :
                self.__lev = 4
            if self.__speed >= 80 :
                self.__lev = 5
            print("now speed : {}, now level : {}".format(str(self.__speed), str(self.__lev)))
            self.__dirty += 10
            self.__fuel -= 20


    def spDown(self, amount):
        if self.__isOn == False :
            print("시동을 켜세요.")
        else :
            self.__speed -= amount
            if self.__speed <= 0 :
                print("정지")
                self.__lev = 0
                self.__speed = 0
            if self.__speed >= 20 :
                self.__lev = 2
            if self.__speed >= 40 :
                self.__lev = 3
            if self.__speed >= 60 :
                self.__lev = 4
            if self.__speed >= 80:
                self.__lev = 5
            print("now speed : {}, now level : {}".format(str(self.__speed), str(self.__lev)))

    def clean(self):
        self.__dirty = 0
        print("clean complete")

    def putFuel(self, amount):
        if self.__isOn == True :
            print("시동을 끄세요")
        else :
            self.__fuel += amount
            print("now fuel : {}".format(self.__fuel))

a = Car("kia", "2023", "red")
# a.putFuel(20)
a.start()
a.spUp(50)
a.spUp(50)
a.spDown(50)
a.spDown(150)
a.spUp(200)
a.spDown(100)
a.spDown(200)
# print(a)

a = {1,2,3}
print(type(a))
print(a)

