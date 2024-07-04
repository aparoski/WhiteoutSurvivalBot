import win32gui as w
import pyautogui as p
import time
from fractions import Fraction
import relative_locations as rl
"""A temporary file that will be used to gather position information
for the different icons of the app"""


def Window_lw(x1, y1, x2, y2):
    """finds the length and width of a rectangular
    box between two coordinates if the coordinates are
    located at the top left and bottom right corners of the rectangle"""

    l = y2 - y1
    w = x2 - x1

    return(w, l)

def enumHandler(hwnd, list):
    if "BlueStacks App Player 1" in w.GetWindowText(hwnd):

        
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
    elif "BlueStacks App Player 3" in w.GetWindowText(hwnd):

        
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
    elif "BlueStacks App Player 4" in w.GetWindowText(hwnd):

        
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
    elif "BlueStacks App Player" in w.GetWindowText(hwnd):

        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])

window_list = []

w.EnumWindows(enumHandler, window_list)

for i in window_list:
    print(i[2])
    print()
    print(i[1])
    print()
    print()


x1, y1, x2, y2 = window_list[0][1]

W, L = Window_lw(x1, y1, x2, y2)

time.sleep(2)

pos_x, pos_y = p.position()

x_distance = pos_x - x1
y_distance = pos_y - y1

rel_x = x_distance / W
rel_y = y_distance / L

print(rel_x, rel_y)


p.moveTo(x1 + W*rl.PetPerk_Elk_x,  
         y1 + L*rl.PetPerk_Elk_y)