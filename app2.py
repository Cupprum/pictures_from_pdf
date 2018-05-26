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
    counter_pack = 1
    actual_maturita = PdfFileReader(open(f"{maturita}", 'rb'))
    lenght = actual_maturita.getNumPages() - 2

    os.system(f"mkdir IMG/{maturita[4:-4]}")

    for alfa in range(1, lenght, 2):
        im1 = convert_from_path(maturita)[alfa]
        im2 = convert_from_path(maturita)[alfa + 1]

        p1 = np.array(im1)
        p2 = np.array(im2)

        list1 = []
        line1 = 0

        list2 = []
        line2 = 0

        counter_in_pack = -1

        for x in p1:
            list_docastny = ""
            counter = 0
            for y in range(400, 1300):
                if str(x[y]) == "[255 255 255]":
                    break
                else:
                    counter += 1
            if counter >= 900:
                list1.append(line1)
            line1 += 1

        for x in p2:
            list_docastny = ""
            counter = 0
            for y in range(400, 1300):
                if str(x[y]) == "[255 255 255]":
                    break
                else:
                    counter += 1
            if counter >= 900:
                list2.append(line2)
            line2 += 1

        final_list1 = list1[:]
        final_list2 = list2[:]

        act = maturita[4:-4]

        for x in range(0, len(list1) - 1):
            if list1[x] + 1 == list1[x + 1]:
                final_list1.remove(list1[x + 1])

        for x in range(0, len(final_list1) - 1):

            zadanie = im1.crop((133, final_list1[x], 1520, final_list1[x + 1]))

            iterate_foto = np.array(zadanie)

            counter_of_faults = 0

            for y in range(20, len(iterate_foto) - 20, 5):
                actual_line = iterate_foto[y]

                for z in actual_line[300: -300]:
                    print(f"original {z}, moje [255 255 255]")
                    if z != "[255 255 255]":
                        counter_of_faults += 1

            print(counter_of_faults)
            if counter_of_faults > 100:
                counter_in_pack += 1
                zadanie.save(
                    f"IMG/{act}/{act}_{counter_pack}_{counter_in_pack}.jpg")

        for x in range(0, len(list2) - 1):
            if list2[x] + 1 == list2[x + 1]:
                final_list2.remove(list2[x + 1])

        for x in range(0, len(final_list2) - 1):
            zadanie = im2.crop((133, final_list2[x], 1520, final_list2[x + 1]))

            iterate_foto = np.array(zadanie)

            counter_of_faults = 0

            for y in range(20, len(iterate_foto) - 20, 5):
                actual_line = iterate_foto[y]

                for z in actual_line[500: -500]:
                    print(f"original {z}, moje [255 255 255]")
                    if z != "[255 255 255]":
                        counter_of_faults += 1

            print(counter_of_faults)
            if counter_of_faults > 100:
                counter_in_pack += 1
                zadanie.save(
                    f"IMG/{act}/{act}_{counter_pack}_{counter_in_pack}.jpg")

        print(f"{act}_{counter_pack}_{counter_in_pack}")
        print(f"pic done in {(time.time() - start_time)}")
        counter_pack += 1

    print(f"--- {(time.time() - start_time)} seconds ---")
