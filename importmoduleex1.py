#import module:
ch=int(input("Enter your choice:"))
if(ch==1):
    import funadd
    funadd.add()
elif(ch==2):
    import funsub
    funsub.sub()
else:
    print("Invalid choice")
