import ctypes
import threading
import os
import sys
from ctypes import windll, wintypes, CFUNCTYPE

# Constants from the Windows API
WHEEL_DELTA = 120
WM_MOUSEWHEEL = 0x020A
WM_MOUSEHWHEEL = 0x020E

# Mapping of WM_MOUSEWHEEL and WM_MOUSEHWHEEL to scroll vectors
SCROLL_BUTTONS = {
    WM_MOUSEWHEEL: (0, 1),
    WM_MOUSEHWHEEL: (1, 0)
}


class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("pt", wintypes.POINT),
        ("mouseData", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


HOOKPROC = CFUNCTYPE(wintypes.LPARAM, ctypes.c_int, wintypes.WPARAM, ctypes.POINTER(MSLLHOOKSTRUCT))


class ScrollReader:
    def __init__(self):
        self._user32 = windll.user32
        self._k32 = windll.kernel32
        self._msg = wintypes.MSG()
        self._hooked = None
        self._mouse_hook = HOOKPROC(self._low_level_mouse_proc)
        self._thread = threading.Thread(target=self.run, args=())
        self._up_scroll_count = 0
        self._down_scroll_count = 0
        self._is_alive = True

    def run(self):
        try:
            self._set_hook()
            while self._is_alive and self._user32.GetMessageA(ctypes.byref(self._msg), 0, 0, 0) != 0:
                self._user32.TranslateMessage(ctypes.byref(self._msg))
                self._user32.DispatchMessageA(ctypes.byref(self._msg))
        except Exception as ex:
            print(f"Error occurred in thread: {ex}")

    def start(self):
        self._thread.start()

    def stop(self):
        self._is_alive = False
        self._user32.PostThreadMessageW(self._thread.ident, 0x0012, 0, 0)  # 0x0012 is WM_QUIT
        if self._thread.is_alive():
            self._thread.join()
        self._remove_hook()

    def get_scroll_counts(self):
        up_count = self._up_scroll_count
        down_count = self._down_scroll_count
        self._up_scroll_count = 0
        self._down_scroll_count = 0
        return up_count, down_count

    def _on_scroll(self, _, __, dx, dy):
        if dx == 0 and dy > 0:
            self._up_scroll_count += 1
        elif dx == 0 and dy < 0:
            self._down_scroll_count += 1

    def _get_module_handle(self):
        if hasattr(sys, "frozen") and sys.frozen in ("windows_exe", "console_exe"):  # Pyinstaller compatibility
            hMod = self._k32.GetModuleHandleW(None)
        else:
            hMod = self._k32.GetModuleHandleW(ctypes.c_wchar_p(os.path.abspath(__file__)))
        return hMod

    def _low_level_mouse_proc(self, nCode, wParam, lParam):
        if nCode == 0 and wParam in [WM_MOUSEWHEEL, WM_MOUSEHWHEEL]:
            mouse_struct = lParam.contents
            wm_mouse_scroll = wParam
            mx, my = SCROLL_BUTTONS[wm_mouse_scroll]
            dd = wintypes.SHORT(mouse_struct.mouseData >> 16).value // WHEEL_DELTA
            self._on_scroll(mouse_struct.pt.x, mouse_struct.pt.y, dd * mx, dd * my)
        return self._user32.CallNextHookEx(None, nCode, wParam, lParam)

    def _set_hook(self):
        self._hooked = self._user32.SetWindowsHookExW(14, self._mouse_hook, self._get_module_handle(), 0)
        if not self._hooked:
            print("Failed to install hook")
            sys.exit(1)

    def _remove_hook(self):
        if self._hooked is not None:
            self._user32.UnhookWindowsHookEx(self._hooked)
            self._hooked = None
