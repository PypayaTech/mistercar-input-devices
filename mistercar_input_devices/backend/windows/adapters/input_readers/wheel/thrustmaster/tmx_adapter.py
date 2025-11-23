import pywinusb.hid as hid
from typing import Optional, Dict, Tuple
from mistercar_input_devices.backend.multiplatform.input_readers.wheel_reader.base import WheelButton, WheelState


class TMXWheelAdapter:
    """Windows-specific adapter for Thrustmaster TMX wheel"""

    # Device identifiers
    VENDOR_ID = 0x044F  # Thrustmaster
    PRODUCT_ID = 0xB67F  # TMX Racing Wheel

    # Constants for pedal range
    MAX_PEDAL_VALUE = 0x3FF  # Maximum observed value (1023)

    def __init__(self):
        self._device = None
        self._last_data = None
        self._pedal_mode = "normal"  # or "swapped"
        self._initialize_device()

    def get_pedal_mode(self) -> str:
        """Get current pedal mode.

        Returns:
            str: Current pedal mode ("normal" or "swapped")
        """
        return self._pedal_mode

    def set_pedal_mode(self, mode: str) -> None:
        """Set pedal signal mapping to match the MODE LED on your wheel.

        The TMX wheel MODE button swaps the left and right pedal signals:

        Green LED (normal mode):
            Left pedal → Clutch signal
            Middle pedal → Brake signal
            Right pedal → Throttle signal

        Red LED (swapped mode):
            Left pedal → Throttle signal
            Middle pedal → Brake signal
            Right pedal → Clutch signal

        Use swapped mode if your pedals are physically reversed or you
        prefer a different arrangement.

        Important: Set this to match the actual LED color on your wheel!

        Args:
            mode: Either "normal" (green LED) or "swapped" (red LED)

        Raises:
            ValueError: If mode is not "normal" or "swapped"
        """
        if mode not in ("normal", "swapped"):
            raise ValueError('Pedal mode must be either "normal" or "swapped"')
        self._pedal_mode = mode

    def _initialize_device(self):
        """Initialize connection to the wheel"""
        all_devices = hid.HidDeviceFilter(
            vendor_id=self.VENDOR_ID,
            product_id=self.PRODUCT_ID
        ).get_devices()

        if not all_devices:
            raise RuntimeError("TMX wheel not found")

        self._device = all_devices[0]
        self._device.open()
        self._device.set_raw_data_handler(self._data_handler)

    def _data_handler(self, data):
        """Handle incoming data from the wheel"""
        self._last_data = bytes(data)

    def _parse_steering(self, data: bytes) -> float:
        """Parse steering value from raw data"""
        if not data or len(data) < 3:
            return 0.0

        # Combine two bytes for full steering range
        raw_value = (data[2] << 8) | data[1]
        # Convert to -1.0 to 1.0 range
        return (raw_value - 32767) / 32767

    def _parse_pedals(self, data: bytes) -> Tuple[float, float, float]:
        """Parse pedal values from raw data.

        Pedal byte mapping:
        - Bytes 3,4: Middle pedal (always Brake)
        - Bytes 5,6: Left pedal (Clutch in normal mode, Throttle in swapped mode)
        - Bytes 7,8: Right pedal (Throttle in normal mode, Clutch in swapped mode)

        Each pedal is a 16-bit little-endian value that starts high (~1023) when
        unpressed and decreases to 0 when fully pressed.

        Returns:
            Tuple[float, float, float]: (throttle, brake, clutch) values from 0.0 to 1.0
        """
        if not data or len(data) < 9:
            return 0.0, 0.0, 0.0

        # Brake is always middle pedal (bytes 3,4)
        brake_raw = (data[4] << 8) | data[3]

        # Left and right pedal signal assignment depends on mode
        if self._pedal_mode == "normal":
            # Green LED: Standard layout
            clutch_raw = (data[6] << 8) | data[5]    # bytes 5,6 = left pedal
            throttle_raw = (data[8] << 8) | data[7]  # bytes 7,8 = right pedal
        else:  # swapped mode
            # Red LED: Swapped layout
            throttle_raw = (data[6] << 8) | data[5]  # bytes 5,6 = left pedal
            clutch_raw = (data[8] << 8) | data[7]    # bytes 7,8 = right pedal

        # Convert to 0.0-1.0 range and invert (since raw values decrease when pressed)
        return (
            max(0.0, min(1.0, 1.0 - (throttle_raw / self.MAX_PEDAL_VALUE))),
            max(0.0, min(1.0, 1.0 - (brake_raw / self.MAX_PEDAL_VALUE))),
            max(0.0, min(1.0, 1.0 - (clutch_raw / self.MAX_PEDAL_VALUE)))
        )

    def _parse_buttons(self, data: bytes) -> Dict[WheelButton, bool]:
        """Parse button states from raw data"""
        if not data or len(data) < 15:
            return {}

        buttons = {}

        # Byte 11 buttons
        buttons[WheelButton.BUTTON_1] = bool(data[11] & 0x20)  # LB
        buttons[WheelButton.BUTTON_3] = bool(data[11] & 0x08)  # Left outer
        buttons[WheelButton.PADDLE_LEFT] = bool(data[11] & 0x01)  # Left paddle
        buttons[WheelButton.PADDLE_RIGHT] = bool(data[11] & 0x02)  # Right paddle
        buttons[WheelButton.XBOX_A] = bool(data[11] & 0x10)  # A button
        buttons[WheelButton.XBOX_X] = bool(data[11] & 0x04)  # X button
        buttons[WheelButton.VIEW] = bool(data[11] & 0x40)  # ⧉ button (formerly SELECT/BACK)
        buttons[WheelButton.MENU] = bool(data[11] & 0x80)  # ≡ button (formerly START)

        # Byte 12 buttons
        buttons[WheelButton.BUTTON_2] = bool(data[12] & 0x04)  # RB
        buttons[WheelButton.BUTTON_4] = bool(data[12] & 0x08)  # Right outer
        buttons[WheelButton.XBOX_B] = bool(data[12] & 0x01)  # B button
        buttons[WheelButton.XBOX_Y] = bool(data[12] & 0x02)  # Y button
        buttons[WheelButton.XBOX_GUIDE] = bool(data[12] & 0x10)  # Xbox/Power button

        # D-pad (byte 14)
        d_pad = data[14]

        # Clear all D-pad states first
        buttons[WheelButton.DPAD_UP] = False
        buttons[WheelButton.DPAD_DOWN] = False
        buttons[WheelButton.DPAD_LEFT] = False
        buttons[WheelButton.DPAD_RIGHT] = False

        # Set D-pad states based on value
        if d_pad == 0x00:  # UP
            buttons[WheelButton.DPAD_UP] = True
        elif d_pad == 0x01:  # UP-RIGHT
            buttons[WheelButton.DPAD_UP] = True
            buttons[WheelButton.DPAD_RIGHT] = True
        elif d_pad == 0x02:  # RIGHT
            buttons[WheelButton.DPAD_RIGHT] = True
        elif d_pad == 0x03:  # DOWN-RIGHT
            buttons[WheelButton.DPAD_DOWN] = True
            buttons[WheelButton.DPAD_RIGHT] = True
        elif d_pad == 0x04:  # DOWN
            buttons[WheelButton.DPAD_DOWN] = True
        elif d_pad == 0x05:  # DOWN-LEFT
            buttons[WheelButton.DPAD_DOWN] = True
            buttons[WheelButton.DPAD_LEFT] = True
        elif d_pad == 0x06:  # LEFT
            buttons[WheelButton.DPAD_LEFT] = True
        elif d_pad == 0x07:  # UP-LEFT
            buttons[WheelButton.DPAD_UP] = True
            buttons[WheelButton.DPAD_LEFT] = True

        return buttons

    def get_state(self) -> Optional[WheelState]:
        """Get current wheel state"""
        if not self._last_data:
            return None

        steering = self._parse_steering(self._last_data)
        throttle, brake, clutch = self._parse_pedals(self._last_data)
        buttons = self._parse_buttons(self._last_data)

        return WheelState(
            steering=steering,
            throttle=throttle,
            brake=brake,
            clutch=clutch,
            buttons=buttons
        )

    def close(self):
        """Close connection to the wheel"""
        if self._device:
            self._device.close()
            self._device = None
