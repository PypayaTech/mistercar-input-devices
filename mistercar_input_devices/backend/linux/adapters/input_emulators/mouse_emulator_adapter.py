from typing import Optional
import pyautogui


class MouseEmulatorAdapter:
    def __init__(self):
        pass

    def move_mouse_by(self, dx: int, dy: int):
        pyautogui.moveRel(dx, dy)

    def move_cursor_to(self, x: int, y: int):
        pyautogui.moveTo(x, y)

    def scroll(self, clicks: int = 1):
        pyautogui.scroll(clicks * 120)  # Each click scrolls by 120 units

    def left_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseDown, "left")

    def left_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseUp, "left")

    def middle_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseDown, "middle")

    def middle_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseUp, "middle")

    def right_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseDown, "right")

    def right_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self._move_and_click(x, y, pyautogui.mouseUp, "right")

    def xbutton1_press(self, x: Optional[int] = None, y: Optional[int] = None):
        raise NotImplementedError

    def xbutton1_release(self, x: Optional[int] = None, y: Optional[int] = None):
        raise NotImplementedError

    def xbutton2_press(self, x: Optional[int] = None, y: Optional[int] = None):
        raise NotImplementedError

    def xbutton2_release(self, x: Optional[int] = None, y: Optional[int] = None):
        raise NotImplementedError

    def click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.left_click(x, y, duration)

    def left_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._move_and_click(x, y, pyautogui.click, "left", duration)

    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._move_and_click(x, y, pyautogui.click, "middle", duration)

    def right_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self._move_and_click(x, y, pyautogui.click, "right", duration)

    def xbutton1_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        raise NotImplementedError

    def xbutton2_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        raise NotImplementedError

    def _move_and_click(self, x, y, action, button, duration=0.0):
        if x is not None and y is not None:
            pyautogui.moveTo(x, y)
        action(button=button, duration=duration)
