

class MouseReaderAdapter:
    def __init__(self):
        pass

    def get_cursor_position(self):
        raise NotImplementedError

    def get_relative_movement(self):
        raise NotImplementedError

    def get_button_states(self):
        raise NotImplementedError

    def get_wheel(self):
        raise NotImplementedError

    def get_horizontal_wheel(self):
        raise NotImplementedError
