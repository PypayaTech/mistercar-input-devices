# Code from https://github.com/Sentdex/pygta5/blob/master/original_project/keys.py
# Further modifications by PypayaTech

import ctypes
import time
from threading import Thread
from time import sleep
from queue import Queue
from typing import Optional
from win32con import WHEEL_DELTA
from mistercar_input_devices.backend.windows.platform_specific.mouse.mouse_input_constants import MOUSEEVENTF_MOVE, \
    MOUSEEVENTF_ABSOLUTE, MOUSEEVENTF_WHEEL, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_RIGHTDOWN, \
    MOUSEEVENTF_RIGHTUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_XDOWN, MOUSEEVENTF_XUP
from mistercar_input_devices.backend.windows.platform_specific.structures import MOUSEINPUT, KEYBDINPUT, HARDWAREINPUT, \
    _INPUTunion, INPUT
from mistercar_input_devices.backend.windows.platform_specific.keyboard.virtual_keys import vk
from mistercar_input_devices.backend.windows.platform_specific.keyboard.direct_keys import dk


DIRECT_KEYS = 0x0008
VIRTUAL_KEYS = 0x0000
KEY_PRESS = 0x0000
KEY_RELEASE = 0x0002

XBUTTON1 = 0x0001
XBUTTON2 = 0x0002


# main keys and mouse class
class KeysAndMouse(object):
    common = None
    standalone = False

    # instance of worker class
    keys_and_mouse_worker = None
    keys_process = None

    # setup object
    def __init__(self, common=None):
        self.keys_and_mouse_worker = KeysAndMouseWorker(self)
        # Thread(target=self.keys_worker.processQueue).start()
        self.common = common
        if common is None:
            self.standalone = True
        self._screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        self._screen_height = ctypes.windll.user32.GetSystemMetrics(1)

    # parses keys string and adds keys to the queue
    def parseKeyString(self, string):

        # print keys
        if not self.standalone:
            self.common.info("Processing keys: %s" % string)

        key_queue = []
        errors = []

        # defaults to direct keys
        key_type = DIRECT_KEYS

        # split by comma
        keys = string.upper().split(",")

        # translate
        for key in keys:

            # up, down or stroke?
            up = True
            down = True
            direction = key.split("_")
            subkey = direction[0]
            if len(direction) >= 2:
                if direction[1] == 'UP':
                    down = False
                else:
                    up = False

            # switch to virtual keys
            if subkey == "VK":
                key_type = VIRTUAL_KEYS

            # switch to direct keys
            elif subkey == "DK":
                key_type = DIRECT_KEYS

            # key code
            elif subkey.startswith("0x"):
                subkey = int(subkey, 16)
                if subkey > 0 and subkey < 256:
                    key_queue.append({
                        "key": int(subkey),
                        "okey": subkey,
                        "time": 0,
                        "up": up,
                        "down": down,
                        "type": key_type,
                    })
                else:
                    errors.append(key)

            # pause
            elif subkey.startswith("-"):
                time = float(subkey.replace("-", "")) / 1000
                if time > 0 and time <= 10:
                    key_queue.append({
                        "key": None,
                        "okey": "",
                        "time": time,
                        "up": False,
                        "down": False,
                        "type": None,
                    })
                else:
                    errors.append(key)

            # direct key
            elif key_type == DIRECT_KEYS and subkey in dk:
                key_queue.append({
                    "key": dk[subkey],
                    "okey": subkey,
                    "time": 0,
                    "up": up,
                    "down": down,
                    "type": key_type,
                })

            # virtual key
            elif key_type == VIRTUAL_KEYS and subkey in vk:
                key_queue.append({
                    "key": vk[subkey],
                    "okey": subkey,
                    "time": 0,
                    "up": up,
                    "down": down,
                    "type": key_type,
                })

            # no match?
            else:
                errors.append(key)

        # if there are errors, do not process keys
        if len(errors):
            return errors

        # create new thread if there is no active one
        if self.keys_process is None or not self.keys_process.isAlive():
            self.keys_process = Thread(target=self.keys_and_mouse_worker.processQueue)
            self.keys_process.start()

        # add keys to queue
        for i in key_queue:
            self.keys_and_mouse_worker.key_queue.put(i)
        self.keys_and_mouse_worker.key_queue.put(None)

        return True

    # direct key press
    def direct_key(self, key, direction=None, type=None):
        if type is None:
            type = DIRECT_KEYS
        if direction is None:
            direction = KEY_PRESS
        if key.startswith("0x"):
            key = int(key, 16)
        else:
            key = key.upper()
            lookup_table = dk if type == DIRECT_KEYS else vk
            key = lookup_table[key] if key in lookup_table else 0x0000

        self.keys_and_mouse_worker.sendKey(key, direction | type)

    def _mouse_press(self, event_type: int, x: Optional[int] = None, y: Optional[int] = None, data=0):
        flags = event_type
        if x is not None and y is not None:
            flags |= MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE
            x, y = self._normalize_coords(x, y)
        else:
            x, y = 0, 0
        self.keys_and_mouse_worker.sendMouse(x, y, data, flags)

    def move_mouse_by(self, dx: int, dy: int):
        self.keys_and_mouse_worker.sendMouse(dx, dy, 0, MOUSEEVENTF_MOVE)

    def move_cursor_to(self, x, y):
        x, y = self._normalize_coords(x, y)
        self.keys_and_mouse_worker.sendMouse(x, y, 0, MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE)

    def scroll(self, clicks: int = 1):
        self.keys_and_mouse_worker.sendMouse(0, 0, clicks * WHEEL_DELTA, MOUSEEVENTF_WHEEL)

    def left_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_LEFTDOWN, x, y)

    def left_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_LEFTUP, x, y)

    def middle_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_MIDDLEDOWN, x, y)

    def middle_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_MIDDLEUP, x, y)

    def right_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_RIGHTDOWN, x, y)

    def right_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_RIGHTUP, x, y)

    def xbutton1_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_XDOWN, x, y, XBUTTON1)

    def xbutton1_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_XUP, x, y, XBUTTON1)

    def xbutton2_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_XDOWN, x, y, XBUTTON2)

    def xbutton2_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._mouse_press(MOUSEEVENTF_XUP, x, y, XBUTTON2)

    def click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.left_button_press(x, y)
        time.sleep(duration)
        self.left_button_release(x, y)

    def left_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.click(x, y, duration)

    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.middle_button_press(x, y)
        time.sleep(duration)
        self.middle_button_release(x, y)

    def right_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.right_button_press(x, y)
        time.sleep(duration)
        self.right_button_release(x, y)

    def xbutton1_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.xbutton1_press(x, y)
        time.sleep(duration)
        self.xbutton1_release(x, y)

    def xbutton2_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.xbutton2_press(x, y)
        time.sleep(duration)
        self.xbutton2_release(x, y)

    def _normalize_coords(self, x, y):
        return (x * 65535) // self._screen_width, (y * 65535) // self._screen_height


# threaded sending keys class
class KeysAndMouseWorker:
    # keys and mouse object
    keys_and_mouse = None

    # queue of keys
    key_queue = Queue()

    # init
    def __init__(self, keys_and_mouse):
        self.keys_and_mouse = keys_and_mouse

    # main function, process key's queue in loop
    def processQueue(self):

        # endless loop
        while True:

            # get one key
            key = self.key_queue.get()

            # terminate process if queue is empty
            if key is None:
                self.key_queue.task_done()
                if self.key_queue.empty():
                    return
                continue
            # print key
            elif not self.keys_and_mouse.standalone:
                self.keys_and_mouse.common.info(
                    "Key: \033[1;35m%s/%s\033[0;37m, duration: \033[1;35m%f\033[0;37m, direction: \033[1;35m%s\033[0;37m, type: \033[1;35m%s" % (
                        key["okey"] if key["okey"] else "None",
                        key["key"], key["time"],
                        "UP" if key["up"] and not key["down"] else "DOWN" if not key["up"] and key[
                            "down"] else "BOTH" if key["up"] and key["down"] else "NONE",
                        "None" if key["type"] is None else "DK" if key["type"] == DIRECT_KEYS else "VK"),
                    "\033[0;35mKEY:    \033[0;37m"
                    )

            # if it's a key
            if key["key"]:

                # press
                if key["down"]:
                    self.sendKey(key["key"], KEY_PRESS | key["type"])

                # wait
                sleep(key["time"])

                # and release
                if key["up"]:
                    self.sendKey(key["key"], KEY_RELEASE | key["type"])

            # not an actual key, just pause
            else:
                sleep(key["time"])

            # mark as done (decrement internal queue counter)
            self.key_queue.task_done()

    # send key
    def sendKey(self, key, type):
        self.SendInput(self.Keyboard(key, type))

    # send mouse
    def sendMouse(self, dx, dy, data, flags):
        self.SendInput(self.Mouse(flags, dx, dy, data))

    # send input
    def SendInput(self, *inputs):
        nInputs = len(inputs)
        LPINPUT = INPUT * nInputs
        pInputs = LPINPUT(*inputs)
        cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
        return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)

    # get input object
    def Input(self, structure):
        if isinstance(structure, MOUSEINPUT):
            return INPUT(0, _INPUTunion(mi=structure))
        if isinstance(structure, KEYBDINPUT):
            return INPUT(1, _INPUTunion(ki=structure))
        if isinstance(structure, HARDWAREINPUT):
            return INPUT(2, _INPUTunion(hi=structure))
        raise TypeError('Cannot create INPUT structure!')

    # mouse input
    def MouseInput(self, x, y, data, flags):
        return MOUSEINPUT(x, y, data, flags, 0, None)

    # keyboard input
    def KeybdInput(self, code, flags):
        return KEYBDINPUT(code, code, flags, 0, None)

    # hardware input
    def HardwareInput(self, message, parameter):
        return HARDWAREINPUT(message & 0xFFFFFFFF,
                             parameter & 0xFFFF,
                             parameter >> 16 & 0xFFFF)

    # mouse object
    def Mouse(self, flags, x=0, y=0, data=0):
        return self.Input(self.MouseInput(x, y, data, flags))

    # keyboard object
    def Keyboard(self, code, flags=0):
        return self.Input(self.KeybdInput(code, flags))

    # hardware object
    def Hardware(self, message, parameter=0):
        return self.Input(self.HardwareInput(message, parameter))


def main():
    keys = KeysAndMouse()

    sleep_time = 2
    x, y = 500, 200

    sleep(sleep_time)

    # Left click at current point
    print("Left click at current point")
    keys.left_click()
    sleep(sleep_time)

    # Left click at specific point
    print(f"Left click at x={x}, y={y}")
    keys.left_click(x=x, y=y)
    sleep(sleep_time)

    # Middle click at current point
    print("Middle click at current point")
    keys.middle_click()
    sleep(sleep_time)

    # Middle click at specific point
    print(f"Middle click at x={x}, y={y}")
    keys.middle_click(x=x, y=y)
    sleep(sleep_time)

    # Right click at current point
    print("Right click at current point")
    keys.right_click()
    sleep(sleep_time)

    # Right click at specific point
    print(f"Right click at x={x}, y={y}")
    keys.right_click(x=x, y=y)
    sleep(sleep_time)

    # Click XBUTTON1
    print("Click XBUTTON1")
    keys.xbutton1_click()
    sleep(sleep_time)

    # Click XBUTTON2
    print("Click XBUTTON2")
    keys.xbutton2_click()
    sleep(sleep_time)

    # Moving
    print("Moving mouse by dx = 50, dy = 50")
    keys.move_mouse_by(dx=50, dy=50)
    sleep(sleep_time)

    # Teleporting
    print(f"Teleporting cursor to x={x}, y={y}")
    keys.move_cursor_to(x=x, y=y)
    sleep(sleep_time)

    # Scrolling
    print("Scrolling mouse 3 times up")
    keys.scroll(clicks=3)
    sleep(sleep_time)

    # keyboard (direct keys)
    keys.direct_key("a")
    sleep(0.04)
    keys.direct_key("a", KEY_RELEASE)

    # keyboard (virtual keys)
    keys.direct_key("a", type=VIRTUAL_KEYS)
    sleep(0.04)
    keys.direct_key("a", KEY_RELEASE, VIRTUAL_KEYS)

    # queue of keys (direct keys, threaded, only for keybord input)
    keys.parseKeyString("a_down,-4,a_up,0x01")  # -4 - pause for 4 ms, 0x00 - hex code of Esc

    # queue of keys (virtual keys, threaded, only for keybord input)
    keys.parseKeyString("vk,a_down,-4,a_up")  # -4 - pause for 4 ms


if __name__ == "__main__":
    main()
