#unpack method:
name=input("Enter your name:")
age=int(input("Enter your age:"))
dob=input("Enter your DOB:")
address=input("Enter your address:")
def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
print_details(name=name,age=age,dob=dob,address=address)


