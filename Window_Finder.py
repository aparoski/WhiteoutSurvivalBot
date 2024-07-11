import win32gui as w

import Image_Rec 


class BlueStack_Window:

    def __init__(self, order):

        self.order = order
         
        def single_window_return(order):

            def enumHandler(hwnd, list):
                if "BlueStacks App Player 1" in w.GetWindowText(hwnd):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "second")
                    list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
                elif "BlueStacks App Player 3" in w.GetWindowText(hwnd):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "third")
                    list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
                elif "BlueStacks App Player 4" in w.GetWindowText(hwnd):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "fourth")
                    list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
                elif "BlueStacks App Player" in w.GetWindowText(hwnd):

                    print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "main")
                    list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])

            window_list = []
            w.EnumWindows(enumHandler, window_list)

            return(window_list[order][1])
        
        self.rectangle = single_window_return(order)

        def Window_lw(x1, y1, x2, y2):
            """finds the length and width of a rectangular
            box between two coordinates if the coordinates are
            located at the top left and bottom right corners of the rectangle"""

            l = y2 - y1
            w = x2 - x1

            return(w, l)
        
        x1, y1, x2, y2 = self.rectangle

        self.W_L = Window_lw(x1, y1, x2, y2)

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
        

    def swipe(self, dir = "up"):
        
        Image_Rec.swipe(self.rectangle[0],
                        self.rectangle[1],
                        self.W_L[0],
                        self.W_L[1],
                        dir)

if __name__ == '__main__':
    
    test = BlueStack_Window(order=0)
    for _ in range(15):
        test.swipe("up")

    for _ in range(5):
        test.swipe("down")

    for _ in range(7):
        test.swipe("left")

    

    




