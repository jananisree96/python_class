import matplotlib.pyplot as plt
from tabulate import tabulate
import datetime

x = datetime.datetime.now()
print("Today Date & Time:", x)
f = open("D://stationery.txt", "w")
print("welcome stationery world")
print("***Available products***\n 1.Pen \n 2.Note \n 3.Pencil \n")
n = int(input("Enter your choice:"))

if n == 1:
    product_name = "Pen"
    print("You are selected Pen\n")
    qty = int(input("How many pen do u want?:"))
    price = 30
    tot = price * qty
    print("Total:", tot)
    f.write("You are selected Pen\n")
    f.write("Price:" + str(price) + "\n")
    f.write("Qty:" + str(qty) + "\n")
    f.write("Total:" + str(tot) + "\n")
    f.close()

elif n == 2:
    product_name = "Note"
    print("You are selected Note\n")
    qty = int(input("How many Note do u want?:"))
    price = 50
    tot = price * qty
    print("Total:", tot)
    f.write("You are selected Note\n")
    f.write("Price:" + str(price) + "\n")
    f.write("Qty:" + str(qty) + "\n")
    f.write("Total:" + str(tot) + "\n")
    f.close()

elif n == 3:
    product_name = "Pencil"
    print("You are selected Pencil\n")
    qty = int(input("How many pencil do u want?:"))
    price = 20
    tot = price * qty
    print("Total:", tot)
    f.write("You are selected Pencil\n")
    f.write("Price:" + str(price) + "\n")
    f.write("Qty:" + str(qty) + "\n")
    f.write("Total:" + str(tot) + "\n")
    f.close()

else:
    print("Invalid option please select one of the numbers:1,2,3")
    exit()

# Display a table using tabulate
table_data = [["Product", "Price", "Qty", "Total"],[product_name, price, qty, tot]]
table = tabulate(table_data, headers="firstrow", tablefmt="grid")
print("\n", table)

# Create a bar chart using matplotlib
categories = ["Price", "Qty", "Total"]
values = [price, qty, tot]

plt.bar(categories, values, color=['blue', 'orange', 'green'])
plt.title(f"{product_name} Details")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
