from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Tuple, Set
from enum import IntEnum, auto


class WheelButton(IntEnum):
    """Standard wheel button mappings"""

    # Core buttons (present on most wheels)
    PADDLE_LEFT = auto()  # Left paddle shifter
    PADDLE_RIGHT = auto()  # Right paddle shifter
    BUTTON_1 = auto()  # Primary action button
    BUTTON_2 = auto()  # Secondary action button
    DPAD_UP = auto()
    DPAD_DOWN = auto()
    DPAD_LEFT = auto()
    DPAD_RIGHT = auto()

    # Extended buttons (common but not universal)
    BUTTON_3 = auto()
    BUTTON_4 = auto()
    VIEW = auto()  # ⧉ button (formerly SELECT/BACK)
    MENU = auto()  # ≡ button (formerly START)

    # Console-specific buttons (same physical positions, different labels)
    XBOX_A = auto()  # Xbox: Green A  | PlayStation: Blue Cross (×)
    XBOX_B = auto()  # Xbox: Red B    | PlayStation: Red Circle (○)
    XBOX_X = auto()  # Xbox: Blue X   | PlayStation: Pink Square (□)
    XBOX_Y = auto()  # Xbox: Yellow Y | PlayStation: Green Triangle (△)
    XBOX_GUIDE = auto()  # Xbox: Guide    | PlayStation: PS button

    # Advanced features
    CLUTCH_PADDLE_LEFT = auto()  # Additional clutch paddle
    CLUTCH_PADDLE_RIGHT = auto()  # Some high-end wheels have dual clutch
    DIAL_1 = auto()  # Rotary encoder/dial
    DIAL_2 = auto()  # Additional dial


@dataclass
class WheelState:
    """Represents the current state of a racing wheel"""
    # Main controls (-1.0 to 1.0 for steering, 0.0 to 1.0 for pedals)
    steering: float = 0.0  # -1.0 = full left, 1.0 = full right
    throttle: float = 0.0  # 0.0 = no throttle, 1.0 = full throttle
    brake: float = 0.0  # 0.0 = no brake, 1.0 = full brake
    clutch: float = 0.0  # 0.0 = no clutch, 1.0 = full clutch

    # Button states
    buttons: Dict[WheelButton, bool] = None

    def __post_init__(self):
        if self.buttons is None:
            self.buttons = {}

    def is_button_supported(self, button: WheelButton) -> bool:
        """Check if a button is supported by this wheel"""
        return button in self.buttons


class WheelDevice(ABC):
    """Abstract base class for all wheel devices"""

    @abstractmethod
    def get_supported_buttons(self) -> Set[WheelButton]:
        """Get set of buttons supported by this wheel"""
        pass

    @abstractmethod
    def get_state(self) -> WheelState:
        """Get the current state of all wheel controls"""
        pass

    @abstractmethod
    def get_steering(self) -> float:
        """Get steering wheel position (-1.0 to 1.0)"""
        pass

    @abstractmethod
    def get_pedals(self) -> Tuple[float, float, float]:
        """Get pedal positions (throttle, brake, clutch) from 0.0 to 1.0"""
        pass

    @abstractmethod
    def get_buttons(self) -> Dict[WheelButton, bool]:
        """Get states of all buttons"""
        pass

    def supports_force_feedback(self) -> bool:
        """Whether the device supports force feedback"""
        return False

    def set_force_feedback(self, strength: float) -> None:
        """Set force feedback strength if supported"""
        raise NotImplementedError("Force feedback not supported")
