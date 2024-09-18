import math
import time
from mistercar_input_devices.input_readers.gamepad_reader import global_gamepad_reader
from mistercar_input_devices.input_emulators.gamepad_emulator import global_gamepad_emulator


def gamepad_reader_demo():
    print("=== Gamepad Reader Demo ===")

    print("Use your gamepad. This demo will run for 30 seconds.")
    controls_to_check = [
        'AxisLx', 'AxisLy', 'AxisRx', 'AxisRy',
        'TriggerL', 'TriggerR',
        'BtnA', 'BtnB', 'BtnX', 'BtnY',
        'BtnThumbL', 'BtnThumbR',
        'BtnShoulderL', 'BtnShoulderR',
        'BtnBack', 'BtnStart',
        'Dpad'
    ]

    start_time = time.time()
    while time.time() - start_time < 30:
        # Read multiple control states
        control_states = global_gamepad_reader.get_states_of_multiple_controls(controls_to_check)

        print("\nGamepad State:")
        for control, state in zip(controls_to_check, control_states):
            print(f"{control}: {state}")

        time.sleep(0.1)

    print("\nGamepad reader demo finished.")


def gamepad_emulator_demo():
    print("\n=== Gamepad Emulator Demo ===")

    # Emulate left stick movement
    print("Moving left stick in a circle")
    for i in range(0, 360, 10):
        x = math.cos(math.radians(i))
        y = math.sin(math.radians(i))
        global_gamepad_emulator.emulate_control('AxisLx', x)
        global_gamepad_emulator.emulate_control('AxisLy', y)
        time.sleep(0.05)

    # Reset stick position
    global_gamepad_emulator.emulate_control('AxisLx', 0)
    global_gamepad_emulator.emulate_control('AxisLy', 0)

    # Emulate button presses
    print("Pressing A, B, X, Y buttons in sequence")
    for button in ['BtnA', 'BtnB', 'BtnX', 'BtnY']:
        global_gamepad_emulator.emulate_control(button, 1)
        time.sleep(0.2)
        global_gamepad_emulator.emulate_control(button, 0)
        time.sleep(0.2)

    # Emulate trigger presses
    print("Pressing left and right triggers")
    for i in range(0, 101, 10):
        value = i / 100
        global_gamepad_emulator.emulate_control('TriggerL', value)
        global_gamepad_emulator.emulate_control('TriggerR', 1 - value)
        time.sleep(0.05)

    # Reset trigger positions
    global_gamepad_emulator.emulate_control('TriggerL', 0)
    global_gamepad_emulator.emulate_control('TriggerR', 0)

    # Emulate D-pad
    print("Pressing D-pad in all directions")
    for direction in [1, 2, 4, 8]:  # Up, Down, Left, Right
        global_gamepad_emulator.emulate_control('Dpad', direction)
        time.sleep(0.5)

    # Reset D-pad
    global_gamepad_emulator.emulate_control('Dpad', 0)


if __name__ == "__main__":
    gamepad_reader_demo()
    gamepad_emulator_demo()

    print("\nGamepad demo completed.")
