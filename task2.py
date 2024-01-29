from tabulate import tabulate
import matplotlib.pyplot as plt

n = []
t = []
e = []
m = []
s = []
ss = []
total = []
avg = []

for i in range(10):
    name = input("Enter Name: ")
    n.append(name)
    
    tamil = int(input("Tamil: "))
    t.append(tamil)
    
    english = int(input("English: "))
    e.append(english)
    
    maths = int(input("Maths: "))
    m.append(maths)
    
    science = int(input("Science: "))
    s.append(science)
    
    social = int(input("Social: "))
    ss.append(social)
    
    # Calculate Total
    tot = tamil + english + maths + science + social
    total.append(tot)
    
    # Calculate Average
    average = tot / 5
    avg.append(average)

x = []
h = ["Sno", "Name", "Tamil", "English", "Maths", "Science", "Social", "Total", "Average"]

for i in range(10):
    y = [i+1, n[i], t[i], e[i], m[i], s[i], ss[i], total[i], avg[i]]
    x.append(y)

print(tabulate(x, headers=h, tablefmt='simple'))
plt.bar(n, total)
plt.xlabel('Student Names')
plt.ylabel('Total Marks')
plt.title('Total Marks for 10 Students')
plt.show()
