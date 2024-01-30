#File Append:

x=open("D://fwrite3.txt","a")
n=int(input("Enter Number of students:"))
for i in range(n):
    
    roll=int(input("Enter Rollno:"))
    name=input("Enter Name:")
    m1=int(input("Enter Mark1:"))
    m2=int(input("Enter Mark2:"))
    m3=int(input("Enter Mark3:"))
    tot=m1+m2+m3
    avg=tot/3
    x.write(str(roll)+"\t"+name+"\t"+str(m1)+"\t"+str(m2)+"\t"+str(m3)+"\t"+str(tot)+"\t"+str(avg)+"\n")
x.close()
