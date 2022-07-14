import pyautogui, time

time.sleep(5); f = open("beemovie.txt", "r")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
