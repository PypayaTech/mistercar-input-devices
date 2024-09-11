from mistercar_input_devices.backend.windows.platform_specific.keyboard import keyboard_reader as wkr


class KeyboardReaderAdapter:
    def __init__(self):
        self.__kb_reader = wkr.KeyboardReader()

    def get_key_state(self, key):
        return self.__kb_reader.get_key_state(key)

    def get_states_of_multiple_keys(self, keys_to_check):
        return self.__kb_reader.get_states_of_multiple_keys(keys_to_check)
