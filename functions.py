import ctypes
from win32gui import *
import win32con as con
from win32api import RGB

enumWindows = ctypes.windll.user32.EnumWindows
enumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
getWindowText = ctypes.windll.user32.GetWindowTextW
getWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
isWindowVisible = ctypes.windll.user32.IsWindowVisible


def getHWNDandTITLES():                         # This function returns a dictionary containing window titles
    names_and_hwnd, names_only = {}, []         # And their respective hwnd, and a list only containing names

    def foreach_window(hwnd, lParam):
        if isWindowVisible(hwnd) or IsWindowEnabled(hwnd):
            length = getWindowTextLength(hwnd)
            title_name = ctypes.create_unicode_buffer(length + 1)
            getWindowText(hwnd, title_name, length + 1)

            if title_name.value == "":
                pass
            else:
                names_and_hwnd[title_name.value] = hwnd
                names_only.append(title_name.value)

        return True
    enumWindows(enumWindowsProc(foreach_window), 0)

    return names_and_hwnd, names_only


def changeTopMost(option_selected, hwnd):
    x, y, z, a = GetWindowPlacement(hwnd)[4]

    if option_selected == "True":
        ShowWindow(hwnd, True)
        SetWindowPos(hwnd, con.HWND_TOPMOST, x, y, z, a, 0)

    elif option_selected == "Normal":
        ShowWindow(hwnd, True)
        SetWindowPos(hwnd, con.HWND_NOTOPMOST, x, y, z, a, 0)

    elif option_selected == "Bottom":
        ShowWindow(hwnd, True)
        SetWindowPos(hwnd, con.HWND_BOTTOM, x, y, z, a, 0)


def changeState(option_selected, hwnd):
    if option_selected == "Minimize":
        ShowWindow(hwnd, con.SW_FORCEMINIMIZE)

    elif option_selected == "Hide":
        ShowWindow(hwnd, con.SW_HIDE)

    elif option_selected == "Maximize":
        ShowWindow(hwnd, con.SW_MAXIMIZE)

    elif option_selected == "Unhide":
        ShowWindow(hwnd, con.SW_SHOW)

    elif option_selected == "Restore":
        ShowWindow(hwnd, con.SW_RESTORE)


def EnableOrDisable(option_selected, hwnd):
    if option_selected == "Enabled":
        EnableWindow(hwnd, True)

    elif option_selected == "Disabled":
        EnableWindow(hwnd, False)


def closeWindow(hwnd):
    PostMessage(hwnd, con.WM_CLOSE, 0, 0)


def Locking(option_selected, hwnd):
    if option_selected == "Locked":
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) & ~ con.WS_SIZEBOX & ~ con.WS_MAXIMIZEBOX)

    if option_selected == "Unlocked":
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) | con.WS_SIZEBOX | con.WS_MAXIMIZEBOX)


def moveWindow(hwnd, x, y):
    SetWindowPos(hwnd, 0, x, y, 0, 0, con.SWP_NOZORDER | con.SWP_NOSIZE | con.SWP_NOACTIVATE)


def resizeWindow(hwnd, width, height):
    z, a, *_ = GetWindowPlacement(hwnd)[4]
    SetWindowPos(hwnd, 0, z, a, width, height, 0)


def resetAllValues(window_name):
    window_name["-SELECTED-"].update("Select a window")
    window_name["-TOPMOST-"].update("Choose a value")
    window_name["-STATE-"].update("Choose a value")
    window_name["-ENABLED-"].update("Choose a value")
    window_name["-LOCKED-"].update("Choose a value")
    window_name["-RESIZE-"].update("x y")
    window_name["-MOVE-"].update("x y")
    window_name["-TRANSPARENCY-"].update("0-255")
    window_name["-DISABLEBTNS-"].update("Choose a value")
    window_name["-ENABLEBTNS-"].update("Choose a value")
    window_name["-WINTITLEBAR-"].update("Choose a value")


def addOrRemoveTitleBar(option_selected, hwnd):
    if option_selected == "Add":
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE)
                      | (con.WS_BORDER | con.WS_DLGFRAME | con.WS_THICKFRAME))

    elif option_selected == "Remove":
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE)
                      & ~ (con.WS_BORDER | con.WS_DLGFRAME | con.WS_THICKFRAME))


def enableTitleBarButtons(option_selected, hwnd):
    all_option = True if option_selected == "All" else False

    if option_selected == "Minimize" or all_option:
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) | con.WS_MINIMIZEBOX)

    if option_selected == "Maximize" or all_option:
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) | con.WS_MAXIMIZEBOX)

    if option_selected == "Exit" or all_option:
        EnableMenuItem(GetSystemMenu(hwnd, False), con.SC_CLOSE, con.MF_BYCOMMAND | con.MF_ENABLED)


def disableTitleBarButtons(option_selected, hwnd):
    all_option = True if option_selected == "All" else False

    if option_selected == "Minimize" or all_option:
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) & ~ con.WS_MINIMIZEBOX)

    if option_selected == "Maximize" or all_option:
        SetWindowLong(hwnd, con.GWL_STYLE, GetWindowLong(hwnd, con.GWL_STYLE) & ~ con.WS_MAXIMIZEBOX)

    if option_selected == "Exit" or all_option:
        EnableMenuItem(GetSystemMenu(hwnd, False), con.SC_CLOSE, con.MF_BYCOMMAND | con.MF_DISABLED | con.MF_GRAYED)


def windowTransparency(value, hwnd):
    SetWindowLong(hwnd, con.GWL_EXSTYLE, GetWindowLong(hwnd, con.GWL_EXSTYLE) | con.WS_EX_LAYERED)
    SetLayeredWindowAttributes(hwnd, RGB(0, 0, 0), value, con.LWA_ALPHA)
