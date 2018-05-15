from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import numpy as np
import time
import glob


list_maturita = glob.glob(
    'PDF/*.pdf')

maturita = list_maturita[0]

im1 = convert_from_path(maturita)[1]
im2 = convert_from_path(maturita)[2]

p1 = np.array(im1)
p2 = np.array(im2)

list1 = []
line = 0

counter_of_done = 0

for x in p1:
    list_docastny = ""
    counter = 0
    for y in range(133, 1520):
        if str(x[y]) == "[255 255 255]":
            break
        else:
            counter += 1
    if counter > 1386:
        list1.append(line)
    line += 1

list2 = []
line = 0

for x in p2:
    list_docastny = ""
    counter = 0
    for y in range(133, 1520):
        if str(x[y]) == "[255 255 255]":
            break
        else:
            counter += 1
    if counter > 1386:
        list2.append(line)
    line += 1

final_list1 = list1[:]

for x in range(0, len(list1) - 1):
    if list1[x] + 1 == list1[x + 1]:
        final_list1.remove(list1[x + 1])

for x in range(0, len(final_list1) - 1):
    counter_of_done += 1

    zadanie = im1.crop((133, final_list1[x], 1520, final_list1[x + 1]))
    zadanie.save(f"IMG/{maturita[4:-4]}_{counter_of_done}.jpg")

final_list2 = list2[:]

for x in range(0, len(list2) - 1):
    if list2[x] + 1 == list2[x + 1]:
        final_list2.remove(list2[x + 1])

for x in range(0, len(final_list2) - 1):
    counter_of_done += 1

    if counter_of_done == 10:
        break

    zadanie = im2.crop((133, final_list2[x], 1520, final_list2[x + 1]))
    zadanie.save(f"IMG/{maturita[4:-4]}_{counter_of_done}.jpg")


"""
for maturita in list_maturita:
    start_time = time.time()
    counter_of_done = 0

    actual_maturita = PdfFileReader(open(f"{list_maturita[0]}", 'rb'))
    lenght = actual_maturita.getNumPages() - 3

    for alfa in range(1, lenght):
        im = convert_from_path(maturita)[alfa]

        p = np.array(im)
        list1 = []
        line = 0

        for x in p:
            list_docastny = ""
            counter = 0
            for y in range(133, 1520):
                if str(x[y]) == "[255 255 255]":
                    break
                else:
                    counter += 1
            if counter > 1386:
                list1.append(line)
            line += 1

        final_list = list1[:]

        for x in range(0, len(list1) - 1):
            if list1[x] + 1 == list1[x + 1]:
                final_list.remove(list1[x + 1])

        for x in range(0, len(final_list) - 1):
            counter_of_done += 1

            zadanie = im.crop((133, final_list[x], 1520, final_list[x + 1]))
            zadanie.save(f"IMG/{maturita[4:-4]}_{counter_of_done}.jpg")

        print(f"pic done in {(time.time() - start_time)}")
    print(f"--- {(time.time() - start_time)} seconds ---")
"""