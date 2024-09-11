import platform


class KeyboardReader:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_readers.keyboard_reader_adapter import KeyboardReaderAdapter
            self.__reader = KeyboardReaderAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_readers.keyboard_reader_adapter import KeyboardReaderAdapter
            self.__reader = KeyboardReaderAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_readers.keyboard_reader_adapter import KeyboardReaderAdapter
            self.__reader = KeyboardReaderAdapter()

    def get_key_state(self, key):
        return self.__reader.get_key_state(key)

    def get_states_of_multiple_keys(self, keys_to_check):
        return self.__reader.get_states_of_multiple_keys(keys_to_check)
