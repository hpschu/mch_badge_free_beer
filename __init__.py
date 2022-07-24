import display as d
import buttons
import mch22
import sys
import time
import audio

APP_PATH = "/".join(__file__.split("/")[:-1])
sys.path.append(APP_PATH)
from rickfile import *

def reboot(pressed):
  if pressed:
    mch22.exit_python()

nricks = len(ricks)

i = 0
start_time = time.ticks_ms()

d.drawFill(0x000000)
channel_id = audio.play("%s/%s" % (APP_PATH, "background.mp3"), volume=130, loop=True)

def showFrame(ricks, nricks, i):
    d.drawPng(59, 0, ricks[i])
    d.flush()
    i += 1
    if i == nricks - 1:
        i = 0
        start_time = time.ticks_ms()
    return i
    
while time.ticks_diff(time.ticks_ms(), start_time) < 1000:
    print() # This does nothing :)
start_time = time.ticks_ms()

while True:
    if time.ticks_diff(time.ticks_ms(), start_time) > 50:
        start_time = time.ticks_ms()
        i = showFrame(ricks, nricks, i)
