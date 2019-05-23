from PIL import Image
from pytesseract import image_to_string
from fpdf import FPDF

#open a folder and loop around the documents

#check that the order title has OPGORDER in it?

image = Image.open('order name variable.tif')
image.load()
parsing = ""

# our tiffs have multiple frames or pages
for frame in range(0, image.n_frames):
    image.seek(frame)
    parsing += image_to_string(image)
    parsing += '\n'

# these characters were causing the pdf write process to fail with a latin vs unicode spat
parsing = parsing.replace('\u2018', "'")
parsing = parsing.replace('\u2019', "'")
parsing = parsing.replace('\u201c', '"')
parsing = parsing.replace('\u201d', '"')

pdf = FPDF()
pdf.add_page(orientation = 'P')
pdf.set_font('Arial', size=12)
pdf.write(5, parsing)
pdf.output('pdfs\output variable.pdf')