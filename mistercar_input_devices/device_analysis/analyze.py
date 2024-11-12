import platform
import sys


def get_analyzer():
    system = platform.system()

    if system == "Windows":
        from mistercar_input_devices.device_analysis.analyzers.windows.pywinusb_analyzer import PyWinUSBAnalyzer
        return PyWinUSBAnalyzer()
    elif system == "Linux":
        from mistercar_input_devices.device_analysis.analyzers.linux.evdev_analyzer import EvdevAnalyzer
        return EvdevAnalyzer()
    elif system == "Darwin":
        from mistercar_input_devices.device_analysis.analyzers.macos.iokit_analyzer import IOKitAnalyzer
        return IOKitAnalyzer()
    else:
        raise NotImplementedError(f"Platform {system} is not supported")


def print_data_changes(data: bytes, last_data: list):
    """Print bytes only when they change"""
    current_data = list(data)

    # Check if data changed
    if current_data != last_data:
        # Print bytes in hex with spacing every 4 bytes for readability
        hex_values = ""
        for i, b in enumerate(current_data):
            hex_values += f'{b:02X}'
            if i < len(current_data) - 1:  # Don't add space after last byte
                hex_values += " " if (i + 1) % 4 != 0 else "  "
        print(hex_values)

        # Update last_data for next comparison
        last_data.clear()
        last_data.extend(current_data)


def main():
    try:
        analyzer = get_analyzer()
    except NotImplementedError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ImportError as e:
        print(f"Error: Required dependencies not installed for this platform: {e}")
        sys.exit(1)

    # List available devices
    print("Available devices:")
    try:
        devices = analyzer.list_devices()
        for i, device in enumerate(devices):
            print(f"{i + 1}. {device}")
    except Exception as e:
        print(f"Error listing devices: {e}")
        return

    # Get device selection from user
    if not devices:
        print("No devices found!")
        return

    while True:
        try:
            selection = int(input("\nSelect device number (or 0 to exit): "))
            if selection == 0:
                return
            if 1 <= selection <= len(devices):
                break
        except ValueError:
            pass
        print("Invalid selection!")

    device = devices[selection - 1]

    # Open selected device
    print(f"\nOpening {device.name}...")
    try:
        if not analyzer.open_device(device.vendor_id, device.product_id):
            print("Failed to open device!")
            return
    except Exception as e:
        print(f"Error opening device: {e}")
        return

    print("Device opened successfully!")
    print("\nMonitoring data changes... (Press Ctrl+C to exit)\n")

    try:
        # Store last data for comparison
        last_data = []
        analyzer.start_monitoring(lambda data: print_data_changes(data, last_data))

        # Keep main thread alive until Ctrl+C
        while True:
            pass

    except KeyboardInterrupt:
        print("\nStopping...")
    except Exception as e:
        print(f"\nError during monitoring: {e}")
    finally:
        analyzer.close_device()


if __name__ == "__main__":
    if sys.platform != "win32":
        print("This example only works on Windows!")
        sys.exit(1)
    main()
