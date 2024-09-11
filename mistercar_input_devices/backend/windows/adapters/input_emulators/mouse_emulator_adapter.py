from typing import Optional
from mistercar_input_devices.backend.windows.platform_specific.keys_and_mouse import KeysAndMouse


class MouseEmulatorAdapter:
    def __init__(self):
        self._keys_and_mouse = KeysAndMouse()

    def move_mouse_by(self, dx: int, dy: int):
        self._keys_and_mouse.move_mouse_by(dx, dy)

    def move_cursor_to(self, x: int, y: int):
        self._keys_and_mouse.move_cursor_to(x, y)

    def scroll(self, clicks: int = 1):
        self._keys_and_mouse.scroll(clicks)

    def left_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.left_button_press(x, y)

    def left_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.left_button_release(x, y)

    def middle_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.middle_button_press(x, y)

    def middle_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.middle_button_release(x, y)

    def right_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.right_button_press(x, y)

    def right_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.right_button_release(x, y)

    def xbutton1_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.xbutton1_press(x, y)

    def xbutton1_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.xbutton1_release(x, y)

    def xbutton2_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.xbutton2_press(x, y)

    def xbutton2_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._keys_and_mouse.xbutton2_release(x, y)

    def click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._keys_and_mouse.click(x, y, duration)

    def left_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.click(x, y, duration)

    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._keys_and_mouse.middle_click(x, y, duration)

    def right_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._keys_and_mouse.right_click(x, y, duration)

    def xbutton1_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._keys_and_mouse.xbutton1_click(x, y, duration)

    def xbutton2_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._keys_and_mouse.xbutton2_click(x, y, duration)
