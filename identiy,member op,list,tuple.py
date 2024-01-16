Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
b=10
a is b
True
a is not b
False
c='hi'
d='hi'
c is d
True
c is a
False
c is not a
True
c is not d
False
a is not c
True
a is not d
True
a is not b
False
c is not a
True
c is not d
False
'i' in c
True
'H' in c
False
10 in a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    10 in a
TypeError: argument of type 'int' is not iterable
10 not in a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    10 not in a
TypeError: argument of type 'int' is not iterable
'o' not inc
SyntaxError: invalid syntax
'o' not in c
True
'o' in c
False
a=[]
type(a)
<class 'list'>
a=[1,2,'hi',4,5]
a
[1, 2, 'hi', 4, 5]
a[0]
1
a[:2]
[1, 2]
a[3:]
[4, 5]
a[1:4]
[2, 'hi', 4]
a+[5,6]
[1, 2, 'hi', 4, 5, 5, 6]
a
[1, 2, 'hi', 4, 5]
a+=[5,6,"bye"]
a
[1, 2, 'hi', 4, 5, 5, 6, 'bye']
a*3
[1, 2, 'hi', 4, 5, 5, 6, 'bye', 1, 2, 'hi', 4, 5, 5, 6, 'bye', 1, 2, 'hi', 4, 5, 5, 6, 'bye']
dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a.sort()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a
[1, 2, 'hi', 4, 5, 5, 6, 'bye']
>>> a=()
>>> type(a)
<class 'tuple'>
>>> a=(9,8,7,1,2,3.5,"hello",3,4)
>>> a
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4)
>>> a[6]
'hello'
>>> a[-2]
3
>>> a[1:4]
(8, 7, 1)
>>> a[:6]
(9, 8, 7, 1, 2, 3.5)
>>> a[6:]
('hello', 3, 4)
>>> a[-4:-1]
(3.5, 'hello', 3)
>>> a+=(10,20)
>>> a
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4, 10, 20)
>>> a
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4, 10, 20)
>>> a+(4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a+(4)
TypeError: can only concatenate tuple (not "int") to tuple
>>> b=(78,9,8)
>>> a+b
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4, 10, 20, 78, 9, 8)
>>> a
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4, 10, 20)
>>> a+=(78,9,8)
>>> a
(9, 8, 7, 1, 2, 3.5, 'hello', 3, 4, 10, 20, 78, 9, 8)
>>> type(a)
<class 'tuple'>
