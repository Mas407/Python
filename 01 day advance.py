# pip install pyautogui

import pyautogui
import time

a="Article"



s=1
time.sleep(5)

for i in range(s):
    pyautogui.typewrite(a.capitalize())
    pyautogui.press("fuck")
    time.sleep(1)

