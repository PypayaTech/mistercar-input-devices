from mistercar_input_devices.backend.windows.platform_specific.pyxinput import vController


class GamepadEmulatorAdapter:
    def __init__(self):
        self._gamepad = vController()

    # === STICKS ===
    def emulate_left_stick(self, x, y):
        """Set left stick position"""
        self._gamepad.set_value("AxisLx", x)
        self._gamepad.set_value("AxisLy", y)

    def emulate_right_stick(self, x, y):
        """Set right stick position"""
        self._gamepad.set_value("AxisRx", x)
        self._gamepad.set_value("AxisRy", y)

    def emulate_left_stick_x(self, value):
        self._gamepad.set_value("AxisLx", value)

    def emulate_left_stick_y(self, value):
        self._gamepad.set_value("AxisLy", value)

    def emulate_right_stick_x(self, value):
        self._gamepad.set_value("AxisRx", value)

    def emulate_right_stick_y(self, value):
        self._gamepad.set_value("AxisRy", value)

    # === TRIGGERS ===
    def emulate_triggers(self, left, right):
        """Set both trigger values"""
        self._gamepad.set_value("TriggerL", left)
        self._gamepad.set_value("TriggerR", right)

    def emulate_left_trigger(self, value):
        self._gamepad.set_value("TriggerL", value)

    def emulate_right_trigger(self, value):
        self._gamepad.set_value("TriggerR", value)

    # === FACE BUTTONS ===
    def emulate_face_buttons(self, a, b, x, y):
        """Set all face button states"""
        self._gamepad.set_value("BtnA", 1 if a else 0)
        self._gamepad.set_value("BtnB", 1 if b else 0)
        self._gamepad.set_value("BtnX", 1 if x else 0)
        self._gamepad.set_value("BtnY", 1 if y else 0)

    def emulate_button_a(self, pressed):
        self._gamepad.set_value("BtnA", 1 if pressed else 0)

    def emulate_button_b(self, pressed):
        self._gamepad.set_value("BtnB", 1 if pressed else 0)

    def emulate_button_x(self, pressed):
        self._gamepad.set_value("BtnX", 1 if pressed else 0)

    def emulate_button_y(self, pressed):
        self._gamepad.set_value("BtnY", 1 if pressed else 0)

    # === SHOULDER BUTTONS ===
    def emulate_shoulder_buttons(self, left, right):
        """Set both shoulder button states"""
        self._gamepad.set_value("BtnShoulderL", 1 if left else 0)
        self._gamepad.set_value("BtnShoulderR", 1 if right else 0)

    def emulate_left_shoulder(self, pressed):
        self._gamepad.set_value("BtnShoulderL", 1 if pressed else 0)

    def emulate_right_shoulder(self, pressed):
        self._gamepad.set_value("BtnShoulderR", 1 if pressed else 0)

    # === THUMB BUTTONS ===
    def emulate_thumb_buttons(self, left, right):
        """Set both thumb button states"""
        self._gamepad.set_value("BtnThumbL", 1 if left else 0)
        self._gamepad.set_value("BtnThumbR", 1 if right else 0)

    def emulate_left_thumb(self, pressed):
        self._gamepad.set_value("BtnThumbL", 1 if pressed else 0)

    def emulate_right_thumb(self, pressed):
        self._gamepad.set_value("BtnThumbR", 1 if pressed else 0)

    # === MENU BUTTONS ===
    def emulate_menu_buttons(self, back, start):
        """Set both menu button states"""
        self._gamepad.set_value("BtnBack", 1 if back else 0)
        self._gamepad.set_value("BtnStart", 1 if start else 0)

    def emulate_back_button(self, pressed):
        self._gamepad.set_value("BtnBack", 1 if pressed else 0)

    def emulate_start_button(self, pressed):
        self._gamepad.set_value("BtnStart", 1 if pressed else 0)

    # === DPAD ===
    def emulate_dpad(self, up, down, left, right):
        """Set dpad state - uses original Dpad control with combined value"""
        value = 0
        if up: value |= 1
        if down: value |= 2
        if left: value |= 4
        if right: value |= 8
        self._gamepad.set_value("Dpad", value)

    def emulate_dpad_up(self, pressed):
        self._gamepad.set_value("Dpad", 1 if pressed else 0)

    def emulate_dpad_down(self, pressed):
        self._gamepad.set_value("Dpad", 2 if pressed else 0)

    def emulate_dpad_left(self, pressed):
        self._gamepad.set_value("Dpad", 4 if pressed else 0)

    def emulate_dpad_right(self, pressed):
        self._gamepad.set_value("Dpad", 8 if pressed else 0)
