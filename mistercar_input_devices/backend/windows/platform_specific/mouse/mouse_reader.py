import win32api
from ctypes import windll, Structure, c_long, byref
from win32con import VK_LBUTTON, VK_MBUTTON, VK_RBUTTON, VK_XBUTTON1, VK_XBUTTON2
from mistercar_input_devices.backend.windows.platform_specific.mouse.raw_mouse_reader import RawMouseReader


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


MOUSE_BUTTONS = {
    "left": VK_LBUTTON,
    "middle": VK_MBUTTON,
    "right": VK_RBUTTON,
    "xbutton1": VK_XBUTTON1,
    "xbutton2": VK_XBUTTON2
}


class MouseReader:
    """Read cursor position, mouse movement, scrolling amount and button status"""
    def __init__(self):
        self._raw_mouse_reader = RawMouseReader()
        self._raw_mouse_reader.start()

    @staticmethod
    def get_cursor_position():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return pt.x, pt.y

    def get_relative_movement(self):
        return self._raw_mouse_reader.get_relative_movement()

    @staticmethod
    def get_button_states():
        return [int(win32api.GetAsyncKeyState(button_const) < 0) for button_name, button_const in MOUSE_BUTTONS.items()]

    def get_wheel(self):
        return self._raw_mouse_reader.get_wheel_delta()

    def get_horizontal_wheel(self):
        return self._raw_mouse_reader.get_hwheel_delta()

    def __del__(self):
        self._raw_mouse_reader.stop()
