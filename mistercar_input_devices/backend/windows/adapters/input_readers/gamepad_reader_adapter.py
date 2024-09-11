from mistercar_input_devices.backend.windows.platform_specific.pyxinput import rController


class GamepadReaderAdapter:
    def __init__(self):
        self.__read_controller = rController(1)

    def get_control_state(self, control):
        return self.__read_controller.gamepad.__getitem__(control)

    def get_states_of_multiple_controls(self, controls_to_check):
        states = [0] * len(controls_to_check)
        for i in range(len(controls_to_check)):
            states[i] = self.__read_controller.gamepad.__getitem__(controls_to_check[i])
        return states
