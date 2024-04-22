#1번 실습
def first() :
    gender = input("male or female? (M/m/F/f) : ")
    height = float(input("your height? : "))

    male_avg_height = 173.5
    female_avg_height = 163.2

    if gender.upper() == 'M':
        if height >= male_avg_height:
            print("you are taller than the average height")
        elif height < male_avg_height:
            print("you are smaller than the average height")

    if gender.upper() == 'F':
        if height >= female_avg_height:
            print("you are taller than the average height")
        elif height < female_avg_height:
            print("you are smaller than the average height")

#2번 실습
def second() :
    integer = int(input("enter your integer number"))
    if integer % 4 == 0 and integer % 5  == 0:
        print("{} 은 4의 배수이면서 5의 배수입니다".format(integer))
    elif integer % 4 == 0:
        print("{} 은 4의 배수입니다".format(integer))
    elif integer % 5 == 0:
        print("{} 은 5의 배수입니다".format(integer))
    else :
        print("{} 은 4의 배수도 아니고 5의 배수도 아닙니다".format(integer))

#3번 실습
def third() :
    age = int(input("enter your age : "))
    height = float(input("enter your height : "))
    if age >= 10 and height >= 165.0 :
        print("you are able to ride")
    else :
        print("you are not able to ride")

#4번 실습
def forth() :
    age = int(input("enter your age : "))
    height = float(input("enter your height : "))
    if age >= 10:
        if height >= 165.0:
            print("up to 10 years old, up to 165cm, you are able to ride")
        else :
            print("you are not able to ride because you are too small")
    elif age < 10:
        if height >= 165.0:
            print("you are not able to ride. you are too young")
        else:
            print("you are not able to ride. you are too small and too young")

#5번 실습
import datetime
def fifth() :
    now = datetime.datetime.now()
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')
    hour = int(datetime.datetime.now().strftime('%H'))
    minute = datetime.datetime.now().strftime('%M')
    weekday = now.weekday()
    amPm = datetime.datetime.now().strftime('%P')

    if hour >= 12 :
        amPm = "오후"
    elif hour < 12 :
        amPm = "오전"

    hour = now.hour % 12

    if weekday == 0:
        weekdaystr = "월요일"
    if weekday == 1:
        weekdaystr = "화요일"
    if weekday == 2:
        weekdaystr = "수요일"
    if weekday == 3:
        weekdaystr = "목요일"
    if weekday == 4:
        weekdaystr = "금요일"
    if weekday == 5:
        weekdaystr = "토요일"
    if weekday == 6:
        weekdaystr = "일요일"

    print("지금은 {}년 {}월 {}일 {} {} {}시 {}분 입니다.".format(year, month, day, weekdaystr, amPm, hour, minute))



#6번 실습
def sixth() :

    python_grade = int(input("파이썬 점수를 입력하세요 : "))
    c_grade = int(input("C언어 점수를 입력하세요 : "))
    compter_grade = int(input("컴퓨터개론 점수를 입력하세요 : "))
    sum = python_grade + c_grade + compter_grade
    aver = (python_grade + c_grade + compter_grade) / 3

    print("총점 : ", sum)

    if aver >= 90 :
        grade = "A"
        print("{}학점으로 성적우수 장학생입니다.".format(grade))
    elif aver < 90 and aver >= 80 :
        grade = "B"
        print("{}학점으로 우수한 성적입니다.".format(grade))
    elif aver < 80 and aver >= 70:
        grade = "C"
        print("{}학점으로 조금 더 노력해야합니다.".format(grade))
    elif aver < 70 and aver >= 60:
        grade = "D"
        print("{}학점으로 열심히 노력해야합니다.".format(grade))
    elif aver < 60 :
        grade = "F"
        print("{}학점으로 재수강해야합니다.".format(grade))

first()
second()
third()
forth()
fifth()
sixth()