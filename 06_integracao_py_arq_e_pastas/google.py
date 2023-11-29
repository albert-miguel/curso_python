import pyautogui
import time

pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('google chrome')
pyautogui.press('enter')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
while not pyautogui.locateOnScreen('mail.png'):
  time.sleep(1)
x, y = pyautogui.locateCenterOnScreen('app_google.png')
pyautogui.click(x, y)

x, y, largura, altura = pyautogui.locateOnScreen('contatos.png')
pyautogui.click(x + largura / 2, y + altura / 2)


# x, y = pyautogui.locateCenterOnScreen('mail.png')
# pyautogui.click(x, y)
# pyautogui.click(screenxota)

# x, y = pyautogui.locateCenterOnScreen('mail.png')
# pyautogui.click(x, y)