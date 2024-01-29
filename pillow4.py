n=int(input("Enter the ID No:"))
from PIL import Image
if(n==1):
    print("Welcome to our JS studio")
    print("Name:Sree")
    print("Address:Madurai")
    print("Lost visiting Date:10.01.2024")
    print("Mobile No:123456789")
    print("Thank You visit again..!")
    a=Image.open("D:/sch1.jpg")
    a.show()
elif(n==2):
    print("Welcome to our JS studio")
    print("Name:Chatresh")
    print("Address:Chennai")
    print("Lost visiting Date:24.11.2023")
    print("Mobile No:987654321")
    print("Thank You visit again..!")
    a=Image.open("D:/sch2.jpg")
    a.show()
elif(n==3):
    print("Welcome to our JS studio")
    print("Name:Teena")
    print("Address:Bangalore")
    print("Lost visiting Date:22.01.2022")
    print("Mobile No:132435467")
    print("Thank You visit again..!")
    a=Image.open("D:/sch3.jpg")
    a.show()
else:
    print("Invalid ID Enter the valid ID")
    
