import ctypes
from _ctypes import Structure, Union
from ctypes import wintypes


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)))


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)))


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-hardwareinput
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_ushort),
                ("wParamH", ctypes.c_ushort))


class _INPUTunion(ctypes.Union):
    _fields_ = (("mi", MOUSEINPUT),
                ("ki", KEYBDINPUT),
                ("hi", HARDWAREINPUT))


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
class INPUT(ctypes.Structure):
    _fields_ = (("type", ctypes.c_ulong),
                ("union", _INPUTunion))


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawinputdevice
class RAWINPUTDEVICE(Structure):
    _fields_ = (
        ("usUsagePage", wintypes.USHORT),
        ("usUsage", wintypes.USHORT),
        ("dwFlags", wintypes.DWORD),
        ("hwndTarget", wintypes.HWND)
    )


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawinputheader
class RAWINPUTHEADER(Structure):
    _fields_ = (
        ("dwType", wintypes.DWORD),
        ("dwSize", wintypes.DWORD),
        ("hDevice", wintypes.HANDLE),
        ("wParam", wintypes.WPARAM)
    )


#
class RAWMOUSE_BUTTONS(Structure):
    _fields_ = (
        ("usButtonFlags", wintypes.USHORT),
        ("usButtonData", wintypes.USHORT)
    )


class RAWMOUSE_UNION(Union):
    _fields_ = (
        ("ulButtons", wintypes.ULONG),
        ("Buttons", RAWMOUSE_BUTTONS)
    )


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawmouse
class RAWMOUSE(Structure):
    _fields_ = (
        ("usFlags", wintypes.USHORT),
        ("union", RAWMOUSE_UNION),
        ("ulRawButtons", wintypes.ULONG),
        ("lLastX", wintypes.LONG),
        ("lLastY", wintypes.LONG),
        ("ulExtraInformation", wintypes.ULONG)
    )


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawkeyboard
class RAWKEYBOARD(Structure):
    _fields_ = (
        ("MakeCode", wintypes.USHORT),
        ("Flags", wintypes.USHORT),
        ("Reserved", wintypes.USHORT),
        ("VKey", wintypes.USHORT),
        ("Message", wintypes.UINT),
        ("ExtraInformation", wintypes.ULONG)
    )


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawhid
class RAWHID(Structure):
    _fields_ = (
        ("dwSizeHid", wintypes.DWORD),
        ("dwCount", wintypes.DWORD),
        ("bRawData", wintypes.BYTE * 1)  # Array of bytes of size 1
    )


class RAWINPUT_DATA(Union):
    _fields_ = (
        ("mouse", RAWMOUSE),
        ("keyboard", RAWKEYBOARD),
        ("hid", RAWHID)
    )


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawinput
class RAWINPUT(Structure):
    _fields_ = (
        ("header", RAWINPUTHEADER),
        ("data", RAWINPUT_DATA)
    )
