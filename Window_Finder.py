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
                if ("BlueStacks App Player 1" in w.GetWindowText(hwnd) and
                order == "BlueStacks App Player 1"):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "second")
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
                elif ("BlueStacks App Player 3" in w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 3"):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "third")
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
                elif ("BlueStacks App Player 4" in w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 4"):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "fourth")
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
                elif ("BlueStacks App Player" in w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player"):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "main")
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


    def window_to_foreground(self):
        w.SetForegroundWindow(self.hwnd)

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
    
    #events functions need to be wrapped into something neater
    #current form is for testing
    def open_events(self):
        Image_Rec.gotoevents(self.rectangle[0],
                             self.rectangle[1],
                             self.W_L[0],
                             self.W_L[1])
        
    def lucky_wheel_chip_grab(self):
        Image_Rec.Lucky_Wheel_Chip_Grab(self.rectangle[0],
                                        self.rectangle[1],
                                        self.W_L[0],
                                        self.W_L[1])

    def backout(self):
        Image_Rec.Universal_Backout(self.rectangle[0],
                                    self.rectangle[1],
                                    self.W_L[0],
                                    self.W_L[1])

        
    #temp set up for testing
    def swipe(self, dir = "up", magnitude = 1, 
              starting_x = 0.5, starting_y = 0.5):
        
        HF.swipe(self.rectangle[0],
                 self.rectangle[1],
                 self.W_L[0],
                 self.W_L[1],
                 dir,
                 magnitude,
                 starting_x, starting_y)
        
    def vid(self):

        HF.stop_video_recording(self.rectangle[0],
                                self.rectangle[1],
                                self.W_L[0],
                                self.W_L[1])

if __name__ == '__main__':

    test = BlueStack_Window(order="BlueStacks App Player")


    test.window_to_foreground()

    x1, y1, x2, y2 = test.rectangle

    W, L, = test.W_L

    error_int = 0
    
    while error_int < 20:

        error_int += 1

        wait_time = Image_Rec.Online_Reward_Finder(x1, y1, W, L)
        

        time.sleep(wait_time)




