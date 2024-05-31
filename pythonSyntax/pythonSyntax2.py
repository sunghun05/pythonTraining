# #맴버체크
# listdata = [1,2,3,4]
# ret1 = 5 in listdata
# ret2 = 4 in listdata
# print(ret1); print(ret2)
# strdata = 'abcde'
# ret3 = 'c' in strdata
# ret4 = 'l' in strdata
# print(ret3); print(ret4)
# ret5 = 'abc' in strdata
# print(ret5)
#
# #문자열
# strdata1 = '나는 파이썬'
# strdata2 = 'you are a programmer'
# strdata3 = """I love
#     python. You love
#     python"""
# strdata4 = "My son's name is <NAME>"
#
# print(strdata3)
#
# print("이 문장은 화면 폭에 비해 너무 길어 보기가 힘듭니다. \
# 그래서 enter키를 이용해 문장을 다음 줄과 연속되게 합니다.")
#
# #list
#
# def myfunc():
#     print("Hello")
#
# list4 = [1,2,myfunc]
# list4[2]()
#
#
# #tuple
# """
#     튜플의 요소는 변경 불가
# """
#
# tuple1 = (1,2,3,4,5)
# tuple2 = ('a','b','c')
# tuple3 = (1, 'a' , 'abc', [1,2,3,4,5], ['a','b','c'])
# # tuple1[0] = 6
#
# def myfunc1():
#     print("Hello")
#
# tuple4 = (1,2,myfunc1)
#
# tuple4[2]()
#
# #dictionary
#
# dict1 = {'a':1,'b':2,'c':3}
# print(dict1['a'])
# dict1['d'] = 4
# print(dict1)
# dict1['b'] = 7
# print(dict1)
# print(len(dict1))

#def 인자 이해

# def add_txt(t1, t2='파이썬'):
#     print(t1+':'+t2)
#
# add_txt('best')
# add_txt(t2='korea', t1='won')
# """
#
# """
#
#
# """
#     *args : 가변 인자. 인자의 개수가 불분명할때 사용
#     함수 내에서 튜플로 처리
#     아무런 값 없을 때 빈 튜플
# """
# def func1(*args):
#     print(args)
#
#
# """
#     **kwargs :  키워드 인자가 불분명할 경우 사용
#     차후 어떤 키워드 인자가 필요한지 확정되지 않은 경우 **kwargs를 사용하여 인자를 지정.
#     사전으로 처리됨.
# """
# def func2(width, height, **kwargs):
#     print(kwargs)
#
# func1()
# func1(3,5,1,5)
# func2(10, 20)
# func2(10,20, depth=50, color='blue')

# param = 10
# strdata = '전역변수'
#
# def func1():
#     strdata = '지역변수'

# name='mike'
# def greeting():
#     print("minsu")
#     return
#
# class hi():
#     name = 'jane'
#     def __init__(self, name):
#         print("Hi "+name)
#         print("My name is "+self.name)
#
#         print("his name is "+name)
#         return
#
#     def greeting(self):
#         print("her name is "+name)
#         return
#
#     def goodbye(self):
#         self.greeting()
#         greeting()
#         return
#
# A = hi('sunghun')
# A.greeting()
# A.goodbye()

f = open("files/log_1", 'w')

for i in range(1,11):
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)

f = open("files/log_1", 'r')
lines = f.readlines()

for line in lines:
    print(line)
f.close()

