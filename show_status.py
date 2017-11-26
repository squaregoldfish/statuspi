#!/usr/bin/python

import random
import time
import datetime
from Adafruit_LED_Backpack import AlphaNum4
from Adafruit_LED_Backpack import BicolorMatrix8x8

MATRIX_ADDRESS = 0x74
ALPHA_ADDRESS = 0x70
I2C_BUS = 1
BRIGHTNESS = 5

ALPHA_LETTERS = ["A", "T", "R", "P", "H", "M", "Z", "I"]
ALPHA_FILES = ["rtm_all.txt", "rtm_longestoverdue.txt", "feedly_oldest.txt", "oldest_podcast.txt", "mp3_length.txt", "mp3_length_m.txt", "mp3_size.txt", "images_to_process.txt"]

WEATHER_CAM_FLAG = 1
SQUAREGOLDFISH_FLAG = 1 << 1
SQUAREGOLDFISH_COMMENT_FLAG = 1 << 2
LWC_FLAG = 1 << 3
LWC_GRUNT_FLAG = 1 << 4

WEATHER_CAM_SYMBOL = [[0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,6],[7,5],[6,4],[6,3],[5,4],[5,3],[7,2],[7,1],[6,0],[5,0],[4,0],[3,0],[2,0],[1,0],[0,0]]

SQUAREGOLDFISH_SYMBOL = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,6],[2,6],[3,5],[3,4],[3,3],[3,2],[4,1],[5,1],[6,1],[7,2],[7,3],[7,4],[7,5],[7,6]]

SQUAREGOLDFISH_COMMENT_SYMBOL = [[7,2],[7,1],[7,0],[0,4],[0,5],[0,6],[0,7],[1,7],[2,7],[2,6],[2,5],[2,4],[3,4],[4,4],[4,5],[4,6],[4,7],[7,3],[6,3],[5,3],[4,3],[3,3],[3,2],[3,1],[3,0]]

SQUAREGOLDFISH_GRUNT_SYMBOL = [[7,2],[7,1],[7,0],[0,4],[0,5],[0,6],[0,7],[1,7],[2,7],[2,6],[2,5],[2,4],[3,4],[4,4],[4,5],[4,6],[4,7],[5,1],[5,0],[6,0],[7,3],[6,3],[5,3],[4,3],[3,3],[3,2],[3,1],[3,0]]

LWC_SYMBOL = [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[7,4],[7,3],[7,2],[7,1]]

LWC_GRUNT_SYMBOL = [[0,7],[1,7],[2,7],[3,7],[4,7],[4,6],[4,5],[5,1],[5,0],[6,0],[7,0],[7,1],[7,2],[7,3],[6,3],[5,3],[4,3],[3,3],[3,2],[3,1],[3,0]]

LWC_PING_SYMBOL = [[0,7],[1,7],[2,7],[3,7],[4,7],[4,6],[4,5],[5,2],[5,1],[5,0],[4,0],[3,0],[3,1],[3,2],[3,3],[4,3],[5,3],[6,3],[7,3]]

LWC_MAINTENANCE_SYMBOL = [[0,7],[1,7],[2,7],[3,7],[4,7],[4,6],[4,5],[7,3],[6,3],[5,3],[4,3],[5,2],[5,1],[4,0],[5,0],[6,0],[7,0]]

SEADATANET_SYMBOL = [[4,3],[5,3],[6,3],[7,3],[5,2],[6,1],[7,0],[6,0],[5,0],[4,0],[0,4],[0,5],[0,6],[0,7],[1,7],[2,7],[2,6],[2,5],[2,4],[3,4],[4,4],[4,5],[4,6],[4,7]]

SOCAT_SYMBOL = [[4,3],[5,3],[6,3],[7,3],[7,2],[7,1],[7,0],[6,0],[5,0],[4,0],[4,1],[4,2],[4,3],[0,4],[0,5],[0,6],[0,7],[1,7],[2,7],[2,6],[2,5],[2,4],[3,4],[4,4],[4,5],[4,6],[4,7]]

POSEIDON_SYMBOL = [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[0,4],[0,3],[1,2],[2,1],[3,1],[4,2],[4,3],[4,4]]

QUINCE_SYMBOL = [[7,0],[6,1],[5,2],[4,3],[6,2],[5,1],[4,1],[3,1],[2,1],[1,2],[1,3],[1,4],[1,5],[2,6],[3,6],[4,6],[5,6],[6,5],[6,4],[6,3]]

ICOS_LABELLING_SYMBOL = [[0,7],[0,6],[0,5],[1,6],[2,6],[3,6],[4,7],[4,6],[4,5],[3,3],[4,3],[5,3],[6,3],[7,3],[7,2],[7,1]]

GLODAP_SYMBOL = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[7,5],[7,4],[7,3],[7,2],[7,1],[6,1],[5,1],[4,1],[4,2],[4,3]]

#####################################################################################

def calcStatus():
    status = list()
    if getWebcamStatus() == 1:
        status.append(WEATHER_CAM_SYMBOL)

    if getSquareGoldfishComments() == 1:
        status.append(SQUAREGOLDFISH_COMMENT_SYMBOL)
  
    if getNumberFromFile("square_goldfish.txt") == 1:
        status.append(SQUAREGOLDFISH_SYMBOL)

    if getNumberFromFile("square_goldfish_grunt.txt") == 1:
        status.append(SQUAREGOLDFISH_GRUNT_SYMBOL)

    if getNumberFromFile("lwc_grunt.txt") == 1:
        status.append(LWC_GRUNT_SYMBOL)

    if getNumberFromFile("long_webcam_main_site.txt") == 1:
        status.append(LWC_SYMBOL)

    if getNumberFromFile("lwc_maintenance.txt") == 1:
        status.append(LWC_MAINTENANCE_SYMBOL)

    if getNumberFromFile("lwc_ping.txt") == 1:
        status.append(LWC_PING_SYMBOL)

    if getNumberFromFile("poseidon.txt") == 1:
        status.append(POSEIDON_SYMBOL)

    if getNumberFromFile("seadatanet.txt") == 1:
        status.append(SEADATANET_SYMBOL)

    if getNumberFromFile("socat.txt") == 1:
        status.append(SOCAT_SYMBOL)

    if getNumberFromFile("quince.txt") == 1:
        status.append(QUINCE_SYMBOL)

    if getNumberFromFile("icos_labelling.txt") == 1:
        status.append(ICOS_LABELLING_SYMBOL)

    if getNumberFromFile("glodap.txt") == 1:
        status.append(ICOS_LABELLING_SYMBOL)

    return status

def drawBinary(display, x, y, count):
  if count == 9:
    display.set_pixel(x, y, BicolorMatrix8x8.RED)
  elif count > 4:
    display.set_pixel(x, y, BicolorMatrix8x8.YELLOW)
  elif count >= 1:
    display.set_pixel(x, y, BicolorMatrix8x8.GREEN)
  elif count == 0:
    display.set_pixel(x, y, BicolorMatrix8x8.OFF)

  if count == 9:
    display.set_pixel(x, y-1, BicolorMatrix8x8.RED)
  elif count > 5:
    display.set_pixel(x, y-1, BicolorMatrix8x8.YELLOW)
  elif count >= 2:
    display.set_pixel(x, y-1, BicolorMatrix8x8.GREEN)
  elif count < 2:
    display.set_pixel(x, y-1, BicolorMatrix8x8.OFF)

  if count == 9:
    display.set_pixel(x-1, y, BicolorMatrix8x8.RED)
  elif count > 6:
    display.set_pixel(x-1, y, BicolorMatrix8x8.YELLOW)
  elif count >= 3:
    display.set_pixel(x-1, y, BicolorMatrix8x8.GREEN)
  elif count < 3:
    display.set_pixel(x-1, y, BicolorMatrix8x8.OFF)

  if count == 9:
    display.set_pixel(x-1, y-1, BicolorMatrix8x8.RED)
  elif count > 7:
    display.set_pixel(x-1, y-1, BicolorMatrix8x8.YELLOW)
  elif count >= 4:
    display.set_pixel(x-1, y-1, BicolorMatrix8x8.GREEN)
  elif count < 4:
    display.set_pixel(x-1, y-1, BicolorMatrix8x8.OFF)


def drawAlphaText(display, alpha_index):
    number = getNumberFromFile(ALPHA_FILES[alpha_index])

    text = ALPHA_LETTERS[alpha_index]
    point = -1

    if number < 10:
        text = text + "  " + str(number)
    elif number < 100:
      text = text + " " + str(number)
    elif number < 1000:
        text = text + str(number)
    elif number < 10000:
        text = text + str(number)[0:3]
        point = 1
    elif number < 100000:
        text = text + str(number)[0:3]
        point = 2
    else:
        text = text + "***"

    display.print_str(text)

    for i in range(0, 3):
        display.set_decimal(i, point == i)

def drawCombinedCountLeft(display, red, orange, green):
    pixelCount = 0
    state = "RED"
    next_color = "ORANGE"

    if orange == 0:
        if green > 0:
          next_color = "GREEN"
        else:
          next_color = "FINISH_LINE"

    for y in range(7,-1,-1):
        for x in range(7,3,-1):
            if state == "FINISH_LINE":
                display.set_pixel(y, x, BicolorMatrix8x8.OFF)
            else:
                pixelCount = pixelCount + 1

            if state == "RED":
                if pixelCount <= red:
                    display.set_pixel(y, x, BicolorMatrix8x8.RED)

                if pixelCount == red:
                    state = "FINISH_LINE"

            elif state == "ORANGE":
                if pixelCount <= orange:
                    display.set_pixel(y, x, BicolorMatrix8x8.YELLOW)

                if pixelCount == orange:
                    state = "FINISH_LINE"

            elif state == "GREEN":
                if pixelCount <= green:
                    display.set_pixel(y, x, BicolorMatrix8x8.GREEN)

                if pixelCount == green:
                    state = "FINISH_LINE"

        if state == "FINISH_LINE":
            state = next_color
            pixelCount = 0
        
        if state == "RED":
            if orange > 0:
                next_color = "ORANGE"
            elif green > 0:
                next_color = "GREEN"
            else:
                next_color = "FINISH_LINE"

        elif state == "ORANGE":
            if green > 0:
                next_color = "GREEN"
            else:
                next_color = "FINISH_LINE"
        else:
            next_color = "FINISH_LINE"



def drawCount(display, col, count):
  units = count % 10
  temp = count - units
  tens = (temp % 100) / 10
  temp = temp - (tens * 10)
  hundreds = (temp / 100)
  drawBinary(display, 7, col, units)
  drawBinary(display, 5, col, tens)
  drawHundreds(display, col, hundreds)


def drawHundreds(display, col, hundreds):
  currentPixelX = col
  currentPixelY = 3
  while currentPixelY >= 0:
    if hundreds > 0:
      display.set_pixel(currentPixelY, currentPixelX, BicolorMatrix8x8.RED)
      hundreds = hundreds - 1
    else:
      display.set_pixel(currentPixelY, currentPixelX, BicolorMatrix8x8.OFF)

    if currentPixelX == col:
      currentPixelX = currentPixelX - 1
    else:
      currentPixelX = col
      currentPixelY = currentPixelY - 1

def drawCounts(display, overdue, today, impending, count1, count2):
  drawCombinedCountLeft(display, overdue, today, impending)
  drawCount(display, 3, count1)
  drawCount(display, 1, count2)

def drawSymbol(display, points):
  display.clear()
  for point in points:
    display.set_pixel(point[0], point[1], BicolorMatrix8x8.RED)
  

def getNumberFromFile(filename):
  f = open("data/%s" % filename, "r")
  countString = f.read().strip()
  f.close()
  if countString == '':
    countString = "0";

  return int(countString)

def getSquareGoldfishComments():
  result = 0
  commentCount = getNumberFromFile("moderation_count.php")
  commentCount = commentCount + getNumberFromFile("spam_count.php")
  if commentCount != 0:
    result = 1

  return result

def getWebcamStatus():
  result = 0
  f = open("data/webcamStatus", "r")
  ws = f.readline().strip()
  if ws == '1':
    result = 1

  return result



#####################################################################################

# Initialise displays
matrix = BicolorMatrix8x8.BicolorMatrix8x8(address=MATRIX_ADDRESS, busnum=I2C_BUS)
matrix.begin()
matrix.set_brightness(BRIGHTNESS)

alpha = AlphaNum4.AlphaNum4(address=ALPHA_ADDRESS, busnum=I2C_BUS)
alpha.begin()
alpha.set_brightness(BRIGHTNESS)

# Scroll a message across the display
current_alpha = 0
status = list()
current_status = 0
try:
    while True:

        drawAlphaText(alpha, current_alpha)

        current_alpha += 1
        if current_alpha == len(ALPHA_LETTERS):
            current_alpha = 0

        status = calcStatus()
        if len(status) > 0:
            if current_status >= len(status):
                current_status = 0
            drawSymbol(matrix, status[current_status])
            current_status += 1
            if current_status == len(status):
                current_status = 0

        else:
            overdue = getNumberFromFile("rtm_overdue.txt")
            today = getNumberFromFile("rtm_today.txt")
            impending = getNumberFromFile("rtm_impending.txt")
            reading = getNumberFromFile("feedly_count.txt")
            mp3Count = getNumberFromFile("mp3_count.txt")
            drawCounts(matrix, overdue, today, impending, reading, mp3Count)

        matrix.write_display()
        alpha.write_display()

        time.sleep(5)

except Exception, e:
    print str(e)
    f = open("statusError", "w")
    f.write(str(e))
    f.close()
