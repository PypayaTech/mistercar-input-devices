MOUSEEVENTF_MOVE = 0x0001  # Movement occurred.

MOUSEEVENTF_LEFTDOWN = 0x0002  # The left button was pressed.

MOUSEEVENTF_LEFTUP = 0x0004  # The left button was released.

MOUSEEVENTF_RIGHTDOWN = 0x0008  # The right button was pressed.

MOUSEEVENTF_RIGHTUP = 0x0010  # The right button was released.

MOUSEEVENTF_MIDDLEDOWN = 0x0020  # The middle button was pressed.

MOUSEEVENTF_MIDDLEUP = 0x0040  # The middle button was released.

MOUSEEVENTF_XDOWN = 0x0080  # An X button was pressed.

MOUSEEVENTF_XUP = 0x0100  # An X button was released.

MOUSEEVENTF_WHEEL = 0x0800  # The wheel was moved, if the mouse has a wheel.
# The amount of movement is specified in mouseData.

MOUSEEVENTF_HWHEEL = 0x1000  # The wheel was moved horizontally, if the mouse has a wheel.
# The amount of movement is specified in mouseData.
# Windows XP/2000: This value is not supported.

MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000  # The WM_MOUSEMOVE messages will not be coalesced.
# The default behavior is to coalesce WM_MOUSEMOVE messages.
# Windows XP/2000: This value is not supported.

MOUSEEVENTF_VIRTUALDESK = 0x4000  # Maps coordinates to the entire desktop.
# Must be used with MOUSEEVENTF_ABSOLUTE.

MOUSEEVENTF_ABSOLUTE = 0x8000
# The dx and dy members contain normalized absolute coordinates.
# If the flag is not set, dx and dy contain relative data (the change in position since the last reported position).
# This flag can be set, or not set, regardless of what kind of mouse or other pointing device, if any,
# is connected to the system. For further information about relative mouse motion, see the following Remarks section:
# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput#remarks
