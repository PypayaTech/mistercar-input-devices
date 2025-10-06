import platform


class GamepadReader:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_readers.gamepad_reader_adapter import \
                GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_readers.gamepad_reader_adapter import \
                GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_readers.gamepad_reader_adapter import \
                GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()

    # === STICKS ===
    def get_left_stick(self):
        """Returns (x, y) tuple for left stick"""
        return self.__reader.get_left_stick()

    def get_right_stick(self):
        """Returns (x, y) tuple for right stick"""
        return self.__reader.get_right_stick()

    def get_left_stick_x(self):
        return self.__reader.get_left_stick_x()

    def get_left_stick_y(self):
        return self.__reader.get_left_stick_y()

    def get_right_stick_x(self):
        return self.__reader.get_right_stick_x()

    def get_right_stick_y(self):
        return self.__reader.get_right_stick_y()

    # === TRIGGERS ===
    def get_triggers(self):
        """Returns (left, right) tuple"""
        return self.__reader.get_triggers()

    def get_left_trigger(self):
        return self.__reader.get_left_trigger()

    def get_right_trigger(self):
        return self.__reader.get_right_trigger()

    # === FACE BUTTONS ===
    def get_face_buttons(self):
        """Returns [A, B, X, Y] button states"""
        return self.__reader.get_face_buttons()

    def get_button_a(self):
        return self.__reader.get_button_a()

    def get_button_b(self):
        return self.__reader.get_button_b()

    def get_button_x(self):
        return self.__reader.get_button_x()

    def get_button_y(self):
        return self.__reader.get_button_y()

    # === SHOULDER BUTTONS ===
    def get_shoulder_buttons(self):
        """Returns [left, right] shoulder button states"""
        return self.__reader.get_shoulder_buttons()

    def get_left_shoulder(self):
        return self.__reader.get_left_shoulder()

    def get_right_shoulder(self):
        return self.__reader.get_right_shoulder()

    # === THUMB BUTTONS ===
    def get_thumb_buttons(self):
        """Returns [left, right] thumb button states"""
        return self.__reader.get_thumb_buttons()

    def get_left_thumb(self):
        return self.__reader.get_left_thumb()

    def get_right_thumb(self):
        return self.__reader.get_right_thumb()

    # === MENU BUTTONS ===
    def get_menu_buttons(self):
        """Returns [back, start] menu button states"""
        return self.__reader.get_menu_buttons()

    def get_back_button(self):
        return self.__reader.get_back_button()

    def get_start_button(self):
        return self.__reader.get_start_button()

    # === DPAD ===
    def get_dpad(self):
        """Returns [up, down, left, right] dpad states"""
        return self.__reader.get_dpad()

    def get_dpad_up(self):
        return self.__reader.get_dpad_up()

    def get_dpad_down(self):
        return self.__reader.get_dpad_down()

    def get_dpad_left(self):
        return self.__reader.get_dpad_left()

    def get_dpad_right(self):
        return self.__reader.get_dpad_right()

    # === KEYBOARD-STYLE METHODS ===
    def get_button_state(self, button_name):
        """Get state of a single button by name"""
        return self.__reader.get_button_state(button_name)

    def get_states_of_multiple_buttons(self, buttons_to_check):
        """Returns list of button states in same order as input"""
        return self.__reader.get_states_of_multiple_buttons(buttons_to_check)
