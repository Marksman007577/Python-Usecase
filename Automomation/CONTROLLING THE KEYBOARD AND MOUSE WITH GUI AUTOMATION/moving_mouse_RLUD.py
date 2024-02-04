import pyautogui

# Moving the mouse
for i in range(10):
    pyautogui.moveTo(100, 0, duration=.25)
    pyautogui.moveTo(0, 100, duration=.25)
    pyautogui.moveTo(-100, 0, duration=.25)
    pyautogui.moveTo(0, -100, duration=.25)
