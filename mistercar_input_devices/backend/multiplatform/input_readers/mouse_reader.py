import platform


class MouseReader:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_readers.mouse_reader_adapter import MouseReaderAdapter
            self.__reader = MouseReaderAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_readers.mouse_reader_adapter import MouseReaderAdapter
            self.__reader = MouseReaderAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_readers.mouse_reader_adapter import MouseReaderAdapter
            self.__reader = MouseReaderAdapter()

    def get_cursor_position(self):
        return self.__reader.get_cursor_position()

    def get_relative_movement(self):
        return self.__reader.get_relative_movement()

    def get_button_states(self):
        return self.__reader.get_button_states()

    def get_wheel(self):
        return self.__reader.get_wheel()

    def get_horizontal_wheel(self):
        return self.__reader.get_horizontal_wheel()
