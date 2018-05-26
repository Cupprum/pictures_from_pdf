from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import os


name_of_file = input('nazov : ')

counter_pack = 1
actual_maturita = PdfFileReader(open(name_of_file, 'rb'))
lenght = actual_maturita.getNumPages() - 2

os.system(f"mkdir TEST")

for alfa in range(1, lenght):
    im1 = convert_from_path(name_of_file)[alfa]

    im1.save(
        f"TEST/{name_of_file[:3]}_{counter_pack}.jpg")

    counter_pack += 1
