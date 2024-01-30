#File write:

x=open("D://fwrite2.txt","w")
roll=int(input("Enter Rollno:"))
name=input("Enter Name:")
m1=int(input("Enter Mark1:"))
m2=int(input("Enter Mark2:"))
m3=int(input("Enter Mark3:"))
tot=m1+m2+m3
avg=tot/3
x.write("Roll\t Name\t M1\t M2\t M3\t Total\t Avg\n")
x.write(str(roll)+"\t"+name+"\t"+str(m1)+"\t"+str(m2)+"\t"+str(m3)+"\t"+str(tot)+"\t"+str(avg)+"\n")
x.close()
