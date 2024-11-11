import pyautogui

count = 0
exact = 1000

while count < exact:
    pyautogui.typewrite("python pe focus kro")
    pyautogui.press('enter')

    count = count + 1