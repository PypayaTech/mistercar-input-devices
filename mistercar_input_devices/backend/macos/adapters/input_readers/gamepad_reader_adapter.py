

class GamepadReaderAdapter:
    def __init__(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === STICKS ===
    def get_left_stick(self):
        """Returns (x, y) tuple for left stick"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_stick(self):
        """Returns (x, y) tuple for right stick"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_left_stick_x(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_left_stick_y(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_stick_x(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_stick_y(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === TRIGGERS ===
    def get_triggers(self):
        """Returns (left, right) tuple"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_left_trigger(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_trigger(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === FACE BUTTONS ===
    def get_face_buttons(self):
        """Returns [A, B, X, Y] button states"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_button_a(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_button_b(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_button_x(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_button_y(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === SHOULDER BUTTONS ===
    def get_shoulder_buttons(self):
        """Returns [left, right] shoulder button states"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_left_shoulder(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_shoulder(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === THUMB BUTTONS ===
    def get_thumb_buttons(self):
        """Returns [left, right] thumb button states"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_left_thumb(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_right_thumb(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === MENU BUTTONS ===
    def get_menu_buttons(self):
        """Returns [back, start] menu button states"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_back_button(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_start_button(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === DPAD ===
    def get_dpad(self):
        """Returns [up, down, left, right] dpad states"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_dpad_up(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_dpad_down(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_dpad_left(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_dpad_right(self):
        raise NotImplementedError("macOS gamepad support not yet implemented")

    # === KEYBOARD-STYLE METHODS ===
    def get_button_state(self, button_name):
        """Get state of a single button by name"""
        raise NotImplementedError("macOS gamepad support not yet implemented")

    def get_states_of_multiple_buttons(self, buttons_to_check):
        """Returns list of button states in same order as input"""
        raise NotImplementedError("macOS gamepad support not yet implemented")
