import win32api as wapi
from mistercar_input_devices.backend.windows.platform_specific.keyboard.virtual_keys import vk


class KeyboardReader:
    """Read keyboard input"""

    def __init__(self):
        pass

    def get_key_state(self, key):
        if wapi.GetAsyncKeyState(vk[key]):
            return True
        else:
            return False

    def get_states_of_multiple_keys(self, keys_to_check):
        """Returns a vector of 0s and 1s describing which keys are pressed and which are not."""
        states = [0] * len(keys_to_check)
        for i in range(len(keys_to_check)):
            if wapi.GetAsyncKeyState(vk[keys_to_check[i]]):
                states[i] = 1
        return states
