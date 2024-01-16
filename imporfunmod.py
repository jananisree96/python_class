#import module user def fun to import predef fun using elif:
print(" 1 for add\n 2 for sub \n 3 for mul\n 4 for div")
choice=int(input("Enter your choice:"))
if(choice==1):
    print("Addition is importing")
    import funadd
    funadd.add()
elif(choice==2):
    print("Subtraction is importing")
    import funsub
    funsub.sub()
elif(choice==3):
    print("Multiplication is importing")
    import funmul
    funmul.mul()
elif(choice==4):
    print("Division is importing")
    import fundiv
    fundiv.div()
else:
    print("Invalid choice")
