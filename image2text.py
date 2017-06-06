import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("sample/image.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('sample/temp2.jpg')
im = Image.open("Avinash.jpg")
text = pytesseract.image_to_string(im,lang='eng')
print(text.encode("utf-8"))
