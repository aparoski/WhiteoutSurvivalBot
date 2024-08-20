import pandas as pd
import numpy as np

from datetime import datetime, timedelta, date

#move this into Window_Finder when ready
#from Window_Finder import Bluestack_window_return
import os
#temp stopgap
import win32gui as w


class Window_Dataframe: 

    def __init__(self):
        """check to see if the dataframe exists. if not, create it and save.
            if yes, load it. when the dataframe is loaded any times in 
            the past will be removed"""
        
        self.path = os.path.dirname(__file__) + "\\Whiteout_Schedule.csv"

        if os.path.isfile(self.path):
            #load dataframe
            Window_Stats = pd.read_csv(self.path)
            #remove times from the past
            Window_Stats = Window_Stats[Window_Stats["completion_date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) >= datetime.utcnow()]
        else: 

            def current_windows():

                def enumHandler(hwnd, list):
                    if ("BlueStacks App Player" in w.GetWindowText(hwnd)):

                        
                        list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])

                window_list = []
                w.EnumWindows(enumHandler, window_list)

                return(window_list)
            
            windows = current_windows()

            col_len = np.arange(len(windows))

            Window_Stats = pd.DataFrame({"Window_Name" : [i[1] for i in windows],
                                        "window_hwnd" : [i[0] for i in windows],
                                        "Activity" : col_len,
                                        "completion_date" : col_len})
            #force future time for the first few entries so they are never removed

            Window_Stats["completion_date"] = datetime(9999, 1, 1, 1, 1, 1)

        Window_Stats["completion_date"] = Window_Stats["completion_date"].values.astype('datetime64[s]')
        Window_Stats["Activity"] = Window_Stats["Activity"].astype('category')
        
        self.df = Window_Stats

    def save(self):
        self.df.to_csv(self.path, index = False)

    def add(self, window_name, hwnd, activity_name, time):
        """take the amount of time to run an activity
        and marks a time in the future for it's completion.
        times marked are in UTC"""

        future_time = datetime.utcnow() + timedelta(0, time)

        new_record = pd.DataFrame({"Window_Name" : window_name, 
                                "window_hwnd" : hwnd, 
                                "Activity" : activity_name, 
                                "completion_date" : future_time}, index = [0])
        
        new_record["completion_date"] = new_record["completion_date"].values.astype('datetime64[s]')

        self.df = pd.concat([self.df, new_record], axis = 0)
    

if __name__ == '__main__':

    print(os.path.dirname(__file__))

    schedule = Window_Dataframe()

    #schedule.add("test", 1234, "apples", 5)

    latest_event = schedule.df[schedule.df["completion_date"].apply(lambda x: x.year < 3999)].sort_values("completion_date", ascending = False).head(1)

    print(latest_event.shape)