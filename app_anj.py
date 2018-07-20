from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import numpy as np
import time
import glob
import os


list_maturita = glob.glob(
    'PDF/*.pdf')

for maturita in list_maturita:
    start_time = time.time()
    lenght = PdfFileReader(open(f"{maturita}", 'rb')).getNumPages() - 1

    os.system(f"mkdir IMG/{maturita[4:-4]}")

    counter_all = 0

    for alfa in range(1, lenght):
        im = convert_from_path(maturita)[alfa]
        p = np.array(im)

        list1 = []
        line1 = 0

        for x in p:
            counter = 0

            for y in range(400, 1300):
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
            counter_all += 1

            zadanie = im.crop(
                (167, final_list1[x] + 5, 1553, final_list1[x + 1] - 5))
            zadanie.save(
                f"IMG/{act}/{act}_{counter_all}.jpg")

        print(f"pic done in {(time.time() - start_time)}")

    print(f"--- {(time.time() - start_time)} seconds ---")
