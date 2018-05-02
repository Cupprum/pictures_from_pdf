from PIL import Image

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

print(list1)
final_list = list1[:]

for x in range(0, len(list1) - 1):
    if list1[x] + 1 == list1[x + 1]:
        final_list.remove(list1[x + 1])

print(final_list)

original = Image.open('final.bmp')
zadanie = original.crop((133, final_list[0], 1520, final_list[1]))
zadanie.save('ostihana.jpg')
