import pyautogui



pyautogui.rightClick(x=10, y=10)


pyautogui.typewrite(['V'])

 # Вставить
pyautogui.hotkey('ctrlleft','I')

 # Это также может быть вставлено
# pyautogui.keyDown('ctrl')
# pyautogui.press('v')
# pyautogui.keyUp('ctrl')

 # Подтвердите сохранение
# pyautogui.press('enter')