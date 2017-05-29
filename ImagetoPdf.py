import PIL
import PIL.Image

filename = 'filename'
im = PIL.Image.open('a.jpg')

newfilename = 'path1.pdf'
PIL.Image.Image.save(im, newfilename, "PDF", resolution = 100.0)
