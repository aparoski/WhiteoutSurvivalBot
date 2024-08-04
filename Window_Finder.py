import win32gui as w
import Helper_Funcs as HF

#testing
import Image_Rec
import relative_locations as rel
import time
import pyautogui as p
import pandas as pd
from datetime import datetime as dt


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

        def Window_lw(x1, y1, x2, y2):
            """finds the length and width of a rectangular
            box between two coordinates if the coordinates are
            located at the top left and bottom right corners of the rectangle"""

            l = y2 - y1
            w = x2 - x1

            return(w, l)
        
        x1, y1, x2, y2 = temp_rect

        temp_W_L = Window_lw(x1, y1, x2, y2)

        w.MoveWindow(window_hwnd, x1, y1, 550, 951, True)

        self.rectangle = w.GetWindowRect(window_hwnd)

        x1, y1, x2, y2 = self.rectangle

        self.W_L = Window_lw(x1, y1, x2, y2)

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

if __name__ == '__main__':

    test = BlueStack_Window(order="BlueStacks App Player 3")

    path = r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot\images\images_Lighthouse\tent_gold.JPG"
    
    #testing
    def check_for_tent(x1, y1, W, L):
            """assumption here is that no other marches have completed
            so there should only be one check on the screen at a time"""
            
            Image_Rec.Lighthouse_confirm_and_Open(x1, y1, W, L)
            
            dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_lighthouse_misc\\"
            check = "lighthouse_event_completion.JPG"
            tent_checked = HF.check_image(x1, y1, W, L, dir + check,
                                        10, confidence = 0.9,
                                        message = "tent journey completion")
            
            Image_Rec.Universal_Backout(x1, y1, W, L)

    x1, y1, x2, y2 = test.rectangle
    
    W, L = test.W_L

    test.window_to_foreground()

    check_for_tent(x1, y1, W, L)
   

    

    




