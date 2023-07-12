import pyautogui
import os
import time

import subprocess

executable_path = r"C:\Program Files (x86)\Power Automate Desktop\PAD.Console.Host.exe"
subprocess.call([executable_path])

time.sleep(1)

X=571
Y=252

pyautogui.click(X,Y)