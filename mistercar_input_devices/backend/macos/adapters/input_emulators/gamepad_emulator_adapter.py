class GamepadEmulatorAdapter:
    def __init__(self):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === STICKS ===
    def emulate_left_stick(self, x, y):
        """Set left stick position"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_stick(self, x, y):
        """Set right stick position"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_left_stick_x(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_left_stick_y(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_stick_x(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_stick_y(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === TRIGGERS ===
    def emulate_triggers(self, left, right):
        """Set both trigger values"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_left_trigger(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_trigger(self, value):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === FACE BUTTONS ===
    def emulate_face_buttons(self, a, b, x, y):
        """Set all face button states"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_button_a(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_button_b(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_button_x(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_button_y(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === SHOULDER BUTTONS ===
    def emulate_shoulder_buttons(self, left, right):
        """Set both shoulder button states"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_left_shoulder(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_shoulder(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === THUMB BUTTONS ===
    def emulate_thumb_buttons(self, left, right):
        """Set both thumb button states"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_left_thumb(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_right_thumb(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === MENU BUTTONS ===
    def emulate_menu_buttons(self, back, start):
        """Set both menu button states"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_back_button(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_start_button(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    # === DPAD ===
    def emulate_dpad(self, up, down, left, right):
        """Set dpad state"""
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_dpad_up(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_dpad_down(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_dpad_left(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")

    def emulate_dpad_right(self, pressed):
        raise NotImplementedError("macOS gamepad emulation not yet implemented")
