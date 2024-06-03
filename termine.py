# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:13:13 2024

@author: YiQianRong
"""
import pyautogui
import time

from PIL import ImageGrab
import pyautogui
import numpy as np
import matplotlib.pyplot as plt

def is_region_red(region):
    # Capture the region of the screen
    screenshot = ImageGrab.grab(bbox=region)
    # Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)
    
    plt.imshow(screenshot_np)
    plt.title("Captured Region")
    plt.axis("off")  # Hide axes
    plt.show()
    # Get the red channel of the screenshot
    red_channel = screenshot_np[:, :, 0]
    green_channel = screenshot_np[:, :, 1]
    blue_channel = screenshot_np[:, :, 2]
    # Define a threshold for considering a pixel as "red"
    # Check if the majority of pixels in the region are red
    is_red = np.mean((red_channel > green_channel ) & (red_channel > blue_channel))
    return is_red > 0.8


while (1):
    second_screen_x = 102  # 1920 is the width of the primary screen
    second_screen_y = 68
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(1)
    
    second_screen_x = 268  # 1920 is the width of the primary screen
    second_screen_y = 435
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(0.2)
    
    
    second_screen_x = 494  # 1920 is the width of the primary screen
    second_screen_y = 530
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(0.2)
    
    second_screen_x = 494  # 1920 is the width of the primary screen
    second_screen_y = 545
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(0.1)
    
    second_screen_x = 615  # 1920 is the width of the primary screen
    second_screen_y = 820
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(1)
    
    second_screen_x = 615  # 1920 is the width of the primary screen
    second_screen_y = 560
    
    # Move the mouse to the specified coordinates on the second screen
    pyautogui.moveTo(second_screen_x, second_screen_y)
    
    # Click the mouse at the current position
    pyautogui.click()
    
    time.sleep(1)
    
    if is_region_red((158,1340-1080,770,1430-1080)):
        print("free slots are not available")
    else:
        print("congratulation!")
        break;
    time.sleep(30)