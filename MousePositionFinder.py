import pyautogui
import time
from PIL import ImageGrab


for i in range(100):
    pixelRGB = ImageGrab.grab().getpixel(pyautogui.position())
    print(pyautogui.position(), ' - ', pixelRGB)
    time.sleep(2)
