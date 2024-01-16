#find max number into the list:
a=[[23,44,77,89],[84,97,121,89],[99,12,77,99]]
max_num1=a[0][0]
max_num2=a[1][0]
max_num3=a[2][0]
for num in a[0]:
    if num > max_num1:
        max_num1 = num
    for num in a[1]:
      if num > max_num2:
        max_num2 = num
    for num in a[2]:
     if num > max_num3:
        max_num3 = num
print("the maximum number is:",max_num1)
print("the maximum number is:",max_num2)
print("the maximum number is:",max_num3)

    
    
