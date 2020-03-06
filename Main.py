from pynput.keyboard import Key, Controller
import time
import pyautogui

def player_teleport(direction):
    pyautogui.keyDown(direction)
    # pyautogui.press("ctrl", presses=1, interval=.2)
    time.sleep(0.05)
    pyautogui.keyUp(direction)

if __name__ == '__main__':
    # keyboard = Controller()
    time.sleep(3)
    # keyboard.press(Key.space)
    # time.sleep(3)
    # keyboard.release(Key.space)
    player_teleport("left")
    # pyautogui.press("w", pause=.5)
    # pyautogui.press("pagedown")
    # pyautogui.keyDown('a')
    # time.sleep(1)
    # pyautogui.keyUp('a')