Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
h="welcome"
h
'welcome'
3+4
7
print("hi")
hi
x=10
y=1.5
z=6j
type(x)
<class 'int'>
type(y)
<class 'float'>
type(z)
<class 'complex'>

================================================================ RESTART: D:\python\outputmethod.py ===============================================================
RollNo: 121
Name: Janani sree
Age: 22
Address: Madurai

================================================================ RESTART: D:\python\outputmethod.py ===============================================================
Enter No:121
Enter the name:janani
Enter age:22
Enter Address:madurai
Details
Rollno: 121
Name: janani
Age: 22
Address: madurai

================================================================== RESTART: D:\python\arithop.py ==================================================================
**Arithmetic operator**
Enter A:12
Enter B:2
Add: 14
Sub: 10
Mul: 24
Div: 6.0
Mod: 0
Exponentiation: 144
Floor Division: 6
id(x)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    id(x)
NameError: name 'x' is not defined
x=10
y=2.5
z=h6+j
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    z=h6+j
NameError: name 'h6' is not defined
z=4+6j
type(x)
<class 'int'>
type(y)
<class 'float'>
type(z)
<class 'complex'>
id(x)
140724681456344
id(y)
1456424069424
id(z)
1456424072112
a="sree"
type(a)
<class 'str'>
id(a)
1456430253856
a=int(y)
b=float(x)
c=int(z)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c=int(z)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
type(a)
<class 'int'>
type(b)
<class 'float'>
a
2
b
10.0
c
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c
NameError: name 'c' is not defined
z
(4+6j)
c=complex(x)
c
(10+0j)



================================================================== RESTART: D:\python\arithop.py ==================================================================
**Arithmetic operator**
Enter A:10
Enter B:5
Add: 15
Sub: 5
Mul: 50
Div: 2.0
Mod: 0
Exponentiation: 100000
Floor Division: 2

================================================================== RESTART: D:\python\comparop.py =================================================================
**comparision operator**
Enter x value:12
Enter y value:12
Equal to: True
Greater than: False
Less than: False
Greater than or equal: True
Less than or equal: True
Not equal: False

=================================================================== RESTART: D:\python\logiop.py ==================================================================
Logical operator:
Enter A value:12
Enter B value:5
And operator: False
Or operator: False
Not operator: False

================================================================== RESTART: D:\python\assigop.py ==================================================================
Assignment operators
Enter x value:10
Enter y value:5
x value: 15
x value: 10
x value: 50
x value: 10.0

================================================================== RESTART: D:\python\assigop.py ==================================================================
Assignment operators
Enter x value:10
Enter y value:5
x value: 15
x value: 10
x value: 50
x value: 10.0
x value: 0.0

================================================================== RESTART: D:\python\assigop.py ==================================================================
Assignment operators
Enter x value:150
Enter y value:50
x value: 18
x value: 50
x value: 0
x value: 0
x value: 0



a=10
b=10
x="hi"
y="hi"
a is b
True
b is a
True
x is y
True
a is not b
False
a is not x
True
a is b
True
a is x
False
a is not y
True
'i' in x
True
'h' in y
True
'J' in x
False
'L' not in y
True
10 in b
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    10 in b
TypeError: argument of type 'int' is not iterable
'h' not in y
False
'i' in y
True


x=[]
type(x)
<class 'list'>
x=['hi',3,5,'hlo',2,12,'bye']
x
['hi', 3, 5, 'hlo', 2, 12, 'bye']
x[4]
2
x[6]
'bye'
x[:0]
[]
x[0:]
['hi', 3, 5, 'hlo', 2, 12, 'bye']
x[2:]
[5, 'hlo', 2, 12, 'bye']
x[:4]
['hi', 3, 5, 'hlo']
x[1:5]
[3, 5, 'hlo', 2]
x[-2]
12
x[-5:-1]
[5, 'hlo', 2, 12]
x*2
['hi', 3, 5, 'hlo', 2, 12, 'bye', 'hi', 3, 5, 'hlo', 2, 12, 'bye']
x+[12,3,5]
['hi', 3, 5, 'hlo', 2, 12, 'bye', 12, 3, 5]
x
['hi', 3, 5, 'hlo', 2, 12, 'bye']
x+=[5,'welcome',3]
x
['hi', 3, 5, 'hlo', 2, 12, 'bye', 5, 'welcome', 3]
x[9]
3
x[10]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x[10]
IndexError: list index out of range
type(x)
<class 'list'>
id(x)
2795351632768
y=()
type(y)
<class 'tuple'>
y=('hlo',45,3,2,45,'bye')
y
('hlo', 45, 3, 2, 45, 'bye')
y[3]
2
y[:4]
('hlo', 45, 3, 2)
y[-2]
45
y[-5:-1]
(45, 3, 2, 45)
y**2
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    y**2
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
y**2
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    y**2
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
y[2:4]
(3, 2)
y
('hlo', 45, 3, 2, 45, 'bye')
y*2
('hlo', 45, 3, 2, 45, 'bye', 'hlo', 45, 3, 2, 45, 'bye')
y[2]=4
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    y[2]=4
TypeError: 'tuple' object does not support item assignment
y
('hlo', 45, 3, 2, 45, 'bye')
y+=('like')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    y+=('like')
TypeError: can only concatenate tuple (not "str") to tuple
y=('hlo',45,3,2,45,'bye','like')
y
('hlo', 45, 3, 2, 45, 'bye', 'like')
y[7]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    y[7]
IndexError: tuple index out of range
y[5]
'bye'
y[6]
'like'
y
('hlo', 45, 3, 2, 45, 'bye', 'like')
a={}
type(a)
<class 'dict'>
a=set()
type(a)
<class 'set'>
a={'welcome',45,2,3,45,'bye'}
a
{2, 3, 'welcome', 'bye', 45}
a[3]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a[3]
TypeError: 'set' object is not subscriptable
a
{2, 3, 'welcome', 'bye', 45}
a(0)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a(0)
TypeError: 'set' object is not callable
a
{2, 3, 'welcome', 'bye', 45}
a
{2, 3, 'welcome', 'bye', 45}
b={}
type(b)
<class 'dict'>
b={"roll":121,"name":"Sree","age":22,"address":"mdu"}
b
{'roll': 121, 'name': 'Sree', 'age': 22, 'address': 'mdu'}
b[2]
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    b[2]
KeyError: 2
b["age"]
22
b["name"]
'Sree'
b["roll']
  
SyntaxError: unterminated string literal (detected at line 1)
b['roll']
  
121
b['address']
  
'mdu'
b
  
{'roll': 121, 'name': 'Sree', 'age': 22, 'address': 'mdu'}
b
  
{'roll': 121, 'name': 'Sree', 'age': 22, 'address': 'mdu'}

b["address"]
  
'mdu'
b["mdu"]
  
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b["mdu"]
KeyError: 'mdu'


================================================================== RESTART: D:/python/ifelse2.py ==================================================================
Enter A value:12
Number is positive

================================================================== RESTART: D:/python/ifelse2.py ==================================================================
Enter number:-9
Number is negative

=================================================================== RESTART: D:/python/elif2.py ===================================================================
1 for  football
 2 for cricket
 3 for tennis
Enter your choice:1
you are selected football

=================================================================== RESTART: D:/python/elif2.py ===================================================================
1 for  football
 2 for cricket
 3 for tennis
Enter your choice:2
you are selected cricket

=================================================================== RESTART: D:/python/elif2.py ===================================================================
1 for  football
 2 for cricket
 3 for tennis
Enter your choice:3
you are selected tennis

=================================================================== RESTART: D:/python/elif2.py ===================================================================
1 for  football
 2 for cricket
 3 for tennis
Enter your choice:6
Error

=================================================================== RESTART: D:/python/elif2.py ===================================================================
1 for  football
 2 for cricket
 3 for tennis
Enter your choice:9
Error




================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
Enter y value:12
x is greater than y


================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:1
Enter y value:2
x is less than y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
Enter y value:233
x is less than y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:89
Enter y value:9
x is not equal to y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
Enter y value:1
x is not equal to y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
Enter y value:23
x is less than y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
x is less than y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:130
x is less than y

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:12
x is less than 50

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:156
x is greater than 150

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:134
x is less than 150

================================================================= RESTART: D:/python/nestedif2.py =================================================================
Enter x value:60
x is greater than 50


x
  
60
x="banana"
  
for i in x:
  print(i)

  
b
a
n
a
n
a
for i in x:
  print(x)

  
banana
banana
banana
banana
banana
banana


for i in range(25):
  print(i)

  
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24


for i in range(30):
  print i
  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(i)
  
24


i
  
24
for i in range(0:20):
  
SyntaxError: invalid syntax
for i in range(0,25):

  print(i)

  
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
for i in range(3,25,2):
  print(i)

  
3
5
7
9
11
13
15
17
19
21
23




a="janani sree"
  
for i in a:
  print(i)

  
j
a
n
a
n
i
 
s
r
e
e


for i in a:
  print(a)

  
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree
janani sree


x=[12,34,56,3.5,34,2,'hi']
  
x
  
[12, 34, 56, 3.5, 34, 2, 'hi']
for i in x:
  print(x)

  
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
[12, 34, 56, 3.5, 34, 2, 'hi']
>>> for i in x:
...   print(i)
... 
...   
12
34
56
3.5
34
2
hi
>>> 
>>> 
>>> print(x[::-1])
...   
['hi', 2, 34, 3.5, 56, 34, 12]
>>> 
>>> n="janani"
...   
>>> for i in a:
...   print(a[::-1])
... 
...   
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
eers inanaj
>>> 
>>> 
>>> "type,id,i/p,o/p method,operators,datatypes,conditional statement,for loop"
...   
'type,id,i/p,o/p method,operators,datatypes,conditional statement,for loop'
