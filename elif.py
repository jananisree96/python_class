#elif:
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("1 for add\n 2 fo sub\n 3 for mul\n 4 for div\n 5 for mod\n 6 for exponentation\n 7 for floordiv")
choice=int(input("Enter your choice:"))
if(choice==1):
    res=num1+num2
    print("Add:",res)
elif(choice==2):
    res=num1-num2
    print("Sub:",res)
elif(choice==3):
    res=num1*num2
    print("Mul:",res)
elif(choice==4):
    res=num1/num2
    print("Div:",res)
elif(choice==5):
    res=num1%num2
    print("Mod:",res)
elif(choice==6):
    res=num1**num2
    print("Exponentation:",res)
elif(choice==7):
    res=num1//num2
    print("Floor division:",res)
else:
    print("Error selection")
    
