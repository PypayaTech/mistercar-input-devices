import platform


class GamepadReader:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_readers.gamepad_reader_adapter import GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_readers.gamepad_reader_adapter import GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_readers.gamepad_reader_adapter import GamepadReaderAdapter
            self.__reader = GamepadReaderAdapter()

    def get_control_state(self, control):
        return self.__reader.get_control_state(control)

    def get_states_of_multiple_controls(self, controls_to_check):
        return self.__reader.get_states_of_multiple_controls(controls_to_check)
