import os
import time
import random
import pyautogui
import subprocess
from selenium import webdriver

words = "The admin will click on users button on the sidebar The system will then display users page The admin will then be able to create roles for users"

pyautogui.FAILSAFE = False

PATH = 'C:\Program Files (x86)\chromedriver.exe'

def wait(delay):
    time.sleep(delay)

def move_mouse():
    for i in range(0, 9):
        pyautogui.press('shift')

    for i in range(0, 120):
        pyautogui.press('down')

    for i in range(0, 80):
        pyautogui.moveTo(0, i * 7)

    for i in range(0, 120):
        pyautogui.press('up')

def browser():
    driver = webdriver.Chrome(PATH)
   

    driver.get('http://127.0.0.1:8000/')
    driver.maximize_window()
    wait(2)

    username = driver.find_element_by_xpath("//input[@id='email']")
    username.send_keys("rahulkhannafree@gmail.com")
    password = driver.find_element_by_xpath("//input[@id='password']")
    password.send_keys("11111111")

    wait(2)

    submit = driver.find_element_by_xpath("//input[@value='Login']")
    submit.click()

    wait(15)

    driver.close()

# def notepad():
#     os.system("notepad.exe")
#     wait(3)
#     pyautogui.write(words, interval=0.1)

while True:
    wait(4)
    # notepad()
    move_mouse()
    browser()
    wait(4)