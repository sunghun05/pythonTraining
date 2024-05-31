#1번째 실습
#real : 실수
#imag : 허수
# print("첫번째 실습문제")
#
# complex_num1 = 2.7 + 3.2j
# complex_num2 = 5.1 - 2.6j
#
# addition = complex_num1 + complex_num2
# subtraction = complex_num1 - complex_num2
# multiplication = complex_num1 * complex_num2
#
# print("addition = {:.2f}".format(addition))
# print("subtraction = {:.2f}".format(subtraction))
# print("multiplication = {:.2f}".format(multiplication))
#
# print("2.7 + 3.2i 의 실수부분 {}".format(addition.real))
# print("2.7 + 3.2i 의 허수부분 {}".format(addition.imag))
# print("5.1 - 2.6i 의 켤레복소수 {:.2f}".format(subtraction.conjugate()))
# print("5.1 - 2.6i 의 크기 {:.2f}".format(abs(subtraction)))
#
# #2번째 실습
# print("두번째 실습문제")
#
import datetime
#
#
# today = datetime.date.today()
# print("오늘은 {0}년 {1:02d}월 {2:02d}일 입니다".format(today.year, today.month, today.day))
# d_day = today + datetime.timedelta(days=100)
# print("100일 후는 {0}년 {1:02d}월 {2:02d}일 입니다".format(d_day.year, d_day.month, d_day.day))
#
# now = datetime.datetime.now()
#
# print(now)
#
# print("오늘은 {}년 {}월 {}일 입니다.".format(now.year, now.month, now.day))
# print("현재 시간은 {}시 {}분 입니다.".format(now.hour, now.minute))
# print("한국식 표현 (년/월/일) : {}/{}/{}".format(now.year,now.month,now.day))
# print("미국식 표현 (월/일/년) : {}/{}/{}".format(now.month,now.day,now.year))
# print("영국식 표현 (일/월/년) : {}/{}/{}".format(now.day, now.month, now.year))


#3번 실습문제
# print("세번째 실습문제")
# brith_year = int(input("Enter your birth year: "))
# brith_month = int(input("Enter your birth month:"))
# brith_day = int(input("Enter your birth day:"))
#
# brith_date = datetime.date(brith_year, brith_month, brith_day)
# today = datetime.date.today()
# days_between_birth = (today - brith_date).days
#
# print("출생일 {}년{}월{}일로 부터 {}일 지났습니다".format(brith_year, brith_month, brith_day, days_between_birth))

#4번 실습문제
# import datetime
#
# now = datetime.datetime.now()
# today = datetime.date.today()
#
# days = int(input("Enter the number of days : "))
#
# if days > 0 :
#     future_date = today + datetime.timedelta(days) #핵심
#     future_str = future_date.strftime("%Y년 %m월 %d일")
#     print("오늘은 {}년{}월{}일 입니다".format(now.year, now.month, now.day))
#     print("{}일 후는 {}년{}월{}일 입니다".format(days, future_date.year, future_date.month, future_date))
# else :
#     print("양수를 입력하세요")

#5번 실습문제
# personal_info = []
# personal_info.append(input("Enter your name : "))
# personal_info.append(int(input("Enter your age : ")))
# personal_info.append(float(input("Enter your height : ")))

#6번 실습문제
def average() :
    num = []
    repeat = int(input("몇번 반복할까요? (최대 10번) : "))
    if repeat <= 10 :
        for i in range(repeat) :
            num.append(int(input("정수를 입력하세요 : ")))
            i += 1

        print(num)
        print(sum(num))
        aver = sum(num) / len(num)
        return aver
    else :
        print("최대 10번 입니다.")
        average()

print(average())



