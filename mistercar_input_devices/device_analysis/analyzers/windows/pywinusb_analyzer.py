import pywinusb.hid as hid
from typing import List, Optional
from mistercar_input_devices.device_analysis.analyzers.base import DeviceAnalyzer, DeviceInfo


class PyWinUSBAnalyzer(DeviceAnalyzer):
    """Device analyzer using PyWinUSB"""

    def __init__(self):
        super().__init__()
        self._device = None
        self._last_data = None

    def list_devices(self) -> List[DeviceInfo]:
        devices = []
        for device in hid.find_all_hid_devices():
            devices.append(DeviceInfo(
                vendor_id=device.vendor_id,
                product_id=device.product_id,
                name=device.product_name or "Unknown Device",
                description=f"Vendor: {device.vendor_name}",
                path=device.device_path
            ))
        return devices

    def open_device(self, vendor_id: int, product_id: int) -> bool:
        """Open a specific device for analysis"""
        # Close any existing device first
        self.close_device()

        # Find and open the device
        try:
            all_devices = hid.HidDeviceFilter(
                vendor_id=vendor_id,
                product_id=product_id
            ).get_devices()

            if not all_devices:
                return False

            self._device = all_devices[0]
            self._device.open()

            # Store device info
            self.device_info = DeviceInfo(
                vendor_id=self._device.vendor_id,
                product_id=self._device.product_id,
                name=self._device.product_name or "Unknown Device",
                description=f"Vendor: {self._device.vendor_name}",
                path=self._device.device_path
            )

            # Set up data handler
            self._device.set_raw_data_handler(self._data_handler)

            return True

        except Exception as e:
            print(f"Error opening device: {e}")
            self.close_device()
            return False

    def close_device(self) -> None:
        """Close the currently opened device"""
        if self._device:
            self._device.close()
            self._device = None
            self.device_info = None

    def read_data(self) -> Optional[bytes]:
        """Return the last received data packet"""
        return self._last_data

    def _data_handler(self, data):
        """Internal callback for PyWinUSB data"""
        # Convert data to bytes
        data_bytes = bytes(data)
        self._last_data = data_bytes

        # Call user callback if set
        if self.data_callback:
            self.data_callback(data_bytes)

    def __del__(self):
        """Cleanup when object is destroyed"""
        self.close_device()
