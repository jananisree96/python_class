#pillow:

from PIL import Image
x=Image.open("D:/img1.jpg")
x.show()
y=x.rotate(90,expand=True)
y.show()
z=y.save("D:/copy1.jpg")
