# 🎮 mistercar-input-devices

A cross-platform Python package for capturing and emulating keyboard, mouse, and gamepad inputs.

## 🌟 Features

- ⌨️ Keyboard input capture and emulation
- 🖱️ Mouse input capture and emulation
- 🕹️ Gamepad input capture and emulation
- 🖥️ Cross-platform support (Windows, macOS, Linux)

## 🚀 Installation

You can install mistercar-input-devices using pip:

```bash
pip install mistercar-input-devices
```

### 📋 Prerequisites

- Python 3.10 or higher

#### Windows-specific setup

1. Disable driver signature enforcement. This is necessary for installing unsigned drivers. Follow the instructions in this guide: [How to disable driver signature enforcement on Windows 10](https://medium.com/@pypaya_tech/unlock-your-windows-a-guide-to-disabling-driver-signature-enforcement-342103d51997)

2. Open a command prompt as an administrator.

3. Navigate to the appropriate directory:
   - For 64-bit systems: `cd path\to\mistercar_input_devices\backend\windows\platform_specific\pyxinput\ScpVBus-x64`
   - For 32-bit systems: `cd path\to\mistercar_input_devices\backend\windows\platform_specific\pyxinput\ScpVBus-x86`

4. Run the following command:
   ```
   devcon.exe install ScpVBus.inf Root\ScpVBus
   ```

## 🎯 Usage

Here are some basic examples of how to use mistercar-input-devices:

### ⌨️ Keyboard

```python
from mistercar_input_devices.input_readers.keyboard_reader import global_keyboard_reader
from mistercar_input_devices.input_emulators.keyboard_emulator import global_keyboard_emulator

# Check if a key is pressed
if global_keyboard_reader.get_key_state('A'):
    print("A key is pressed")

# Press a key
global_keyboard_emulator.emulate_key('B', 1)  # Press
global_keyboard_emulator.emulate_key('B', 0)  # Release
```

### 🖱️ Mouse

```python
from mistercar_input_devices.input_readers.mouse_reader import global_mouse_reader
from mistercar_input_devices.input_emulators.mouse_emulator import global_mouse_emulator

# Read mouse position
x, y = global_mouse_reader.get_cursor_position()
print(f"Mouse position: {x}, {y}")

# Move mouse
global_mouse_emulator.move_cursor_to(100, 100)

# Click
global_mouse_emulator.left_click()
```

### 🕹️ Gamepad

```python
from mistercar_input_devices.input_readers.gamepad_reader import global_gamepad_reader
from mistercar_input_devices.input_emulators.gamepad_emulator import global_gamepad_emulator

# Read gamepad state
gamepad_state = global_gamepad_reader.get_control_state('AxisLx')
print(f"Left stick X-axis: {gamepad_state}")

# Emulate gamepad input
global_gamepad_emulator.emulate_control('AxisLx', 0.5)  # Move left stick halfway to the right
```

## 🚀 Examples

Check out the `examples` directory for comprehensive demonstrations of the library's capabilities. We provide three example scripts:

1. `keyboard_example.py`: Demonstrates keyboard input reading and emulation.
2. `mouse_example.py`: Shows mouse input reading and emulation.
3. `gamepad_example.py`: Illustrates gamepad input reading and emulation.

## 📊 Implementation status

The current implementation status of mistercar-input-devices across different platforms:

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| Keyboard Reader | ✅ | ❌ | ❌ |
| Keyboard Emulator | ✅ | ✅ | ✅ |
| Mouse Reader | ✅ | ❌ | ❌ |
| Mouse Emulator | ✅ | ✅ | ✅ |
| Gamepad Reader | ✅ | ❌ | ❌ |
| Gamepad Emulator | ✅ | ❌ | ❌ |

Legend:
- ✅ Fully implemented
- ⚠️ Partially implemented or needs testing
- ❌ Not yet implemented

### Notes on implementation

- Windows: Custom low-level implementation for all features, ensuring reliability in various contexts, including video games.
- Linux and macOS: 
  - Keyboard and Mouse emulation use PyAutoGUI, which works well in most contexts but may have limitations in some video games.
  - Keyboard and Mouse reading functionality is not yet implemented.
  - Gamepad functionality is not yet implemented.

### Roadmap

- Implement keyboard and mouse reading functionality for Linux and macOS platforms.
- Implement gamepad support for Linux and macOS.
- Enhance cross-platform compatibility and consistency.
- Explore options for more reliable input methods in game contexts for Linux and macOS.

We welcome contributions to help improve and extend the library's functionality across all supported platforms!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Special thanks to the creators of these libraries and projects that have been instrumental in the development of mistercar-input-devices:

- [PYXInput](https://github.com/bayangan1991/PYXInput): For gamepad reading and emulation implementation on Windows.
- [pygta5](https://github.com/Sentdex/pygta5): For inspiration from the self-driving car GTA V project and the `keys.py` file, which was particularly helpful for implementing keyboard emulation on Windows.
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/): For providing cross-platform keyboard and mouse emulation capabilities, especially utilized in our Linux and macOS implementations.

We are grateful for the open-source community and these projects that have made our work possible.
