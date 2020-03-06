import ctypes
import time
import pyautogui


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


# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
if __name__ == '__main__':
    KEY_Q = 0x10
    KEY_W = 0x11
    KEY_E = 0x12
    KEY_A = 0x1E
    count = 0
    time.sleep(3)
    while True:
        # PressKey(KEY_A)
        # ReleaseKey(KEY_A)
        # time.sleep(0.3)
        # PressKey(KEY_A)
        # ReleaseKey(KEY_A)
        # time.sleep(0.3)
        # PressKey(KEY_A)
        # ReleaseKey(KEY_A)
        # player_teleport("down")
        # time.sleep(0.3)
        # PressKey(KEY_A)
        # ReleaseKey(KEY_A)
        # PressKey(KEY_A)
        # time.sleep(100)
        for i in range(30):
            PressKey(KEY_A)
            ReleaseKey(KEY_A)
            time.sleep(3)
            player_teleport("right")
            count += 1
            print('Loop : {}'.format(count))
        player_teleport("left")
        time.sleep(0.5)
        player_teleport("right")
        time.sleep(0.4)

