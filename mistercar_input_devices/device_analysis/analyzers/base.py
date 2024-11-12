from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Callable, Any, Dict
import threading
import time


@dataclass
class DeviceInfo:
    """Basic information about a USB device"""
    vendor_id: int
    product_id: int
    name: str
    description: str = ""
    path: str = ""

    def __str__(self):
        return f"{self.name} (VID: 0x{self.vendor_id:04x}, PID: 0x{self.product_id:04x})"


class DeviceAnalyzer(ABC):
    """Base class for device analyzers"""

    def __init__(self):
        self.data_callback: Optional[Callable[[bytes], None]] = None
        self.device_info: Optional[DeviceInfo] = None
        self._monitoring_thread: Optional[threading.Thread] = None
        self._running = False

    @abstractmethod
    def list_devices(self) -> List[DeviceInfo]:
        """List all available devices"""
        pass

    @abstractmethod
    def open_device(self, vendor_id: int, product_id: int) -> bool:
        """Open a specific device for analysis"""
        pass

    @abstractmethod
    def close_device(self) -> None:
        """Close the currently opened device"""
        pass

    @abstractmethod
    def read_data(self) -> Optional[bytes]:
        """Read a single data packet from the device
        Returns None if no data is available"""
        pass

    def start_monitoring(self, callback: Callable[[bytes], None]) -> None:
        """Start monitoring device data with a callback

        callback will be called with each data packet received
        """
        if self._monitoring_thread is not None:
            raise RuntimeError("Already monitoring")

        self.data_callback = callback
        self._running = True
        self._monitoring_thread = threading.Thread(target=self._monitor_loop)
        self._monitoring_thread.daemon = True
        self._monitoring_thread.start()

    def stop_monitoring(self) -> None:
        """Stop monitoring device data"""
        self._running = False
        if self._monitoring_thread:
            self._monitoring_thread.join()
            self._monitoring_thread = None

    def _monitor_loop(self) -> None:
        """Internal monitoring loop"""
        while self._running:
            data = self.read_data()
            if data and self.data_callback:
                self.data_callback(data)
            time.sleep(0.001)  # Prevent 100% CPU usage
