import math
import time
from mistercar_input_devices.input_readers.gamepad_reader import global_gamepad_reader
from mistercar_input_devices.input_emulators.gamepad_emulator import global_gamepad_emulator


def gamepad_reader_demo():
    print("=== Gamepad Reader Demo ===")
    print("Use your gamepad. This demo will run for 30 seconds.")

    start_time = time.time()
    while time.time() - start_time < 30:
        print("\n=== Gamepad State ===")

        # Read sticks
        left_stick = global_gamepad_reader.get_left_stick()
        right_stick = global_gamepad_reader.get_right_stick()
        print(f"Left Stick: {left_stick}")
        print(f"Right Stick: {right_stick}")

        # Read triggers
        triggers = global_gamepad_reader.get_triggers()
        print(f"Triggers (L, R): {triggers}")

        # Read face buttons
        face_buttons = global_gamepad_reader.get_face_buttons()
        print(f"Face Buttons [A, B, X, Y]: {face_buttons}")

        # Read shoulder buttons
        shoulder_buttons = global_gamepad_reader.get_shoulder_buttons()
        print(f"Shoulder Buttons [L, R]: {shoulder_buttons}")

        # Read dpad
        dpad = global_gamepad_reader.get_dpad()
        print(f"D-Pad [Up, Down, Left, Right]: {dpad}")

        # Read menu buttons
        menu_buttons = global_gamepad_reader.get_menu_buttons()
        print(f"Menu Buttons [Back, Start]: {menu_buttons}")

        time.sleep(0.5)

    print("\nGamepad reader demo finished.")


def gamepad_emulator_demo():
    print("\n=== Gamepad Emulator Demo ===")

    # Emulate left stick movement in a circle
    print("Moving left stick in a circle")
    for i in range(0, 360, 10):
        x = math.cos(math.radians(i))
        y = math.sin(math.radians(i))
        global_gamepad_emulator.emulate_left_stick(x, y)
        time.sleep(0.05)

    # Reset stick position
    global_gamepad_emulator.emulate_left_stick(0, 0)

    # Emulate face buttons in sequence
    print("Pressing A, B, X, Y buttons in sequence")
    for button_method in [
        global_gamepad_emulator.emulate_button_a,
        global_gamepad_emulator.emulate_button_b,
        global_gamepad_emulator.emulate_button_x,
        global_gamepad_emulator.emulate_button_y
    ]:
        button_method(True)
        time.sleep(0.2)
        button_method(False)
        time.sleep(0.2)

    # Emulate trigger presses
    print("Pressing left and right triggers")
    for i in range(0, 101, 10):
        value = i / 100
        global_gamepad_emulator.emulate_triggers(value, 1 - value)
        time.sleep(0.05)

    # Reset trigger positions
    global_gamepad_emulator.emulate_triggers(0, 0)

    # Emulate D-pad
    print("Pressing D-pad in all directions")
    global_gamepad_emulator.emulate_dpad_up(True)
    time.sleep(0.5)
    global_gamepad_emulator.emulate_dpad_up(False)

    global_gamepad_emulator.emulate_dpad_down(True)
    time.sleep(0.5)
    global_gamepad_emulator.emulate_dpad_down(False)

    global_gamepad_emulator.emulate_dpad_left(True)
    time.sleep(0.5)
    global_gamepad_emulator.emulate_dpad_left(False)

    global_gamepad_emulator.emulate_dpad_right(True)
    time.sleep(0.5)
    global_gamepad_emulator.emulate_dpad_right(False)


if __name__ == "__main__":
    gamepad_reader_demo()
    gamepad_emulator_demo()
    print("\nGamepad demo completed.")
