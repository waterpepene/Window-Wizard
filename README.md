# Window Wizard
## This program is able to manipulate the GUI of other programs running on Windows only.
 
Built using the win32 api and PySimpleGUI.

![Window-Wizard Picture](https://i.imgur.com/g1eq6h3.png)

Before starting, keep in mind that it may not be able to modify every window to your liking, it may not even work on some windows.

To start, clone the repo, run main.py and click whichever window you want to manipulate.

NOTE: The windows in the listbox are either visible or enabled(meaning that they can take input).

### The options:

- ***Topmost:*** This property decides whether the window selected is:
  - **True:** In front of all programs, meaning that the window will always be visible on the screen, with the exception of a fullscreen application.
  - **Normal:** The normal state of the window.
  - **Bottom:** This will make the window visible only on desktop.

- ***State:*** This property defines the visibility state of the window.
  - **Minimize:** Minimizes the selected window.
  - **Maximize:** Maximizes the selected window.
  - **Hide:** Hides the window. The icon will be removed from the taskbar and it can only be restored using the Unhide setting or double-clicking the SystemTray icon, if available.
  - **Unhide:** It will Unhide a hidden window.
  - **Restore:** It will restore a minimized window to the position and size it was before it was minimized
  
- ***Enabled or not:*** Decides whether the window takes input from the user or not.
  -**Enabled:** The window CAN take user input.
  - **Disabled:** The window CAN NOT take user input.
  
- ***Resize Lock:*** Locks or unlocks the ability to resize the window.
  - **Locked:** The selected window CAN NOT be resized anymore.
  - **Unlocked:** The selected window CAN be resized.
  
- ***Resize Window:*** Resizes the selected window to the x y parameters.

- ***Move Window:*** Moves the selected window to the x y paramaters.

- ***Titlebar:*** Adds or removes the title bar of a window. NOTE: It may not work with all windows.
  - **Add:** Adds the title bar
  - **Remove:** Removes the title bar

- ***Disable TB*** Disables the three title bar buttons (Minimize, Maximize and Exit.)
  - **Exit** Disables the exit button.
  - **Minimize** Disables the minimize button.
  - **Maximize** Disables the maximize button.
  - **All** Disables all the title bar buttons.
  
- ***Enable TB*** Enables the three title bar buttons (Minimize, Maximize and Exit.)
  - **Exit** Enables the exit button.
  - **Minimize** Enables the minimize button.
  - **Maximize** Enables the maximize button.
  - **All** Enables all the title bar buttons.
  
- ***Transparency:*** Changes the opacity level of a window. The number can be in-between 0 and 255.
