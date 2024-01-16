#Date and Time:

print("---------Get current date and time--------")
from datetime import date
today=date.today()
print("Today's date:",today)
print()

print("------------Time-------------")
from datetime import time
A=time()
print(A)
B=time(10,45,40,000000)
print(B)
print("Hour=",B.hour)
print("Minute=",B.minute)
print("Second=",B.second)
print("Microsecond=",B.microsecond)
print()

print("--------Timeprint---------")
from datetime import datetime
now=datetime.now().time()
print(now)

print("--------Difference between two dates---------")
from datetime import datetime,date
T1=date(year=2020,month=1,day=19)
T2=date(year=2021,month=1,day=20)
T3=T2-T1
print(T3)
print()

print("-------Difference between Two times-------")
from datetime import timedelta
t1=timedelta(seconds=33)
t2=timedelta(seconds=54)
t3=t1-t2
print(abs(t3))
print()

print("-------General time print--------")
from datetime import datetime
a=datetime(2018,11,28)
print(a)
b=datetime(2017,11,28,23,55,59,342380)
print(b)
print()

print("--------General sleep function--------")
import time
a=10
b=5
print("Addition of a and b:",a+b)
time.sleep(5)
print("After 5 seconds")
print("subtraction of a and b:",a-b)
