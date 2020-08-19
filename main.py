from gui import *
from functions import *
from time import sleep
from PySimpleGUI import PopupError

while True:
    event, value = wind.read()
    names_and_hwnd, names_only = getHWNDandTITLES()

    if event in "-REFRESH-":
        wind["-LISTBOX-"].update(values=names_only)

    if event == "-QUIT-":
        quit()

    if event == "-LISTBOX-":
        wind["-SELECTED-"].update(value["-LISTBOX-"][0])

    if event == "-MINIMIZE-":
        wind.TKroot.wm_overrideredirect(False)
        wind.Minimize()                             # Looking for better ways to minimize it but this works for now
        sleep(1)
        wind.TKroot.wm_overrideredirect(True)
        create_icon(wind)

    if event == "-CLOSE-":
        if value["-SELECTED-"] in names_and_hwnd:
            closeWindow(names_and_hwnd[value["-SELECTED-"]])

    if event == "-RESET-":
        resetAllValues(wind)

    if event == "-APPLY-":
        if value["-SELECTED-"] in names_and_hwnd:
            hwnd = names_and_hwnd[value["-SELECTED-"]]

            changeTopMost(value["-TOPMOST-"], hwnd)
            changeState(value["-STATE-"], hwnd)
            EnableOrDisable(value["-ENABLED-"], hwnd)
            Locking(value["-LOCKED-"], hwnd)
            addOrRemoveTitleBar(value["-WINTITLEBAR-"], hwnd)
            enableTitleBarButtons(value["-ENABLEBTNS-"], hwnd)
            disableTitleBarButtons(value["-DISABLEBTNS-"], hwnd)
            try:
                windowTransparency(int(value["-TRANSPARENCY-"]), hwnd)
            except ValueError:
                if value["-TRANSPARENCY-"] == "0-255":
                    pass
                else:
                    PopupError("You can't enter text in the \'Transparency\' text field.", font=("dubai", 16),
                               auto_close=True, auto_close_duration=5, no_titlebar=True, background_color="#0096C7")
                    wind["-TRANSPARENCY-"].update("0-255")

            except OverflowError:
                PopupError("A number between 0 and 255 has to be inputted in the \'Transparency\' text field.", font=("dubai", 16),
                           auto_close=True, auto_close_duration=5, no_titlebar=True, background_color="#0096C7")
                wind["-TRANSPARENCY-"].update("0-255")

            try:
                moveWindow(hwnd, int(value["-MOVE-"].split()[0]), int(value["-MOVE-"].split()[1]))
            except ValueError:
                if value["-MOVE-"] == "x y":
                    pass
                else:
                    PopupError("You can't enter text in the \'Move window\' text field.", font=("dubai", 16),
                               auto_close=True, auto_close_duration=5, no_titlebar=True, background_color="#0096C7")
                    wind["-MOVE-"].update("x y")

            try:
                resizeWindow(hwnd, int(value["-RESIZE-"].split()[0]), int(value["-RESIZE-"].split()[1]))
            except ValueError:
                if value["-RESIZE-"] == "x y":
                    pass
                else:
                    PopupError("You can't enter text in the \'Resize window\' text field.", font=("dubai", 16),
                               auto_close=True, auto_close_duration=5, no_titlebar=True, background_color="#0096C7")
                    wind["-RESIZE-"].update("x y")

        else:
            print("problem")