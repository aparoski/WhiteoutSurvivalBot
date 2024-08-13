import pandas as pd
import numpy as np

import win32gui as w

def Bluestack_window_return():

    def enumHandler(hwnd, list):
        if ("BlueStacks App Player" in w.GetWindowText(hwnd)):

            print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd))
            list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])


    window_list = []
    w.EnumWindows(enumHandler, window_list)

    return(window_list)

for i in Bluestack_window_return():

    print(i[1])