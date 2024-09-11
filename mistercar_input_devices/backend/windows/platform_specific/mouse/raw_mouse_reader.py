import ctypes
import threading
from ctypes import wintypes
from win32con import WM_QUIT, SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_CXSCREEN, \
    SM_CYSCREEN
from mistercar_input_devices.backend.windows.platform_specific.structures import RAWINPUTDEVICE, RAWINPUTHEADER, \
    RAWINPUT
from mistercar_input_devices.backend.windows.platform_specific.window_utils import register_window_class, \
    create_message_only_window, unregister_window_class

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Constants from the Windows API
RID_INPUT = 0x10000003
WM_INPUT = 0x00FF
RIDEV_INPUTSINK = 0x00000100

# Constants for raw mouse input

WHEEL_DELTA = 120

# usFlags

MOUSE_MOVE_RELATIVE = 0x00  # Mouse movement data is relative to the last mouse position.
# For further information about mouse motion, see the following Remarks section.

MOUSE_MOVE_ABSOLUTE = 0x01  # Mouse movement data is based on absolute position.
# For further information about mouse motion, see the following Remarks section.

MOUSE_VIRTUAL_DESKTOP = 0x02  # Mouse coordinates are mapped to the virtual desktop (for a multiple monitor system).
# For further information about mouse motion, see the following Remarks section.

MOUSE_ATTRIBUTES_CHANGED = 0x04  # Mouse attributes changed; application needs to query the mouse attributes.

MOUSE_MOVE_NOCOALESCE = 0x08  # This mouse movement event was not coalesced. Mouse movement events can be coalesced by default.
# Windows XP/2000: This value is not supported.

# usButtonFlags

# Left button changed to down.
RI_MOUSE_BUTTON_1_DOWN = 0x0001
RI_MOUSE_LEFT_BUTTON_DOWN = RI_MOUSE_BUTTON_1_DOWN

# Left button changed to up.
RI_MOUSE_BUTTON_1_UP = 0x0002
RI_MOUSE_LEFT_BUTTON_UP = RI_MOUSE_BUTTON_1_UP

# Right button changed to down.
RI_MOUSE_BUTTON_2_DOWN = 0x0004
RI_MOUSE_RIGHT_BUTTON_DOWN = RI_MOUSE_BUTTON_2_DOWN

# Right button changed to up.
RI_MOUSE_BUTTON_2_UP = 0x0008
RI_MOUSE_RIGHT_BUTTON_UP = RI_MOUSE_BUTTON_2_UP

# Middle button changed to down.
RI_MOUSE_BUTTON_3_DOWN = 0x0010
RI_MOUSE_MIDDLE_BUTTON_DOWN = RI_MOUSE_BUTTON_3_DOWN

# Middle button changed to up.
RI_MOUSE_BUTTON_3_UP = 0x0020
RI_MOUSE_MIDDLE_BUTTON_UP = RI_MOUSE_BUTTON_3_UP

# XBUTTON1 changed to down.
RI_MOUSE_BUTTON_4_DOWN = 0x0040

# XBUTTON1 changed to up.
RI_MOUSE_BUTTON_4_UP = 0x0080

# XBUTTON2 changed to down.
RI_MOUSE_BUTTON_5_DOWN = 0x0100

# XBUTTON2 changed to up.
RI_MOUSE_BUTTON_5_UP = 0x0200

# Raw input comes from a mouse wheel.
RI_MOUSE_WHEEL = 0x0400

# Raw input comes from a horizontal mouse wheel.
RI_MOUSE_HWHEEL = 0x0800


class RawMouseReader:
    def __init__(self):
        self._thread = None
        self._is_alive = True
        self._hwnd = None
        self._wndclass = None
        self._absolute_x = 0
        self._absolute_y = 0
        self._relative_x = 0
        self._relative_y = 0
        self._wheel_up = 0
        self._wheel_down = 0
        self._hwheel_left = 0
        self._hwheel_right = 0
        self._lock = threading.Lock()

    def start(self):
        self._thread = threading.Thread(target=self._run, args=())
        self._thread.start()

    def stop(self):
        self._is_alive = False
        user32.PostThreadMessageW(self._thread.ident, WM_QUIT, 0, 0)
        if self._thread.is_alive():
            self._thread.join()
        if self._hwnd is not None:
            user32.DestroyWindow(self._hwnd)
            unregister_window_class(self._wndclass)

    def get_absolute_position(self):
        with self._lock:
            return self._absolute_x, self._absolute_y

    def get_relative_movement(self):
        with self._lock:
            relative_x, relative_y = self._relative_x, self._relative_y
            self._relative_x = self._relative_y = 0
            return relative_x, relative_y

    def get_wheel_delta(self):
        with self._lock:
            wheel_up, wheel_down = self._wheel_up, self._wheel_down
            self._wheel_up = self._wheel_down = 0
            return wheel_up, wheel_down

    def get_hwheel_delta(self):
        with self._lock:
            hwheel_left, hwheel_right = self._hwheel_left, self._hwheel_right
            self._hwheel_left = self._hwheel_right = 0
            return hwheel_left, hwheel_right

    def _run(self):
        # Register window class and create message-only window
        self._wndclass = register_window_class(self._wndproc, "MyMessageOnlyWindowClass")
        self._hwnd = create_message_only_window(self._wndclass)

        # Define the mouse usage page and usage
        RID_USAGE_PAGE_GENERIC = 0x01
        RID_USAGE_MOUSE = 0x02

        # Register the raw input device
        rid = RAWINPUTDEVICE()
        rid.usUsagePage = RID_USAGE_PAGE_GENERIC
        rid.usUsage = RID_USAGE_MOUSE
        rid.dwFlags = RIDEV_INPUTSINK
        rid.hwndTarget = self._hwnd

        if user32.RegisterRawInputDevices(ctypes.byref(rid), 1, ctypes.sizeof(rid)) == False:
            raise ctypes.WinError(ctypes.get_last_error())

        # Message loop
        msg = wintypes.MSG()
        while self._is_alive and user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

    def _wndproc(self, hwnd, msg, wparam, lparam):
        if msg == WM_INPUT:
            raw = RAWINPUT()
            sz = ctypes.c_uint(ctypes.sizeof(raw))
            szHeader = ctypes.c_uint(ctypes.sizeof(RAWINPUTHEADER))
            result = user32.GetRawInputData(lparam, RID_INPUT, ctypes.byref(raw), ctypes.byref(sz), szHeader)
            if result == sz.value:
                with self._lock:
                    if raw.data.mouse.usFlags & MOUSE_MOVE_ABSOLUTE:
                        if raw.data.mouse.usFlags & MOUSE_VIRTUAL_DESKTOP:
                            left = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
                            top = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
                            width = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
                            height = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
                        else:
                            left = 0
                            top = 0
                            width = user32.GetSystemMetrics(SM_CXSCREEN)
                            height = user32.GetSystemMetrics(SM_CYSCREEN)

                        self._absolute_x = int((raw.data.mouse.lLastX / 65535.0) * width) + left
                        self._absolute_y = int((raw.data.mouse.lLastY / 65535.0) * height) + top
                    else:
                        self._relative_x += raw.data.mouse.lLastX
                        self._relative_y += raw.data.mouse.lLastY

                    if raw.data.mouse.union.Buttons.usButtonFlags & RI_MOUSE_WHEEL:
                        wheel_delta = self._normalize_wheel_data(raw.data.mouse.union.Buttons.usButtonData)
                        if wheel_delta > 0:
                            self._wheel_up += wheel_delta
                        else:
                            self._wheel_down += abs(wheel_delta)
                    elif raw.data.mouse.union.Buttons.usButtonFlags & RI_MOUSE_HWHEEL:
                        hwheel_delta = self._normalize_wheel_data(raw.data.mouse.union.Buttons.usButtonData)
                        if hwheel_delta > 0:
                            self._hwheel_right += hwheel_delta
                        else:
                            self._hwheel_left += abs(hwheel_delta)
            else:
                print("GetRawInputData didn't return correct size")

        wparam = wintypes.WPARAM(wparam)
        lparam = wintypes.LPARAM(lparam)
        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

    def _normalize_wheel_data(self, wheel_data):
        """
        The mouse wheel delta values come in as a multiple of WHEEL_DELTA (120).
        If the scroll is upwards or to the right, the value is positive,
        while downwards or to the left is negative.
        However, these values are unsigned 16-bit integers. In the case of
        downward/leftward scroll, Windows represents it as a two's complement
        negative number.
        This helper function takes the raw wheel data, figures out if it's really
        a negative number in disguise, and if so converts it to standard negative
        format. Finally, it normalizes the delta to -1 (for down/left) or +1
        (for up/right).
        """
        if wheel_data > 32767:
            wheel_data -= 65536
        return wheel_data // WHEEL_DELTA
