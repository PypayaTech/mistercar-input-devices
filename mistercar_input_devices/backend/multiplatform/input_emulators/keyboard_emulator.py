import platform


class KeyboardEmulator:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_emulators.keyboard_emulator_adapter import KeyboardEmulatorAdapter
            self.__emulator = KeyboardEmulatorAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_emulators.keyboard_emulator_adapter import KeyboardEmulatorAdapter
            self.__emulator = KeyboardEmulatorAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_emulators.keyboard_emulator_adapter import KeyboardEmulatorAdapter
            self.__emulator = KeyboardEmulatorAdapter()

    def emulate_key(self, key, value):
        self.__emulator.emulate_key(key, value)

    def emulate_multiple_keys(self, keys_list):
        self.__emulator.emulate_multiple_keys(keys_list)
