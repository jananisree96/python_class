#nested if:
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
n3=int(input("Enter num3:"))
if(n1>n2):
    if(n1>n3):
        print("n1 is big")
    else:
        print("n2 is big")
else:
    if(n2>n3):
        print("n2  is big")
    else:
        print("n3 is big")        
    
