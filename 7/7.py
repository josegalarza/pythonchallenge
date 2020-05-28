#!/usr/bin/env python
# Python Challenge - Level 7
# http://www.pythonchallenge.com/pc/def/oxygen.html

# pipenv install pillow

import os

from PIL import Image

image = Image.open(
    os.path.join(
        os.getcwd(),
        "oxygen.png"
    )
)

print(
  "Any metadata?",
  image._getexif()
)

print(
  "Any info?",
  image.info
)


# Checking other data
print("Dimension:", image.size)
print("Bands:", image.getbands())


# Reading all pixels
print("Reading 'pixels' as a 2 dimensional (x,y) list of pixels (R,G,B,A,)...")
pixels = []
line = []
x,y = image.size
c = 0
for pixel in image.getdata():
    line.append(pixel)
    c += 1
    if c%x == 0:  # end of the line
        pixels.append(line)
        line = []
print("done")


print("Looking for the 'line' that repeats itself in the image...")
for i in range(len(pixels)):
    if i == y-1:
    	break
    else:
        this_line = pixels[i]
        next_line = pixels[i+1]

        if this_line[:int(x/2)] == next_line[:int(x/2)]:
            print("Found it!", i)
            line = this_line
            break
print("done - is line:", i)


print("Summary - counting the common pixels in the line...")
summary = []
for i in range(len(line)):
    print(i, summary)
    if i == 0:
        summary.append((line[i], 1))
        continue
    elif i == x-1:
        break
    else:
        print(summary)
        print(summary[:-1])
        pix, count = summary[-1]
        if line[i] == pix:
            summary[-1] = (pix, count+1)
        else:
            summary.append((line[i], 1))

print("Summary:")
for pix, count in summary:
    print(count, pix)
    pass


print("Translating line to ASCII...")
translate = ""
for pix, count in summary:
    r,g,b,a = pix
    translate += chr(r)
print(translate)


print("Final solution:")
solution_code = [105, 10, 16, 101, 103, 14, 105, 16, 121]
solution = ""
for i in solution_code:
    solution += chr(i)
print(solution)
