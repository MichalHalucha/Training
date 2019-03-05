import time
import pyautogui

def rusz():
    pyautogui.click(1100, 1100)
    pyautogui.moveTo(100, 150)
    time.sleep(20)
    pyautogui.click(1100, 1100)
    pyautogui.moveTo(100, 150)



if __name__ == '__main__':

    for x in range(10):
        rusz()
