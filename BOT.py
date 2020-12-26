import pyautogui
import time
import random


file= open("spam.txt","r").read()
file= file.splitlines()



while True:
    pyautogui.typewrite(random.choice(file))
    pyautogui.press("Enter")
    
