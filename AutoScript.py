import ctypes
import time
import pyautogui
import random
import json
# from MainWindow import MainWindow
# from PyQt5.QtWidgets import QApplication
# from PyQt5 import sip
from ScreenInformProcess import ScreenInformProcess
from threading import Thread


key_dict = {"A": 0x1E, "B": 0x30, "C": 0x2E, "D": 0x20, "E": 0x12, "F": 0x21, "G": 0x22, "H": 0x23,
            "I": 0x17, "J": 0x24, "K": 0x25, "L": 0x26, "M": 0x32, "N": 0x31, "O": 0x18, "P": 0x19,
            "Q": 0x10, "R": 0x13, "S": 0x1F, "T": 0x14, "U": 0x16, "V": 0x2F, "W": 0x11, "X": 0x2D,
            "Y": 0x15, "Z": 0x2C, "Enter": 0x1c, "0": 0x0B, "1": 0x02, "2":0x03, "3": 0x04 , "4": 0x05, "5":0x06,
            "6": 0x07 ,"7":0x08, "8":0x09, "9": 0x0A, "Esc": 0x01}


arrow_keys_list = ['up','left','right','down']
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
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
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


class AutoScript:
    def __init__(self, callback_show_message=None):
        self.callback_show_message = callback_show_message
        self.stop = False
        self.init()
        self.get_script_json()

    def init(self):
        self.left_right_count = 0
        self.script_list = None

    def get_script_json(self):
        try:
            f = open("script_list.json", 'r')
            self.script_list = json.load(f)
            f.close()
        except Exception as e:
            print('=' * 20)
            print('{}\n{}'.format(e,'script_list.json load error'))
            print('=' * 20)

    def buffer_time(self):
        sec = 3
        for n in range(sec):
            self.show_message('{}秒後開始'.format(sec - n))
            time.sleep(1)

    def script_process(self):
        for script in self.script_list:
            if self.stop is False:
                if script['name'] == 'auto_send_message':
                    self.auto_send_message(do_sleep=script['sleep'])
                elif script['name'] == 'auto_left_and_right':
                    self.auto_left_and_right(do_sleep=script['sleep'])
                elif script['name'] == 'mouse_click':
                    self.mouse_controller(do_sleep=script['sleep'],
                                          click_count=script['click_count'],
                                          x=script['x'],
                                          y=script['y'])
                else:
                    self.keybroad_controller(event=script['event'],
                                             do_sleep=script['sleep'],
                                             repeats=script['repeat'])

    def mouse_controller(self, do_sleep, click_count, x, y):
        pyautogui.click(clicks=click_count, x=x, y=y)
        time.sleep(do_sleep)

        self.show_message('mouse_click: {}, x y : {},{}'.format(click_count, x, y))

    def auto_left_and_right(self, do_sleep):
        time.sleep(1)
        if self.left_right_count % 2 == 1:
            self.show_message('left')
            player_teleport("left")
            time.sleep(do_sleep)
            # time.sleep(0.5 * random.random())
        else:
            self.show_message('right')
            player_teleport("right")
            time.sleep(do_sleep)
            # time.sleep(0.5 * random.random())
        self.left_right_count += 1
        self.show_message('auto_left_and_right: {}'.format(self.left_right_count))

    def auto_send_message(self, do_sleep):
        self.show_message('auto_send_message')
        Key_enter = 0x1c
        delay = 0.1

        PressKey(Key_enter)
        ReleaseKey(Key_enter)
        time.sleep(delay)

        player_teleport('up')
        time.sleep(delay)

        player_teleport('up')
        time.sleep(delay)

        PressKey(Key_enter)
        ReleaseKey(Key_enter)
        time.sleep(delay)

        PressKey(Key_enter)
        ReleaseKey(Key_enter)

        time.sleep(do_sleep)

    def keybroad_controller(self, event, do_sleep, repeats):
        for count in range(repeats):
            if self.stop is False:
                if event in arrow_keys_list:
                    player_teleport(event)
                    time.sleep(do_sleep)
                else:
                    PressKey(key_dict[event])
                    ReleaseKey(key_dict[event])
                    time.sleep(do_sleep)

                self.show_message('event: {}, Loop : {}'.format(event, count))

    def execute(self):
        self.buffer_time()
        while True:
            self.script_process()

    def show_message(self, message):
        if self.callback_show_message is None:
            print(message)
        else:
            self.callback_show_message(message)


if __name__ == '__main__':
    Thread(
        target=ScreenInformProcess().execute,
        daemon=True
    ).start()

    obj = AutoScript()
    print(obj.script_list)
    obj.execute()

    # app = QApplication([])
    #
    # main_window = MainWindow().get_main_window()
    # main_window.setFixedSize(1024, 768)
    # main_window.show()
    # sys.exit(app.exec_())