import PythonMagick
img = PythonMagick.Image()
img.density("300")
img.read("Desktop/path.PDF") # read in at 300 dpi
img.write("Desktop/test.PNG")
