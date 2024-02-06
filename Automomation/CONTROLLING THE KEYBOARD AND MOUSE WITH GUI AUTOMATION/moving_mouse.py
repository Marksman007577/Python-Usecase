import pyautogui

# obtain the screen resolution
wh = pyautogui.size()
print(wh[0])
print(wh[1])

# Moving the mouse
for i in range(10):
    pyautogui.moveTo(100, 100, duration=.25)
    pyautogui.moveTo(200, 100, duration=.25)
    pyautogui.moveTo(200, 200, duration=.25)
    pyautogui.moveTo(100, 200, duration=.25)

# Scrolling mouse
pyautogui.scroll(200)