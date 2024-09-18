from mistercar_input_devices.backend.windows.platform_specific.mouse import mouse_reader as wmr


class MouseReaderAdapter:
    def __init__(self):
        self.__mouse_reader = wmr.MouseReader()

    def get_cursor_position(self):
        return self.__mouse_reader.get_cursor_position()

    def get_relative_movement(self):
        return self.__mouse_reader.get_relative_movement()

    def get_button_states(self):
        return self.__mouse_reader.get_button_states()

    def get_wheel(self):
        return self.__mouse_reader.get_wheel()

    def get_horizontal_wheel(self):
        return self.__mouse_reader.get_horizontal_wheel()
