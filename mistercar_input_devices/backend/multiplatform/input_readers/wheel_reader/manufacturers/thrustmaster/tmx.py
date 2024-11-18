import platform
from typing import Dict, Tuple, Set
from mistercar_input_devices.backend.multiplatform.input_readers.wheel_reader.base import WheelDevice, WheelState, \
    WheelButton


class TMXWheel(WheelDevice):
    """Thrustmaster TMX Racing Wheel implementation"""

    def __init__(self):
        self._adapter = None

        if platform.system() == "Windows":
            from mistercar_input_devices.backend.windows.adapters.input_readers.wheel.thrustmaster.tmx_adapter import TMXWheelAdapter
            self._adapter = TMXWheelAdapter()
        elif platform.system() == "Linux":
            raise NotImplementedError("Linux support not implemented yet")
        elif platform.system() == "Darwin":
            raise NotImplementedError("macOS support not implemented yet")
        else:
            raise NotImplementedError("Unsupported platform")

    def set_pedal_mode(self, mode: str) -> None:
        """Set the pedal mode (normal or swapped).

        In normal mode:
            - Right pedal is throttle
            - Left pedal is clutch
        In swapped mode:
            - Right pedal is clutch
            - Left pedal is throttle

        Args:
            mode: Either "normal" or "swapped"

        Raises:
            ValueError: If mode is not "normal" or "swapped"
        """
        if self._adapter:
            self._adapter.set_pedal_mode(mode)

    def get_pedal_mode(self) -> str:
        """Get current pedal mode.

        Returns:
            str: Current pedal mode ("normal" or "swapped")
        """
        if self._adapter:
            return self._adapter.get_pedal_mode()
        return "normal"  # default mode

    def get_supported_buttons(self) -> Set[WheelButton]:
        """Get set of buttons supported by this wheel"""
        return {
            WheelButton.PADDLE_LEFT,  # Left gear paddle
            WheelButton.PADDLE_RIGHT,  # Right gear paddle
            WheelButton.BUTTON_1,  # Left inner (LB)
            WheelButton.BUTTON_2,  # Right inner (RB)
            WheelButton.BUTTON_3,  # Left outer
            WheelButton.BUTTON_4,  # Right outer
            WheelButton.VIEW,  # ⧉ button
            WheelButton.MENU,  # ≡ button
            WheelButton.XBOX_A,  # Green A
            WheelButton.XBOX_B,  # Red B
            WheelButton.XBOX_X,  # Blue X
            WheelButton.XBOX_Y,  # Yellow Y
            WheelButton.XBOX_GUIDE,  # Xbox/Power button
            WheelButton.DPAD_UP,
            WheelButton.DPAD_DOWN,
            WheelButton.DPAD_LEFT,
            WheelButton.DPAD_RIGHT,
        }

    def get_state(self) -> WheelState:
        """Get the current state of all wheel controls"""
        state = self._adapter.get_state()
        if state is None:
            return WheelState()
        return state

    def get_steering(self) -> float:
        """Get steering wheel position (-1.0 to 1.0)"""
        state = self.get_state()
        return state.steering

    def get_pedals(self) -> Tuple[float, float, float]:
        """Get pedal positions (throttle, brake, clutch) from 0.0 to 1.0"""
        state = self.get_state()
        return state.throttle, state.brake, state.clutch

    def get_buttons(self) -> Dict[WheelButton, bool]:
        """Get states of all buttons"""
        state = self.get_state()
        return state.buttons

    def __del__(self):
        """Cleanup when object is destroyed"""
        if self._adapter:
            self._adapter.close()
