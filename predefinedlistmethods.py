Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> type(a)
<class 'list'>

>>> a.append(3)
>>> a
[3]
>>> a.extend(34,'hi',32)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.extend(34,'hi',32)
TypeError: list.extend() takes exactly one argument (3 given)
>>> a
[3]
>>> a.extend([23,5,4,23,2,1,6,7,9])
>>> a
[3, 23, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a.insert(2,50)
>>> a
[3, 23, 50, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a[2:3]=[]
>>> a
[3, 23, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a
[3, 23, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a[2:3]=(34,5)
>>> a
[3, 23, 34, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a
[3, 23, 34, 5, 4, 23, 2, 1, 6, 7, 9]
>>> a.pop()
9
>>> a
[3, 23, 34, 5, 4, 23, 2, 1, 6, 7]
>>> a.remove(23)
>>> a
[3, 34, 5, 4, 23, 2, 1, 6, 7]
>>> del a[1:2]
>>> a
[3, 5, 4, 23, 2, 1, 6, 7]
del a
a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=[23,4,3,23,23,2,23]
a
[23, 4, 3, 23, 23, 2, 23]
a.clear()
a
[]
a=[89,6,7,8]
a[1:3]=[]
a
[89, 8]
a
[89, 8]
a.extend(34,5,4,2,3,78,9)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.extend(34,5,4,2,3,78,9)
TypeError: list.extend() takes exactly one argument (7 given)
a.extend([32,445,6,7,34])
a
[89, 8, 32, 445, 6, 7, 34]
max(a)
445
min(a)
6
len(a)
7
count(89)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    count(89)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(8)
1
a
[89, 8, 32, 445, 6, 7, 34]
sum(a)
621
89+8+32+445+6+7+34
621
a.index(3)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.index(3)
ValueError: 3 is not in list
a.index(445)
3
a.index(34)
6
a.reverse()
a
[34, 7, 6, 445, 32, 8, 89]
a.sort()
a
[6, 7, 8, 32, 34, 89, 445]
b=a.copy()
b
[6, 7, 8, 32, 34, 89, 445]
a
[6, 7, 8, 32, 34, 89, 445]
x=[]
y=[23,45,56,3,9]
z=[23,0,45,4,3]
all(x)
True
all(y)
True
all(z)
False
any(x)
False
any(y)
True
any(z)
True
s=list(enumerate(a))
s
[(0, 6), (1, 7), (2, 8), (3, 32), (4, 34), (5, 89), (6, 445)]
a
[6, 7, 8, 32, 34, 89, 445]
a.index(445)
6
len(a)
7
sum(a)
621
count(32)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    count(32)
NameError: name 'count' is not defined. Did you mean: 'round'?

a.count(32)
1

=============================================================== RESTART: D:/python/forlistappend.py ===============================================================
Enter values:23
Enter values:34
Enter values:"hi"
Enter values:23
Enter values:1
['23', '34', '"hi"', '23', '1']
a
['23', '34', '"hi"', '23', '1']

=============================================================== RESTART: D:/python/forlistappend.py ===============================================================
Enter values:23
['23']
Enter values:g
['23', 'g']
Enter values:34
['23', 'g', '34']
Enter values:23
['23', 'g', '34', '23']
Enter values:2
['23', 'g', '34', '23', '2']
a
['23', 'g', '34', '23', '2']

=============================================================== RESTART: D:/python/forlistappend.py ===============================================================
Enter values:bye
Enter values:2023
Enter values:welcome
Enter values:2024
Enter values:happy new year
['bye', '2023', 'welcome', '2024', 'happy new year']

================================================================ RESTART: D:/python/forlistapp2.py ================================================================
Enter values:23
Traceback (most recent call last):
  File "D:/python/forlistapp2.py", line 4, in <module>
    a.append(y)
NameError: name 'a' is not defined
34

================================================================ RESTART: D:/python/forlistapp2.py ================================================================
Enter values:56
Enter values:89
Enter values:96
Enter values:8
Enter values:9
Enter values:4
Enter values:8
Enter values:95
Enter values:34
Enter values:98
[56, 89, 96, 8, 9, 4, 8, 95, 34, 98]
x
[56, 89, 96, 8, 9, 4, 8, 95, 34, 98]

================================================================ RESTART: D:/python/forlistapp3.py ================================================================
Traceback (most recent call last):
  File "D:/python/forlistapp3.py", line 3, in <module>
    x.append(a)
NameError: name 'x' is not defined

================================================================ RESTART: D:/python/forlistapp3.py ================================================================
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

================================================================ RESTART: D:/python/forlistapp3.py ================================================================
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

================================================================ RESTART: D:/python/forlistapp3.py ================================================================
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

================================================================ RESTART: D:/python/forlistapp2.py ================================================================
Enter values:34
Enter values:34
Enter values:34
Enter values:fd
Traceback (most recent call last):
  File "D:/python/forlistapp2.py", line 4, in <module>
    y=int(input("Enter values:"))
ValueError: invalid literal for int() with base 10: 'fd'
34
34
34
34
34


=============================================================== RESTART: D:/python/forlistappend.py ===============================================================
Enter values:df
Enter values:df
Enter values:34
Enter values:32
Enter values:fds
['df', 'df', '34', '32', 'fds']
