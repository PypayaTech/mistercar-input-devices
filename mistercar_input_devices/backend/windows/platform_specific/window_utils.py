import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32


WNDPROCTYPE = ctypes.WINFUNCTYPE(ctypes.c_longlong, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)


class WNDCLASSEX(ctypes.Structure):
    _fields_ = (
        ("cbSize", wintypes.UINT),
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROCTYPE),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HICON),
        ("hCursor", ctypes.c_void_p),
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
        ("hIconSm", wintypes.HICON),
    )


def register_window_class(wndproc, class_name):
    wndclass = WNDCLASSEX()
    wndclass.cbSize = ctypes.sizeof(WNDCLASSEX)
    wndclass.lpfnWndProc = WNDPROCTYPE(wndproc)
    wndclass.lpszClassName = class_name
    wndclass.hInstance = kernel32.GetModuleHandleW(None)

    if not user32.RegisterClassExW(ctypes.byref(wndclass)):
        raise ctypes.WinError()

    return wndclass


# https://learn.microsoft.com/en-us/windows/win32/winmsg/window-features#message-only-windows
def create_message_only_window(wndclass):
    hwnd = user32.CreateWindowExW(
        0,  # dwExStyle
        wndclass.lpszClassName,  # lpClassName
        "Message-only window",  # lpWindowName
        0,  # dwStyle
        0,  # X
        0,  # Y
        0,  # nWidth
        0,  # nHeight
        ctypes.cast(-3, wintypes.HWND),  # hWndParent (HWND_MESSAGE)
        None,  # hMenu
        ctypes.c_void_p(wndclass.hInstance),  # hInstance
        None  # lpParam
    )

    if not hwnd:
        raise ctypes.WinError()

    return hwnd


def unregister_window_class(wndclass):
    user32.UnregisterClassW(wndclass.lpszClassName, kernel32.GetModuleHandleW(None))
