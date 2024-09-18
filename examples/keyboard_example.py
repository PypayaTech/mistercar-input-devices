import time
from mistercar_input_devices.input_readers.keyboard_reader import global_keyboard_reader
from mistercar_input_devices.input_emulators.keyboard_emulator import global_keyboard_emulator


def keyboard_reader_demo():
    print("=== Keyboard Reader Demo ===")

    print("Press keys on your keyboard. Press Esc to exit.")
    keys_to_check = ['A', 'S', 'D', 'W', 'SPACE', 'LSHIFT', 'LCTRL']

    while True:
        # Check individual key state
        if global_keyboard_reader.get_key_state('ESC'):
            print("\nEsc pressed. Exiting keyboard reader demo.")
            break

        # Check multiple key states
        key_states = global_keyboard_reader.get_states_of_multiple_keys(keys_to_check)
        pressed_keys = [key for key, state in zip(keys_to_check, key_states) if state]

        if pressed_keys:
            print(f"Pressed keys: {', '.join(pressed_keys)}")

        time.sleep(0.1)


def keyboard_emulator_demo():
    print("\n=== Keyboard Emulator Demo ===")

    # Type a string
    text = "Hello, World!"
    print(f"Typing: {text}")
    for char in text:
        global_keyboard_emulator.emulate_key(char, 1)  # Press
        time.sleep(0.05)
        global_keyboard_emulator.emulate_key(char, 0)  # Release
        time.sleep(0.05)

    time.sleep(1)

    # Simulate key combinations
    print("Simulating Ctrl+C (copy)")
    global_keyboard_emulator.emulate_key('LCTRL', 1)
    global_keyboard_emulator.emulate_key('C', 1)
    time.sleep(0.1)
    global_keyboard_emulator.emulate_key('C', 0)
    global_keyboard_emulator.emulate_key('LCTRL', 0)

    time.sleep(1)

    print("Simulating Alt+Tab")
    global_keyboard_emulator.emulate_key('LALT', 1)
    global_keyboard_emulator.emulate_key('TAB', 1)
    time.sleep(0.1)
    global_keyboard_emulator.emulate_key('TAB', 0)
    global_keyboard_emulator.emulate_key('LALT', 0)

    # Simulate holding a key
    print("Holding 'W' key for 2 seconds")
    global_keyboard_emulator.emulate_key('W', 1)
    time.sleep(2)
    global_keyboard_emulator.emulate_key('W', 0)


if __name__ == "__main__":
    keyboard_reader_demo()
    keyboard_emulator_demo()

    print("\nKeyboard demo completed.")
