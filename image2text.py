import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("sample/content.png") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('sample/temp2.jpg')
im = Image.open("sample/content.png")
text = pytesseract.image_to_string(im)
print(text)
