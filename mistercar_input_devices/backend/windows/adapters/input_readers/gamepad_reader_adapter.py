from mistercar_input_devices.backend.windows.platform_specific.pyxinput import rController


class GamepadReaderAdapter:
    def __init__(self):
        self.__read_controller = rController(1)

    # === STICKS ===
    def get_left_stick(self):
        """Returns (x, y) tuple for left stick"""
        gamepad = self.__read_controller.gamepad
        return (gamepad["thumb_lx"], gamepad["thumb_ly"])

    def get_right_stick(self):
        """Returns (x, y) tuple for right stick"""
        gamepad = self.__read_controller.gamepad
        return (gamepad["thumb_rx"], gamepad["thumb_ry"])

    def get_left_stick_x(self):
        return self.__read_controller.gamepad["thumb_lx"]

    def get_left_stick_y(self):
        return self.__read_controller.gamepad["thumb_ly"]

    def get_right_stick_x(self):
        return self.__read_controller.gamepad["thumb_rx"]

    def get_right_stick_y(self):
        return self.__read_controller.gamepad["thumb_ry"]

    # === TRIGGERS ===
    def get_triggers(self):
        """Returns (left, right) tuple"""
        gamepad = self.__read_controller.gamepad
        return (gamepad["left_trigger"], gamepad["right_trigger"])

    def get_left_trigger(self):
        return self.__read_controller.gamepad["left_trigger"]

    def get_right_trigger(self):
        return self.__read_controller.gamepad["right_trigger"]

    # === FACE BUTTONS ===
    def get_face_buttons(self):
        """Returns [A, B, X, Y] button states"""
        buttons = self.__read_controller.buttons
        return [
            1 if 'A' in buttons else 0,
            1 if 'B' in buttons else 0,
            1 if 'X' in buttons else 0,
            1 if 'Y' in buttons else 0
        ]

    def get_button_a(self):
        return 1 if 'A' in self.__read_controller.buttons else 0

    def get_button_b(self):
        return 1 if 'B' in self.__read_controller.buttons else 0

    def get_button_x(self):
        return 1 if 'X' in self.__read_controller.buttons else 0

    def get_button_y(self):
        return 1 if 'Y' in self.__read_controller.buttons else 0

    # === SHOULDER BUTTONS ===
    def get_shoulder_buttons(self):
        """Returns [left, right] shoulder button states"""
        buttons = self.__read_controller.buttons
        return [
            1 if "LEFT_SHOULDER" in buttons else 0,
            1 if "RIGHT_SHOULDER" in buttons else 0
        ]

    def get_left_shoulder(self):
        return 1 if "LEFT_SHOULDER" in self.__read_controller.buttons else 0

    def get_right_shoulder(self):
        return 1 if "RIGHT_SHOULDER" in self.__read_controller.buttons else 0

    # === THUMB BUTTONS ===
    def get_thumb_buttons(self):
        """Returns [left, right] thumb button states"""
        buttons = self.__read_controller.buttons
        return [
            1 if "LEFT_THUMB" in buttons else 0,
            1 if "RIGHT_THUMB" in buttons else 0
        ]

    def get_left_thumb(self):
        return 1 if "LEFT_THUMB" in self.__read_controller.buttons else 0

    def get_right_thumb(self):
        return 1 if "RIGHT_THUMB" in self.__read_controller.buttons else 0

    # === MENU BUTTONS ===
    def get_menu_buttons(self):
        """Returns [back, start] menu button states"""
        buttons = self.__read_controller.buttons
        return [
            1 if "BACK" in buttons else 0,
            1 if "START" in buttons else 0
        ]

    def get_back_button(self):
        return 1 if "BACK" in self.__read_controller.buttons else 0

    def get_start_button(self):
        return 1 if "START" in self.__read_controller.buttons else 0

    # === DPAD ===
    def get_dpad(self):
        """Returns [up, down, left, right] dpad states"""
        buttons = self.__read_controller.buttons
        return [
            1 if "DPAD_UP" in buttons else 0,
            1 if "DPAD_DOWN" in buttons else 0,
            1 if "DPAD_LEFT" in buttons else 0,
            1 if "DPAD_RIGHT" in buttons else 0
        ]

    def get_dpad_up(self):
        return 1 if "DPAD_UP" in self.__read_controller.buttons else 0

    def get_dpad_down(self):
        return 1 if "DPAD_DOWN" in self.__read_controller.buttons else 0

    def get_dpad_left(self):
        return 1 if "DPAD_LEFT" in self.__read_controller.buttons else 0

    def get_dpad_right(self):
        return 1 if "DPAD_RIGHT" in self.__read_controller.buttons else 0

    # === KEYBOARD-STYLE METHODS ===
    def get_button_state(self, button_name):
        """Get state of a single button by name"""
        button_mapping = {
            'A': 'A', 'B': 'B', 'X': 'X', 'Y': 'Y',
            "LEFT_SHOULDER": "LEFT_SHOULDER", "RIGHT_SHOULDER": "RIGHT_SHOULDER",
            "LEFT_THUMB": "LEFT_THUMB", "RIGHT_THUMB": "RIGHT_THUMB",
            "BACK": "BACK", "START": "START",
            "DPAD_UP": "DPAD_UP", "DPAD_DOWN": "DPAD_DOWN",
            "DPAD_LEFT": "DPAD_LEFT", "DPAD_RIGHT": "DPAD_RIGHT"
        }

        if button_name in button_mapping:
            return 1 if button_mapping[button_name] in self.__read_controller.buttons else 0
        return 0

    def get_states_of_multiple_buttons(self, buttons_to_check):
        """Returns list of button states in same order as input"""
        return [self.get_button_state(button) for button in buttons_to_check]
