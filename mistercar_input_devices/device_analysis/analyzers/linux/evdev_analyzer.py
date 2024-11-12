import evdev
from typing import List, Optional, Callable
from mistercar_input_devices.device_analysis.analyzers.base import DeviceAnalyzer, DeviceInfo


class EvdevAnalyzer(DeviceAnalyzer):
    """Linux device analyzer using evdev."""

    def __init__(self):
        super().__init__()
        self._device: Optional[evdev.InputDevice] = None
        self._running = False

    def list_devices(self) -> List[DeviceInfo]:
        """List all available input devices.

        Returns:
            List[DeviceInfo]: List of available devices

        Raises:
            PermissionError: If user doesn't have permission to access input devices
        """
        devices = []
        try:
            for path in evdev.list_devices():
                try:
                    device = evdev.InputDevice(path)
                    # Extract vendor and product ID from device info
                    vendor_id = device.info.vendor
                    product_id = device.info.product

                    devices.append(DeviceInfo(
                        vendor_id=vendor_id,
                        product_id=product_id,
                        name=device.name,
                        description=f"Path: {device.path}",
                        path=device.path
                    ))
                except (PermissionError, OSError) as e:
                    # Skip devices we can't access
                    continue
        except Exception as e:
            raise RuntimeError(f"Failed to list devices: {e}")

        return devices

    def open_device(self, vendor_id: int, product_id: int) -> bool:
        """Open a specific device for analysis.

        Args:
            vendor_id: USB vendor ID of the device
            product_id: USB product ID of the device

        Returns:
            bool: True if device was opened successfully

        Raises:
            PermissionError: If user doesn't have permission to access the device
            RuntimeError: If device cannot be opened
        """
        self.close_device()

        try:
            # Find device with matching vendor/product ID
            for path in evdev.list_devices():
                device = evdev.InputDevice(path)
                if (device.info.vendor == vendor_id and
                        device.info.product == product_id):
                    self._device = device
                    return True
        except Exception as e:
            raise RuntimeError(f"Failed to open device: {e}")

        return False

    def close_device(self) -> None:
        """Close the currently opened device."""
        if self._device:
            self._device.close()
            self._device = None

    def read_data(self) -> Optional[bytes]:
        """Read a single data packet from the device.

        Returns:
            Optional[bytes]: Raw input data or None if no data available

        Note:
            evdev doesn't provide raw HID data like Windows/macOS.
            This implementation converts evdev events to a standardized format.
        """
        if not self._device:
            return None

        try:
            events = self._device.read()
            if events:
                # Convert events to standardized binary format
                # This is a placeholder - actual implementation would depend
                # on how we want to standardize the data across platforms
                return bytes([event.type, event.code, event.value & 0xFF]
                             for event in events)
        except BlockingIOError:
            # No data available
            pass
        except Exception as e:
            raise RuntimeError(f"Error reading device: {e}")

        return None

    def _monitor_loop(self) -> None:
        """Internal monitoring loop.

        Note:
            Overridden to use evdev's async capabilities if needed.
        """
        try:
            while self._running:
                data = self.read_data()
                if data and self.data_callback:
                    self.data_callback(data)
        except Exception as e:
            print(f"Error in monitor loop: {e}")
            self._running = False
