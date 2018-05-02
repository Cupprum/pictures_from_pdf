from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import time


start_time = time.time()

for alfa in range(1, 16):
    im = convert_from_path('doc1.pdf')[alfa]

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

    txt = open('blackandwhite.txt', 'r').readlines()
    list1 = []

    line = 0
    for x in txt:
        counter = 0

        for y in range(400, 800):
            if x[y] == 'b':
                counter += 1
            else:
                break
        if counter > 399:
            list1.append(line)
        line += 1

    final_list = list1[:]

    for x in range(0, len(list1) - 1):
        if list1[x] + 1 == list1[x + 1]:
            final_list.remove(list1[x + 1])

    print(f"final_list {final_list}")

    for x in range(0, len(final_list) - 1):
        zadanie = im.crop((133, final_list[x], 1520, final_list[x + 1]))
        zadanie.save(f"foto{alfa + x}.jpg")

print("--- %s seconds ---" % (time.time() - start_time))
