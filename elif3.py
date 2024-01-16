#elif:
print("1 for dep\n,2 for wd\n,3 for balchk\n,4 for exit\n")
bal=1000
print("Minimum balance")
choice=int(input("Enter your choice:"))
if(choice==1):
    dep=int(input("Enter your deposit amt:"))
    bal=bal+dep
    print("Successfully deposited your current balance is:",bal)
elif(choice==2):
    wd=int(input("Enter your withdraw amt:"))
    bal=bal-wd
    print("Successfully withdraw your current balance is:",bal)
elif(choice==3):
    print("Your current bal is:",bal)
elif(choice==4):
    print("Thank u")
else:
    print("Error:Invalid option")
    
    
