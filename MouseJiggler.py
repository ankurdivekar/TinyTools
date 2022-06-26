import pyautogui
import time
import sys
import msvcrt
from datetime import datetime
from pynput.keyboard import Key, Listener


def on_press(key):

    global sec_counter
    global init_pos
    sec_counter = 0
    # init_pos = pyautogui.position()

    # print("{0} pressed".format(key))
    # if key == Key.f8:
    #     return False
    # print("sec counter reset")


# def on_release(key):
#     print("{0} release".format(key))


def wiggle_mouse(init_pos):

    pyautogui.moveTo(1, 995)
    pyautogui.click()
    # time.sleep(1)
    pyautogui.moveTo(1, 997)
    # time.sleep(1)
    pyautogui.click()
    # pyautogui.moveTo(1, 1079)
    pyautogui.moveTo(init_pos)
    # time.sleep(1)
    pyautogui.click()
    print(f"Movement made at {datetime.now().time():%I:%M:%S %p}")


pyautogui.FAILSAFE = False
check_delay_sec = 118

global sec_counter
# global init_pos

sec_counter = 0
listener = Listener(
    on_press=on_press,
    # on_release=on_release,
)
listener.start()
print("Monitoring activity...")

while True:
    init_pos = pyautogui.position()
    time.sleep(1)
    sec_counter += 1
    # print(f"{sec_counter = }")
    new_pos = pyautogui.position()

    if init_pos == new_pos:
        if sec_counter >= check_delay_sec:
            # print("Moving mouse")
            wiggle_mouse(init_pos)
            sec_counter = 0
    else:
        sec_counter = 0
