# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import touchio
import digitalio

from adafruit_circuitplayground import cp

capPins = (board.A1, board.A2, board.A5)

touchPad = []
for i in range(3):
    touchPad.append(touchio.TouchIn(capPins[i]))

editmode = False
color = [255, 0, 0]
allcolors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (75, 0, 130), (148, 0, 211), (75, 50, 130), (0, 0, 255), (0, 255, 0)]


i = 0
smooth = True

while True:

    if smooth:
        print("smooth")
        print(color[0])
        cp.pixels[0:10] = [(color[0], color[1], color[2])]*10
        if color[0] > allcolors[i][0]:
            color[0] -= 1
        elif color[0] < allcolors[i][0]:
            color[0] += 1

        if color[1] > allcolors[i][1]:
            color[1] -= 1
        elif color[1] < allcolors[i][1]:
            color[1] += 1

        if color[2] > allcolors[i][2]:
            color[2] -= 1
        elif color[2] < allcolors[i][2]:
            color[2] += 1

        if (color[0], color[1], color[2]) == allcolors[i]:

            i += 1
        if i >= 9:
            i = 0
        time.sleep(0.01)
    if touchPad[1].value:
        if smooth == False:
            smooth = True
        else:
            smooth = False
        time.sleep(0.5)
    elif touchPad[0].value:
        smooth = False
        print(1)
        if editmode == True:
            cp.pixels[0:10] = [allcolors[i]]*10
            i += 1
            if i >= 9:
                i = 0
        if editmode == False:
            if cp.pixels[0] == (255, 0, 0):
                cp.pixels[0] = (0, 0, 0)
                cp.pixels[1] = (0, 0, 0)
                cp.pixels[2] = (0, 0, 0)
                cp.pixels[3] = (0, 0, 0)
                cp.pixels[4] = (0, 0, 0)
                cp.pixels[5] = (0, 0, 0)
                cp.pixels[6] = (0, 0, 0)
                cp.pixels[7] = (0, 0, 0)
                cp.pixels[8] = (0, 0, 0)
                cp.pixels[9] = (0, 0, 0)
            else:
                cp.pixels[0] = (255, 0, 0)
                cp.pixels[1] = (255, 127, 0)
                cp.pixels[2] = (255, 255, 0)
                cp.pixels[3] = (0, 255, 0)
                cp.pixels[4] = (0, 0, 255)
                cp.pixels[5] = (75, 0, 130)
                cp.pixels[6] = (148, 0, 211)
                cp.pixels[7] = (75, 50, 130)
                cp.pixels[8] = (0, 0, 255)
                cp.pixels[9] = (0, 255, 0)
        time.sleep(0.5)
    elif touchPad[2].value:
        smooth = False
        print(0)
        if editmode == False:
            editmode = True
        else:
            editmode = False
        time.sleep(0.5)
cp.pixels.show()

