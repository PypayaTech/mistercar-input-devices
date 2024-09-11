import platform
from typing import Optional


class MouseEmulator:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_emulators.mouse_emulator_adapter import MouseEmulatorAdapter
            self.__emulator = MouseEmulatorAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_emulators.mouse_emulator_adapter import MouseEmulatorAdapter
            self.__emulator = MouseEmulatorAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_emulators.mouse_emulator_adapter import MouseEmulatorAdapter
            self.__emulator = MouseEmulatorAdapter()

    def move_mouse_by(self, dx: int, dy: int):
        self.__emulator.move_mouse_by(dx, dy)

    def move_cursor_to(self, x: int, y: int):
        self.__emulator.move_cursor_to(x, y)

    def scroll(self, clicks: int = 1):
        self.__emulator.scroll(clicks)

    def left_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.left_button_press(x, y)

    def left_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.left_button_release(x, y)

    def middle_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.middle_button_press(x, y)

    def middle_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.middle_button_release(x, y)

    def right_button_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.right_button_press(x, y)

    def right_button_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.right_button_release(x, y)

    def xbutton1_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.xbutton1_press(x, y)

    def xbutton1_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.xbutton1_release(x, y)

    def xbutton2_press(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.xbutton2_press(x, y)

    def xbutton2_release(self, x: Optional[int] = None, y: Optional[int] = None):
        self.__emulator.xbutton2_release(x, y)

    def click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.click(x, y, duration)

    def left_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.left_click(x, y, duration)

    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.middle_click(x, y, duration)

    def right_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.right_click(x, y, duration)

    def xbutton1_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.xbutton1_click(x, y, duration)

    def xbutton2_click(self, x: Optional[int] = None, y: Optional[int] = None, duration: float = 0.0):
        self.__emulator.xbutton2_click(x, y, duration)
