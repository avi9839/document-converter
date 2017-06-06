import pytesseract
from PIL import Image, ImageFont, ImageOps, ImageDraw, ImageEnhance, ImageFilter


def image2text(file):
	im = Image.open(file) # the second one
	im = im.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(im)
	im = enhancer.enhance(2)
	im = im.convert('1')
	im.save('sample/temp.jpg')
	text = pytesseract.image_to_string(Image.open(file),lang='eng').encode('cp850','replace').decode('cp850')
	textfile = open("output/output.txt","w")
	textfile.write(text)

def text_image(text_path, font_path=None):
	"""Convert text file to a grayscale image with black characters on a white background.

	arguments:
	text_path - the content of this file will be converted to an image
	font_path - path to a font file (for example impact.ttf)
	"""
	grayscale = 'L'
	# parse the file into lines
	with open(text_path) as text_file:  # can throw FileNotFoundError
	    lines = tuple(l.rstrip() for l in text_file.readlines())

	# choose a font (you can see more detail in my library on github)
	large_font = 20  # get better resolution with larger size
	font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
	try:
	    font = PIL.ImageFont.truetype(font_path, size=large_font)
	except IOError:
	    font = PIL.ImageFont.load_default()
	    print('Could not use chosen font. Using default.')

	# make the background image based on the combination of font and lines
	pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
	max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
	# max height is adjusted down because it's too large visually for spacing
	test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	max_height = pt2px(font.getsize(test_string)[1])
	max_width = pt2px(font.getsize(max_width_line)[0])
	height = max_height * len(lines)  # perfect or a little oversized
	width = int(round(max_width + 40))  # a little oversized
	image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
	draw = PIL.ImageDraw.Draw(image)

	# draw each line of text
	vertical_position = 5
	horizontal_position = 5
	line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
	for line in lines:
	    draw.text((horizontal_position, vertical_position),
	              line, fill=PIXEL_ON, font=font)
	    vertical_position += line_spacing
	# crop the text
	c_box = PIL.ImageOps.invert(image).getbbox()
	image = image.crop(c_box)
	image.save('result.jpg')

image2text("sample/image.jpg")