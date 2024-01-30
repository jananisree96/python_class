#File Read:

#keyword--1.ForLoop:

x=open("D://fwrite2.txt","r")
for i in x:
    print(i)
x.close()

#keyword--2.readline:

x=open("D://fwrite3.txt","r")
y=x.readline()
print(y)
y=x.readline()
print(y)
x.close()

#keyword--3.read:
#Ex1:
x=open("D://fwrite.txt","r")
y=x.read(11)
print(y)
x.close()

#Ex2:
a=open("D://fwrite.txt","r")
b=a.read()
print(b)
a.close()


