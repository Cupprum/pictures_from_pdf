from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import numpy as np
import time
import glob
import os


def last_step():
    zadanie = im1.crop(
        (190, final_list1[x] + 5, 1520, final_list1[x + 1] - 5))
    zadanie.save(
        f"IMG/{act}/{act}_{counter_order}.jpg")


list_maturita = glob.glob(
    'PDF/*.pdf')

for maturita in list_maturita:
    start_time = time.time()

    counter_order = 0
    counter_stop = 0

    actual_maturita = PdfFileReader(open(f"{maturita}", 'rb'))
    lenght = actual_maturita.getNumPages() - 2

    os.system(f"mkdir IMG/{maturita[4:-4]}")

    for alfa in range(1, lenght):
        im1 = convert_from_path(maturita)[alfa]

        p1 = np.array(im1)

        list1 = []
        line1 = 0

        for x in p1:
            list_docastny = ""
            counter = 0
            for y in range(170, 1450):
                if str(x[y]) == "[255 255 255]":
                    break
                else:
                    counter += 1
            if counter >= 900:
                list1.append(line1)
            line1 += 1

        final_list1 = list1[:]

        act = maturita[4:-4]

        for x in range(0, len(list1) - 1):
            if list1[x] + 1 == list1[x + 1]:
                final_list1.remove(list1[x + 1])

        for x in range(0, len(final_list1) - 1):
            if counter_stop != 0 and counter_stop != 21:
                counter_order += 1
                last_step()

            counter_stop += 1

            if counter_order >= 30:
                break

    print(f"{act} time {int(time.time() - start_time)} seconds")
