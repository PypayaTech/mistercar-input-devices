from mistercar_input_devices.backend.windows.platform_specific.pyxinput import vController


class GamepadEmulatorAdapter:
    def __init__(self):
        self._gamepad = vController()

    def emulate_control(self, control, value):
        self._gamepad.set_value(control, value)

    def emulate_multiple_controls(self, control_value_dict):
        for key in control_value_dict:
            self._gamepad.set_value(key, control_value_dict[key])
