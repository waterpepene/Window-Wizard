import PySimpleGUI as sg
from b64 import *
from ctypes import windll
from functions import getHWNDandTITLES

WS_EX_APPWINDOW, GWL_EXSTYLE, WS_EX_TOOLWINDOW = 0x00040000, - 20, 0x00000080  # variables used to create icon
sg.theme("DarkBlue16"), sg.theme_background_color("#023E8A"), sg.theme_text_color("#CAF0F8"), sg.theme_border_width(0)
sg.theme_text_element_background_color(sg.theme_background_color())     # Changing a few theme colors


def create_icon(win_name):
    # This function will create an icon for the border-less window
    hwnd = windll.user32.GetParent(win_name.TKroot.winfo_id())
    style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)

    win_name.TKroot.wm_withdraw()
    win_name.TKroot.wm_deiconify()


def window_move(event):                 # This function will enable the title bar area to be grabbed
    xwin, ywin = wind.TKroot.winfo_x(), wind.TKroot.winfo_y()
    startx, starty = event.x_root, event.y_root
    ywin, xwin = ywin - starty, xwin - startx

    def move_window(event):
        wind.TKroot.geometry("1000x700" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))

    startx, starty= event.x_root, event.y_root

    wind["-TITLEBAR-"].TKText.bind('<B1-Motion>', move_window)


# The layout for the custom title bar
titlebar = [[sg.Text(" "*222, background_color="#03045E", key="-TITLEBAR-",),  # Blank text to fill in the frame
            sg.Button("", image_data=minimizeicon, tooltip="Minimize the program", border_width=0,
                      button_color=("#03045E", "#03045E"), key="-MINIMIZE-"),
            sg.Button("", image_data=quiticon, tooltip="Exit the program", border_width=0,
                      button_color=("#03045E", "#03045E"), key="-QUIT-", pad=(10, 0))]]

win_titlebar = [[sg.Text("Title bar", font=("dubai", 16), justification="c")],

                [sg.Combo(["Add", "Remove", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                          text_color=sg.theme_text_color(), key="-WINTITLEBAR-")]]

disable_btns = [[sg.Text("Disable TB", font=("dubai", 16), justification="c")],

                [sg.Combo(["Exit", "Minimize", "Maximize", "All", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                          text_color=sg.theme_text_color(), key="-DISABLEBTNS-", tooltip="This field disables chosen "
                                                                                         "buttons from the title bar of "
                                                                                         "the selected window")]]

enable_btns = [[sg.Text("Enable TB", font=("dubai", 16), justification="c")],

               [sg.Combo(["Exit", "Minimize", "Maximize", "All", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                          text_color=sg.theme_text_color(), key="-ENABLEBTNS-", tooltip="This field enables chosen "
                                                                                        "buttons from the title bar of "
                                                                                        "the selected window")]]

transparency = [[sg.Text("Transparency", font=("dubai", 16), justification="c")],

                [sg.InputText("0-255", font=("dubai", 14), size=(12, 1), justification="c", text_color=sg.theme_text_color(),
                              key="-TRANSPARENCY-", enable_events=True, tooltip="Enter the amount of transparency\n"
                                                                                "you want the window to have. \n"
                                                                                "Lower is better")]]

topmost = [[sg.Text("Topmost", font=("dubai", 16), justification="c")],

           [sg.Combo(["True", "Normal", "Bottom", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                     text_color=sg.theme_text_color(), key="-TOPMOST-")],
           [sg.Col(win_titlebar, element_justification="c")]]

state = [[sg.Text("State", font=("dubai", 16), justification="c")],

         [sg.Combo(["Hide", "Minimize", "Maximize", "Unhide", "Restore", "None"], default_value="Choose a value",
                   font=("dubai", 14), size=(12, 1), text_color=sg.theme_text_color(), key="-STATE-")],
         [sg.Col(disable_btns, element_justification="c")]]

enabled = [[sg.Text("Enabled or not", font=("dubai", 16), justification="c")],

           [sg.Combo(["Enabled", "Disabled", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                     text_color=sg.theme_text_color(), key="-ENABLED-")],
           [sg.Col(enable_btns, element_justification="c")]]

resize_lock = [[sg.Text("Resize Lock", font=("dubai", 16), justification="c")],

               [sg.Combo(["Locked", "Unlocked", "None"], default_value="Choose a value", font=("dubai", 14), size=(12, 1),
                         text_color=sg.theme_text_color(), key="-LOCKED-")],
               [sg.Col(transparency, element_justification="c")]]

resize = [[sg.Text("Resize window", font=("dubai", 16), justification="c")],

          [sg.InputText("x y", font=("dubai", 14), size=(12, 1), justification="c", text_color=sg.theme_text_color(),
                        key="-RESIZE-", enable_events=True)]]

move = [[sg.Text("Move window", font=("dubai", 16), justification="c")],

        [sg.InputText("x y", font=("dubai", 14), size=(12, 1), justification="c", text_color=sg.theme_text_color(),
                      key="-MOVE-", enable_events=True)]]


# The layout of the main window
layout = [[sg.Frame("", layout=titlebar, element_justification="c", background_color="#03045E",
                    border_width=0, pad=(0, 0))],

          [sg.Text("Window Wizard", font=("dubai", 32))],

          [sg.Text("Select a window below to get started!", font=("dubai", 20)),
           sg.Button("", image_data=refresh, border_width=0, tooltip="Refresh the list of windows below.",
                     button_color=(sg.theme_background_color(), sg.theme_background_color()), key="-REFRESH-")],

          [sg.Listbox(["Here should be a list of window names"], size=(25, 4), font=("dubai", 18), key="-LISTBOX-",
                      background_color=sg.theme_input_background_color(), text_color=sg.theme_text_color(),
                      enable_events=True, tooltip="Here are the windows that are enabled or visible")],

          [sg.InputText("Select a window", font=("dubai", 18), readonly=True, size=(25, 1), key="-SELECTED-",
                        text_color=sg.theme_text_color(), justification="c", tooltip="Here's the name of the chosen window",
                        disabled_readonly_background_color=sg.theme_input_background_color())],

          [sg.Col(topmost, element_justification="c"), sg.Col(state, element_justification="c"),
           sg.Col(enabled, element_justification="c"), sg.Col(resize_lock, element_justification="c"),
           sg.Col(resize, element_justification="c"), sg.Col(move, element_justification="c")
           ],

          [sg.Button("Close window", font=("dubai", 13), size=(12, 1), key="-CLOSE-", tooltip="Closes the selected window."),
           sg.Button("Reset Values", font=("dubai", 13), size=(12, 1), key="-RESET-", pad=(10, 15),
                     tooltip="Reset the values selected, but it doesn't reset the\nchanges caused to windows,"
                             "to reset a window, restart it."),
           sg.Button("Apply values", font=("dubai", 13), size=(12, 1), key="-APPLY-", tooltip="Applies the selected changes.")]]

# Creating the window
wind = sg.Window("Window Wizard", layout, size=(1000, 700), element_justification="c", no_titlebar=True)


wind.read(timeout=1)       # This invokes a load event that will create an icon for the program
create_icon(wind)
wind["-TITLEBAR-"].TKText.bind('<Button-1>', window_move)  # binding the function to the title bar and mouse1
_, names_only = getHWNDandTITLES()
wind["-LISTBOX-"].update(values=names_only)                # updates the listbox with the windows running
