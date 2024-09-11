import platform


class GamepadEmulator:
    def __init__(self):
        self.__operating_system = platform.system()
        if self.__operating_system == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_emulators.gamepad_emulator_adapter import GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()
        elif self.__operating_system == "Linux":
            from mistercar_input_devices.backend.linux.adapters.input_emulators.gamepad_emulator_adapter import GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()
        elif self.__operating_system == "Darwin":
            from mistercar_input_devices.backend.macos.adapters.input_emulators.gamepad_emulator_adapter import GamepadEmulatorAdapter
            self.__emulator = GamepadEmulatorAdapter()

    def emulate_control(self, control, value=None):
        """Set a value on the controller
        If percent is True all controls will accept a value between -1.0 and 1.0

        If not then:
            Triggers are 0 to 255
            Axis are -32768 to 32767

        Control List:
            AxisLx          , Left Stick X-Axis
            AxisLy          , Left Stick Y-Axis
            AxisRx          , Right Stick X-Axis
            AxisRy          , Right Stick Y-Axis
            BtnBack         , Menu/Back Button
            BtnStart        , Start Button
            BtnA            , A Button
            BtnB            , B Button
            BtnX            , X Button
            BtnY            , Y Button
            BtnThumbL       , Left Thumbstick Click
            BtnThumbR       , Right Thumbstick Click
            BtnShoulderL    , Left Shoulder Button
            BtnShoulderR    , Right Shoulder Button
            Dpad            , Set Dpad Value (0 = Off, Use DPAD_### Constants)
            TriggerL        , Left Trigger
            TriggerR        , Right Trigger
        """
        self.__emulator.emulate_control(control, value)

    def emulate_multiple_controls(self, control_value_dict):
        self.__emulator.emulate_multiple_controls(control_value_dict)
