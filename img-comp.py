import PIL
from PIL import Image
from tkinter.filedialog import *
file_path = askopenfilename()
image = PIL.Image.open(file_path)
height, width = image.size
img = image.resize((height, width) , PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+"compressed-image.jpg")
