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


current_windows = Bluestack_window_return()


#check to see if the dataframe exists. if not, create it and save. 

if False:
    pass
else: 
    col_len = np.arange(len(current_windows))

    Window_Stats = pd.DataFrame({"Window_Name" : [i[1] for i in current_windows],
                                 "window_hwnd" : [i[0] for i in current_windows],
                                 "Activity" : col_len,
                                 "completion_date" : col_len})

    Window_Stats["completion_date"] = Window_Stats["completion_date"].astype('datetime64[ns]')
    Window_Stats["Activity"] = Window_Stats["Activity"].astype('category')
    
print(Window_Stats)