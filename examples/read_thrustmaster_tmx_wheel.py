import time
from typing import Dict, Optional
from mistercar_input_devices.backend.multiplatform.input_readers.wheel_reader.base import WheelState, WheelButton
from mistercar_input_devices.input_readers.wheel_reader.manufacturers.thrustmaster.tmx import global_tmx_wheel


class WheelTester:
    def __init__(self):
        self.last_state: Optional[WheelState] = None

    def _has_state_changed(self, current: WheelState, last: WheelState) -> bool:
        """Check if any wheel state values have changed."""
        if last is None:
            return True

        # Check analog values with small threshold to avoid float comparison issues
        threshold = 0.001
        if (abs(current.steering - last.steering) > threshold or
                abs(current.throttle - last.throttle) > threshold or
                abs(current.brake - last.brake) > threshold or
                abs(current.clutch - last.clutch) > threshold):
            return True

        # Check buttons
        if current.buttons != last.buttons:
            return True

        return False

    def _format_analog_value(self, name: str, value: float) -> str:
        """Format analog value for display."""
        return f"{name}: {value:7.3f}"

    def _format_buttons(self, buttons: Dict[WheelButton, bool]) -> str:
        """Format button states for display."""
        active_buttons = [button.name for button, pressed in buttons.items() if pressed]
        if not active_buttons:
            return "No buttons pressed"
        return "Buttons: " + ", ".join(active_buttons)

    def print_state_changes(self, state: WheelState):
        """Print wheel state if it has changed."""
        if not self._has_state_changed(state, self.last_state):
            return

        # Clear line and move cursor to start
        print('\r' + ' ' * 100 + '\r', end='')

        # Print analog values
        analog_values = [
            self._format_analog_value("Steering", state.steering),
            self._format_analog_value("Throttle", state.throttle),
            self._format_analog_value("Brake", state.brake),
            self._format_analog_value("Clutch", state.clutch)
        ]
        print(" | ".join(analog_values))

        # Print active buttons on new line
        print(self._format_buttons(state.buttons))
        print()  # Empty line for better readability

        self.last_state = state


def main():
    print("Testing TMX Wheel implementation")
    print("Press Ctrl+C to exit\n")
    print("Interact with the wheel to see state changes...")
    print("=" * 80)

    tester = WheelTester()

    try:
        while True:
            state = global_tmx_wheel.get_state()
            tester.print_state_changes(state)
            time.sleep(0.01)  # Small delay to prevent CPU overuse

    except KeyboardInterrupt:
        print("\nTest finished.")
    except Exception as e:
        print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
