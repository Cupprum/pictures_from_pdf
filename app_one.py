from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import numpy as np
import time
import os


name_of_file = input('nazov : ')

start_time = time.time()
counter_pack = 1
actual_maturita = PdfFileReader(open(name_of_file, 'rb'))
lenght = actual_maturita.getNumPages() - 2

os.system(f"mkdir IMG/{name_of_file[:-4]}")

for alfa in range(1, lenght, 2):
    im1 = convert_from_path(name_of_file)[alfa]
    im2 = convert_from_path(name_of_file)[alfa + 1]

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

    act = name_of_file[:-4]

    for x in range(0, len(list1) - 1):
        if list1[x] + 1 == list1[x + 1]:
            final_list1.remove(list1[x + 1])

    for x in range(0, len(final_list1) - 1):
        counter_in_pack += 1

        zadanie = im1.crop(
            (195, final_list1[x] + 5, 1520, final_list1[x + 1] - 5))
        zadanie.save(
            f"IMG/{act}/{act}_{counter_pack}_{counter_in_pack}.jpg")

    for x in range(0, len(list2) - 1):
        if list2[x] + 1 == list2[x + 1]:
            final_list2.remove(list2[x + 1])

    for x in range(0, len(final_list2) - 1):
        counter_in_pack += 1

        zadanie = im2.crop(
            (195, final_list2[x] + 5, 1520, final_list2[x + 1] - 5))
        zadanie.save(
            f"IMG/{act}/{act}_{counter_pack}_{counter_in_pack}.jpg")

    print(f"pic done in {(time.time() - start_time)}")
    counter_pack += 1

print(f"--- {(time.time() - start_time)} seconds ---")
