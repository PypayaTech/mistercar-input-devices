import platform


class GamepadEmulator:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_emulators.gamepad_emulator_adapter import \
                GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_emulators.gamepad_emulator_adapter import \
                GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_emulators.gamepad_emulator_adapter import \
                GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()

    # === STICKS ===
    def emulate_left_stick(self, x, y):
        """Set left stick position"""
        return self.__emulator.emulate_left_stick(x, y)

    def emulate_right_stick(self, x, y):
        """Set right stick position"""
        return self.__emulator.emulate_right_stick(x, y)

    def emulate_left_stick_x(self, value):
        return self.__emulator.emulate_left_stick_x(value)

    def emulate_left_stick_y(self, value):
        return self.__emulator.emulate_left_stick_y(value)

    def emulate_right_stick_x(self, value):
        return self.__emulator.emulate_right_stick_x(value)

    def emulate_right_stick_y(self, value):
        return self.__emulator.emulate_right_stick_y(value)

    # === TRIGGERS ===
    def emulate_triggers(self, left, right):
        """Set both trigger values"""
        return self.__emulator.emulate_triggers(left, right)

    def emulate_left_trigger(self, value):
        return self.__emulator.emulate_left_trigger(value)

    def emulate_right_trigger(self, value):
        return self.__emulator.emulate_right_trigger(value)

    # === FACE BUTTONS ===
    def emulate_face_buttons(self, a, b, x, y):
        """Set all face button states"""
        return self.__emulator.emulate_face_buttons(a, b, x, y)

    def emulate_button_a(self, pressed):
        return self.__emulator.emulate_button_a(pressed)

    def emulate_button_b(self, pressed):
        return self.__emulator.emulate_button_b(pressed)

    def emulate_button_x(self, pressed):
        return self.__emulator.emulate_button_x(pressed)

    def emulate_button_y(self, pressed):
        return self.__emulator.emulate_button_y(pressed)

    # === SHOULDER BUTTONS ===
    def emulate_shoulder_buttons(self, left, right):
        """Set both shoulder button states"""
        return self.__emulator.emulate_shoulder_buttons(left, right)

    def emulate_left_shoulder(self, pressed):
        return self.__emulator.emulate_left_shoulder(pressed)

    def emulate_right_shoulder(self, pressed):
        return self.__emulator.emulate_right_shoulder(pressed)

    # === THUMB BUTTONS ===
    def emulate_thumb_buttons(self, left, right):
        """Set both thumb button states"""
        return self.__emulator.emulate_thumb_buttons(left, right)

    def emulate_left_thumb(self, pressed):
        return self.__emulator.emulate_left_thumb(pressed)

    def emulate_right_thumb(self, pressed):
        return self.__emulator.emulate_right_thumb(pressed)

    # === MENU BUTTONS ===
    def emulate_menu_buttons(self, back, start):
        """Set both menu button states"""
        return self.__emulator.emulate_menu_buttons(back, start)

    def emulate_back_button(self, pressed):
        return self.__emulator.emulate_back_button(pressed)

    def emulate_start_button(self, pressed):
        return self.__emulator.emulate_start_button(pressed)

    # === DPAD ===
    def emulate_dpad(self, up, down, left, right):
        """Set dpad state"""
        return self.__emulator.emulate_dpad(up, down, left, right)

    def emulate_dpad_up(self, pressed):
        return self.__emulator.emulate_dpad_up(pressed)

    def emulate_dpad_down(self, pressed):
        return self.__emulator.emulate_dpad_down(pressed)

    def emulate_dpad_left(self, pressed):
        return self.__emulator.emulate_dpad_left(pressed)

    def emulate_dpad_right(self, pressed):
        return self.__emulator.emulate_dpad_right(pressed)
