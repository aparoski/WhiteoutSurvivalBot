import pandas as pd
import numpy as np

from datetime import datetime, timedelta

#move this into Window_Finder when ready
from Window_Finder import Bluestack_window_return
import os


class Window_Dataframe: 

    def __init__(self, path):
        """check to see if the dataframe exists. if not, create it and save.
            if yes, load it """
        
        self.path = path
        
        current_windows = Bluestack_window_return()

        if os.path.isfil:
            pass
        else: 
            col_len = np.arange(len(current_windows))

            Window_Stats = pd.DataFrame({"Window_Name" : [i[1] for i in current_windows],
                                        "window_hwnd" : [i[0] for i in current_windows],
                                        "Activity" : col_len,
                                        "completion_date" : col_len})

            Window_Stats["completion_date"] = Window_Stats["completion_date"].astype('datetime64[ns]')
            Window_Stats["Activity"] = Window_Stats["Activity"].astype('category')
            
        self.df = Window_Stats

    def close_df(self):
        self.df.to_csv(self.path)

    def add_activity(self, window_name, hwnd, activity_name, time):
        """take the amount of time to run an activity
        and marks a time in the future for it's completion.
        times marked are in UTC"""

        future_time = datetime.utcnow() + timedelta(0, time)

        new_record = pd.DataFrame({"Window_Name" : window_name, 
                                "window_hwnd" : hwnd, 
                                "Activity" : activity_name, 
                                "completion_date" : future_time}, index = [0])

        return(pd.concat([self.df, new_record], axis = 0))