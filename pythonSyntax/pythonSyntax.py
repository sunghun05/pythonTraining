import numpy as np
# print(5)
# print(-10)
# print(3.14)
# print(5+3)
# print(6*3)
# print(3*(3+1))
# print('풍선')
# print("나비")
# print('ㅋ'*9)
# print(5>10)
# print(not True)

#변수!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >=3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + " 는 어른일까요?" + str(is_adult))


#연산자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(2**3) #2의 3승
# print(5%3) #5/3의 나머지 = 2
# print(5//3) #몫

# print(1 !=2) #true
# print(not(1 != 3)) #false

# print((3>0) and (3<5)) #true
# print((3>0) & (3<5)) #true

# print((3>0) or (3>5)) #true

# number = 14
# print(number)

# number += 2
# print(number)

# number *= 2
# print(number)

# print(abs(-5)) #절댓값

# print(pow(4, 2)) #4의 2승

# print(max(5, 12)) #둘중에 최댓값 = 12
# print(min(12 , 5)) #최솟값

# print(round(3.14)) #반올림

# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근


#from random import *
# print(random())
# print(random() * 10)
# print(int(random() * 10)) #1부터 10 미만
# print(int(random() * 10)+1) # 1부터 10 이하

# print(int(random() * 45)+ 1)#1부터 45이하
# print(randrange(1, 45)) #1~45 미만

#print(randint(1, 45)) #1~ 45 이하

# sentence3 = """
# 파이썬은
# 쉬워요
# """
# print(sentence3)

#슬라이싱!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# jumin = "990120-1234567"

# print("성별: " + jumin[7])
# print("YEAR: " + jumin[0:2])
# print("MONTH: " + jumin[2:4])
# print("DATE: " + jumin[4:6])

# print("BIRTHDAY: " + jumin[:6]) # = print("BIRTHDAY: " + jumin[0:6])
# print("뒤 7자리: " + jumin[7:]) # = print("뒤 7자리: " + jumin[7:14])
# print("뒤 7 자리(뒤에서부터): " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) #소문자
# print(python.upper()) #대문자
# print(python[0].isupper()) #소문자인지 대문자인지
# print(len(python)) #길이
# print(python.replace("Python", "java")) #대문자 주의

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("java")) #없어서 -1 반환
# # print(python.index("java")) #error
# print(python.count("n")) #몇번째인지

# print("나는 %d살입니다." % 20)
# print("나는 %s를 좋아해요." % "PYTHON")
# print("Apple 은 %c로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# #탈출문!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print("백문이 불어일견 \n백견이 불여일타")

# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다")
# print('저는 \'나도코딩\' 입니다')

# \\ : 문장내에서 하나의 역슬러시로 바뀜
#\를 출력할때
# print("C:\\Users\\sungh\\OneDrive\\바탕 화면\\PythonWorkSpace")

# # \r : 커서를 맨 앞으로 이동
# print("Red apple\rPine")

# # \b: backspace
# print("Redd\bApple")

# # \t : tab
# print("Red\tApple")


# adress = "http://naver.com"
# nameOfSite1 = adress[7:12]
# nameOfSite2 = adress[7:10]
# length = len(nameOfSite1)
# print(f"{nameOfSite2}{length}!")


#리스트!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#지하철 칸별로 10, 20, 30명이 있음
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호는 몇번째 칸에 타고있는가?
# print(subway.index("조세호")+1)

# #다음 정류장에서 다음칸에 하하가 탐. append = 값을 더함
# subway.append("하하")
# print(subway)

# #정형돈을 유재석과 조세호 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 잇는 사람을 꺼냄
# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# num_list = [5, 4, 3, 2, 1]
# num_list.sort() #순서대로 정렬
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# #지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 사용
# num_list = [5, 4, 3, 2, 1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#사전!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# cabinet = {3:"유재석", 100:"김태호"} #정수형
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# print(cabinet[5]) 오류

# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) #true

# cabinet = {"A-3":"유재석", "A-4":"김태호"} #문자형
# print(cabinet["A-3"])
# print(cabinet["A-4"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#튜플 : 리스트와 다름. 리스트보다 빠르고 변경불가.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# #menu.add("생선까스")   (추가불가)

# name = "김종국"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "coding")
# print(name, age, hobby)

#집합 (set)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#중복, 순서 없음

# my_set = {1, 2, 3, 3, 4}
# print(my_set)

# java = {"유재석", "김태호", "조세호"}
# python = set(["유재석", "박명수"])

# #교집합
# #java와 python 개발자

# print(java & python)
# print(java.intersection(python)) #교집합. 위에문장이랑 결과 같음

# #합집합
# #java or python 개발자

# print(java | python)
# print(java.union(python))#합집합

# #차집합
# #java는 할수 있지만 python 은 못함
# print(java - python)
# print(java.difference(python))

# #add
# python.add("김태호")
# print(python)

# #java를 잊었어요
# java.remove("김태호")
# print(java)

#자료구조의 변경 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

# from random import *
#lst = range(1, 21)
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(lst)
# print(sample(lst, 1))
# print(sample(lst, 3))

#if!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# weather = input("오늘 날씨는 어때요?\n")
# if weather == '비' or weather == '눈':
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print('마스크를 챙기세요')
# else:
#     print("준비물이 필요 없어요")

# temp = int(input("기온이 어때요?\n"))
# if temp >= 30:
#     print("너무 더워요, 나가지 마세요")
# elif temp > 10 and temp < 30:
#     print("나가셔도 좋아요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요")

#for !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(1, 6): #1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

#while !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# customer = '토르'
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다, {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. {1}번 호출".format(customer, index))
# ^^^^^^^^^ 무한 루프 (끝내려면 ctrl + c)

# customer = "토르"
# person = "unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?\n")

#continue !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘수업 여기까지. {0}은 교무실로 따라와".format(no_book))
#         break
#     print("{0}번학생, 책을 읽어보세요".format(student))

#출석번호 앞에 100을 붙히지로함
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students = ["iron man", "thor", "groot"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
# students = ["iron man", "thor", "groot"]
# students = [i.upper() for i in students]
# print(students)

# from random import *
# cnt = 0 #총 탑승 승객 수
# for i in range(1, 51): # 승객
#     time = randrange(5, 51) #5~50분 사이의 소요시간 정보
#     if 5 <= time <=15:
#         print("[O] {0}번째 손님, 소요시간 {1}분".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님, 소요시간 {1}분".format(i, time))

# print("승객 : {0}분".format(cnt))

# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}입니다.".format(balance))
#         return balance - money
#     elif balance < money:
#         print("잔액이 모자랍니다. 잔액은 {0}입니다.".format(balance))
#         return balance

# balance = 0
# balance = deposit(balance, 1000)

# withdraw(balance, 5000)

#기본값 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def profile(name, age, main_lang):
#     print("이름 : {0}\n 나이 : {1}\n 주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 40, "자바")
# profile("김태호", 44, "파이썬")

#같은 학년 같은 반 같은 언어

# def profile(name, age=17, main_lang="자바"):
#      print("이름 : {0}\n 나이 : {1}\n 주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

#키워드값!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(age=20, name="유재석", main_lang="자바")

#가변인자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}, 나이: {1}".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0}, 나이: {1}".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "Python", "java", "C", "HTML", "Javascript", "swift")
# profile("김태호", 30, "python", "swift")

#지역변수, 전역변수!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!











