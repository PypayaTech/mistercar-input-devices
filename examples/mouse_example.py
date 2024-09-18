import time
from mistercar_input_devices.input_readers.mouse_reader import global_mouse_reader
from mistercar_input_devices.input_emulators.mouse_emulator import global_mouse_emulator
from mistercar_input_devices.input_readers.keyboard_reader import global_keyboard_reader


def mouse_reader_demo():
    print("=== Mouse Reader Demo ===")

    print("Move your mouse and click buttons. Press 'Q' to exit.")
    try:
        while True:
            # Check if 'Q' is pressed to exit the demo
            if global_keyboard_reader.get_key_state('Q'):
                print("\nQ pressed. Exiting mouse reader demo.")
                break

            # Read mouse position
            x, y = global_mouse_reader.get_cursor_position()
            print(f"Mouse position: ({x}, {y})")

            # Read button states
            button_states = global_mouse_reader.get_button_states()
            print(f"Button states: {button_states}")

            # Read mouse movement
            dx, dy = global_mouse_reader.get_relative_movement()
            print(f"Relative movement: ({dx}, {dy})")

            # Read scroll wheel
            scroll_v, scroll_h = global_mouse_reader.get_wheel(), global_mouse_reader.get_horizontal_wheel()
            print(f"Scroll: Vertical {scroll_v}, Horizontal {scroll_h}")

            time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")


def mouse_emulator_demo():
    print("\n=== Mouse Emulator Demo ===")

    # Move mouse
    print("Moving mouse to (100, 100)")
    global_mouse_emulator.move_cursor_to(100, 100)
    time.sleep(1)

    # Relative mouse movement
    print("Moving mouse relatively by (50, 50)")
    global_mouse_emulator.move_mouse_by(50, 50)
    time.sleep(1)

    # Left click
    print("Performing left click")
    global_mouse_emulator.left_click()
    time.sleep(1)

    # Right click
    print("Performing right click")
    global_mouse_emulator.right_click()
    time.sleep(1)

    # Double click
    print("Performing double click")
    global_mouse_emulator.left_click()
    time.sleep(0.1)
    global_mouse_emulator.left_click()
    time.sleep(1)

    # Drag and drop
    print("Performing drag and drop")
    global_mouse_emulator.move_cursor_to(200, 200)
    global_mouse_emulator.left_button_press()
    for i in range(5):
        global_mouse_emulator.move_mouse_by(10, 10)
        time.sleep(0.1)
    global_mouse_emulator.left_button_release()
    time.sleep(1)

    # Scroll
    print("Scrolling up and down")
    global_mouse_emulator.scroll(1)  # Scroll up
    time.sleep(0.5)
    global_mouse_emulator.scroll(-1)  # Scroll down
    time.sleep(1)


if __name__ == "__main__":
    mouse_reader_demo()
    mouse_emulator_demo()

    print("\nMouse demo completed.")
