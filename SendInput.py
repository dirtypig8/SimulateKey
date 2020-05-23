import ctypes
import time
import pyautogui
import random

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def player_teleport(direction):
    pyautogui.keyDown(direction)
    # pyautogui.press("ctrl", presses=2, interval=.2)
    time.sleep(0.1)
    pyautogui.keyUp(direction)


def ack():
    KEY_Q = 0x10
    KEY_W = 0x11
    KEY_E = 0x12
    KEY_A = 0x1E
    att_count = 0
    left_right_count = 1
    sec = 3
    for n in range(sec):
        print('{}秒後開始'.format(sec - n))
        time.sleep(1)
    while True:
        for i in range(30):
            PressKey(KEY_A)
            ReleaseKey(KEY_A)
            time.sleep(2)
            # player_teleport("left")
            att_count += 1
            print('Loop : {}'.format(att_count))

        if left_right_count % 2 == 1:
            print('left')
            player_teleport("left")
            time.sleep(0.5 * random.random())
        else:
            print('right')
            player_teleport("right")
            time.sleep(0.5 * random.random())
        left_right_count += 1


def auto_wash_red_point():
    Key_1 = 0x02
    Key_0 = 0x0B
    Key_enter = 0x1c
    count = 0

    sleep_time = 0.2

    print(pyautogui.position())

    time.sleep(3)
    while True:
        time.sleep(sleep_time)
        print('count = {}'.format(count))
        print(pyautogui.position())
        pyautogui.rightClick(x=662, y=616)
        pyautogui.click()
        time.sleep(sleep_time)
        pyautogui.rightClick(x=643, y=302)
        pyautogui.click()
        time.sleep(sleep_time)
        pyautogui.rightClick(x=463, y=392)
        pyautogui.click()
        time.sleep(sleep_time)

        if count % 2 == 1:
            pyautogui.rightClick(x=383, y=345)
            pyautogui.click()
        else:
            pyautogui.rightClick(x=426, y=327)
            pyautogui.click()

        time.sleep(sleep_time)
        PressKey(Key_1)
        ReleaseKey(Key_1)
        PressKey(Key_0)
        ReleaseKey(Key_0)
        time.sleep(sleep_time)

        for i in range(3):
            PressKey(Key_enter)
            ReleaseKey(Key_enter)
            time.sleep(sleep_time)

        count += 1

def ack_sock():
    KEY_INS = 0xd2
    KEY_Q = 0x10
    KEY_W = 0x11
    KEY_E = 0x12
    KEY_A = 0x1E
    att_count = 0
    left_right_count = 1
    sec = 3
    for n in range(sec):
        print('{}秒後開始'.format(sec - n))
        time.sleep(1)
    while True:
        for i in range(2):
            PressKey(KEY_INS)
            ReleaseKey(KEY_INS)
            time.sleep(1.2)

        for j in range(60):
            PressKey(KEY_A)
            ReleaseKey(KEY_A)
            time.sleep(0.2)
            # player_teleport("left")
            att_count += 1
            print('Loop : {}'.format(att_count))
        time.sleep(0.5)
        if left_right_count % 2 == 1:
            print('left')
            player_teleport("left")
            time.sleep(0.5 * random.random())
        else:
            print('right')
            player_teleport("right")
            time.sleep(0.5 * random.random())
        left_right_count += 1

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
if __name__ == '__main__':
    # while True:
    #     print(pyautogui.position())
    sleep_time = 0.2
    time.sleep(2)
    while True:
        pyautogui.click(clicks=2, x=140, y=95)
        time.sleep(sleep_time)
        pyautogui.click(x=719, y=378)
        time.sleep(sleep_time)
        pyautogui.click(x=719, y=361)
        time.sleep(sleep_time)
        pyautogui.click(x=661, y=447)
        time.sleep(1)

    # time.sleep(20000)
    #
    # Key_1 = 0x02
    # Key_0 = 0x0B
    # Key_enter = 0x1c
    # count = 0
    #
    #
    #
    # print(pyautogui.position())
    #
    # time.sleep(3)
    # while True:
    #     time.sleep(sleep_time)
    #     print('count = {}'.format(count))
    #     print(pyautogui.position())
    #     pyautogui.rightClick(x=662, y=616)
    #     pyautogui.click()
    #     time.sleep(sleep_time)
    #     pyautogui.rightClick(x=643, y=302)
    #     pyautogui.click()
    #     time.sleep(sleep_time)
    #     pyautogui.rightClick(x=463, y=392)
    #     pyautogui.click()
    #     time.sleep(sleep_time)
    #
    #     if count % 2 == 1:
    #         pyautogui.rightClick(x=383, y=345)
    #         pyautogui.click()
    #     else:
    #         pyautogui.rightClick(x=426, y=327)
    #         pyautogui.click()
    #
    #     time.sleep(sleep_time)
    #     PressKey(Key_1)
    #     ReleaseKey(Key_1)
    #     PressKey(Key_0)
    #     ReleaseKey(Key_0)
    #     time.sleep(sleep_time)
    #
    #     for i in range(3):
    #         PressKey(Key_enter)
    #         ReleaseKey(Key_enter)
    #         time.sleep(sleep_time)
    #
    #     count += 1