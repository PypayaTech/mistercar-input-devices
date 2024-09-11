import pyautogui


class KeyboardEmulatorAdapter:
    def __init__(self):
        pass

    def emulate_key(self, key, value):
        if value == 1:
            pyautogui.keyDown(key)
        elif value == 0:
            pyautogui.keyUp(key)

    def emulate_multiple_keys(self, keys_list):
        for key in keys_list:
            self.emulate_key(key, 1)
