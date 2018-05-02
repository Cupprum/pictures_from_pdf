from pyPdf import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

pdf = PdfFileReader(open('doc1.pdf', 'rb'))
output = PdfFileWriter()

length = pdf.getNumPages()

for x in range(1, length - 3):
    page = pdf.getPage(x)

    page.cropBox.lowerLeft = (45, 55)
    page.cropBox.upperRight = (550, 795)

    output.addPage(page)

with open("out.pdf", "wb") as out_f:
    output.write(out_f)

im = convert_from_path('out.pdf')[0]

txt = open('blackandwhite.txt', 'w')

p = np.array(im)

for x in p:
    list_docastny = ""
    for y in x:
        if str(y) == "[255 255 255]":
            list_docastny += "w"
        else:
            list_docastny += "b"
    txt.write(str(list_docastny))
    txt.write('\n')
