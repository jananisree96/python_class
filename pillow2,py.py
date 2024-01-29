#pillow:

from PIL import Image
a=Image.open("D:/duck.jpg")
a.show()
x=a.rotate(120,expand=True)
x.show()
z=a.save("E:/duckcopy.jpg")
