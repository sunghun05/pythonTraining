import math
a = 1 + 3j
print(a.real)
print(a.imag)
print(a.conjugate())

import time
time1 = time.localtime()
time2 = time.strftime("%Y%m%d-%H:%M")
print(time2)
print(time1)

import datetime
time3 = datetime.datetime.now()
year = time3.year
print(year)
now = datetime.datetime.now()
print(now.weekday())
