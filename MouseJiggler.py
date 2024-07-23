import pyautogui
import time
import sys
import msvcrt
from datetime import datetime
from pynput.keyboard import Key, Listener
from random import randint
from pynput import mouse


def on_mouse_activity(x, y):
    global sec_counter
    sec_counter = 0
    # print("sec counter reset")


def on_keyboard_press(key):

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


def wiggle_mouse(init_pos, screen_width, screen_height):
    global sec_counter
    move_duration = 0.1

    for i in range(5):
        if sec_counter >= check_delay_sec:
            random_x = randint(0, screen_width)
            random_y = randint(0, screen_height)
            pyautogui.moveTo(random_x, random_y, duration=move_duration, tween=pyautogui.easeInOutQuad)
        else:
            return
    pyautogui.moveTo(1350, 1050, duration=move_duration, tween=pyautogui.easeInOutQuad)
    # time.sleep(1)
    pyautogui.click()

    # pyautogui.moveTo(1340, 1050, duration=move_duration)
    # pyautogui.click()
    # # time.sleep(1)

    # # pyautogui.moveTo(1, 1079),
    # pyautogui.moveTo(init_pos)
    # time.sleep(1)
    # pyautogui.click()
    print(f"Movement {movement_counter} made at {datetime.now().time():%I:%M:%S %p}")


pyautogui.FAILSAFE = False
check_delay_sec = 110

global sec_counter
global movement_counter
# global init_pos

sec_counter = 0
movement_counter = 0
keyboard_listener = Listener(
    on_press=on_keyboard_press,
    # on_release=on_release,
)
keyboard_listener.start()

mouse_listener = mouse.Listener(
    on_move=on_mouse_activity,
    on_click=on_mouse_activity,
    on_scroll=on_mouse_activity,
)
mouse_listener.start()

# print("Monitoring activity...")
screenWidth, screenHeight = pyautogui.size()

print(f"Screen width: {screenWidth}, Screen height: {screenHeight}")

while True:
    init_pos = pyautogui.position()
    time.sleep(1)
    sec_counter += 1
    # print(f"{sec_counter = }")
    new_pos = pyautogui.position()

    if init_pos == new_pos:
        if sec_counter >= check_delay_sec:
            movement_counter += 1
            # print(f"Movement {movement_counter}")
            wiggle_mouse(init_pos, screen_width=screenWidth, screen_height=screenHeight)
            sec_counter = 0
    else:
        sec_counter = 0
