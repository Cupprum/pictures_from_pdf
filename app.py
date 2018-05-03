from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import time


start_time = time.time()
counter_of_done = 0

for alfa in range(1, 17):
    im = convert_from_path('doc1.pdf')[alfa]

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

    print(f"done pic analysis {(time.time() - start_time)}")

    final_list = list1[:]

    for x in range(0, len(list1) - 1):
        if list1[x] + 1 == list1[x + 1]:
            final_list.remove(list1[x + 1])

    print(f"final_list {final_list}")

    for x in range(0, len(final_list) - 1):
        counter_of_done += 1

        zadanie = im.crop((133, final_list[x], 1520, final_list[x + 1]))
        zadanie.save(f"foto{counter_of_done}.jpg")

    print(f"pic done in {(time.time() - start_time)}")
print(f"--- {(time.time() - start_time)} seconds ---")
