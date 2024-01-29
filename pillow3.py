#pillow Transpose

import PIL
from PIL import Image
im=Image.open("D:/img1.jpg")
im.show()
out=im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
out.save("D:/transpillow.jpg")
out.show()
