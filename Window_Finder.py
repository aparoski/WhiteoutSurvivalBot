import win32gui as w
import Helper_Funcs as HF

#testing
import Image_Rec
import relative_locations as rel
import time
import pyautogui as p
import pandas as pd
from datetime import datetime as dt

def Bluestack_window_return():

    def enumHandler(hwnd, list):
        if ("BlueStacks App Player" in w.GetWindowText(hwnd)):

            print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd))
            list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])


    window_list = []
    w.EnumWindows(enumHandler, window_list)

    return(window_list)


current_windows = Bluestack_window_return()


class BlueStack_Window:

    def __init__(self, order):

        self.order = order
         
        def single_window_return(order):

            def enumHandler(hwnd, list):
                if ("BlueStacks App Player 1" == w.GetWindowText(hwnd) and
                order == "BlueStacks App Player 1"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
                elif ("BlueStacks App Player 3" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 3"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
                elif ("BlueStacks App Player 4" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 4"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
                elif ("BlueStacks App Player" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])

            window_list = []
            w.EnumWindows(enumHandler, window_list)

            for i in window_list:
                print(i[1])

            return(window_list[0][0])
        
        window_hwnd = single_window_return(order)
        
        temp_rect = w.GetWindowRect(window_hwnd)

        #commented out for testing. remove after confirm
        # def Window_lw(x1, y1, x2, y2):
        #     """finds the length and width of a rectangular
        #     box between two coordinates if the coordinates are
        #     located at the top left and bottom right corners of the rectangle"""

        #     l = y2 - y1
        #     w = x2 - x1

        #     return(w, l)
        
        x1, y1, x2, y2 = temp_rect

        temp_W_L = HF.Window_lw(x1, y1, x2, y2)

        w.MoveWindow(window_hwnd, x1, y1, 550, 951, True)

        self.rectangle = w.GetWindowRect(window_hwnd)

        x1, y1, x2, y2 = self.rectangle

        self.W_L = HF.Window_lw(x1, y1, x2, y2)

        self.hwnd = window_hwnd

    #error when "bring me back to city" button overlaied on the lighthouse icon
    def Open_Lighthouse(self) -> None:
        Image_Rec.Lighthouse_confirm_and_Open(self.rectangle[0],
                                              self.rectangle[1],
                                              self.W_L[0],
                                              self.W_L[1])
    
    
    def Lighthouse_Operation(self):

        march_time = Image_Rec.light_house_icon_Navigator(self.rectangle[0],
                                                    self.rectangle[1],
                                                    self.W_L[0],
                                                    self.W_L[1])
        return(march_time)
    
    def window_to_foreground(self):
        w.SetForegroundWindow(self.hwnd)
        
    #temp set up for testing
    def swipe(self, dir = "up"):
        
        HF.swipe(self.rectangle[0],
                 self.rectangle[1],
                 self.W_L[0],
                 self.W_L[1],
                 dir)
        
    def vid(self):

        HF.stop_video_recording(self.rectangle[0],
                                self.rectangle[1],
                                self.W_L[0],
                                self.W_L[1])

if __name__ == '__main__':

    test = BlueStack_Window(order="BlueStacks App Player")

    test.swipe()
   

    

    




