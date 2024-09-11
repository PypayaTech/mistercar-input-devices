from mistercar_input_devices.backend.windows.platform_specific.keys_and_mouse import KeysAndMouse, KEY_RELEASE


class KeyboardEmulatorAdapter:
    def __init__(self):
        self._keys_and_mouse = KeysAndMouse()

    def emulate_key(self, key, value):
        if value == 0:
            self._keys_and_mouse.direct_key(key, KEY_RELEASE)
        else:
            self._keys_and_mouse.direct_key(key)

    def emulate_multiple_keys(self, keys_list):
        for key in keys_list:
            self._keys_and_mouse.direct_key(key)
