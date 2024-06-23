

#on startup
#find game screen
#load images


#Continuous

#master scheduler

#take screen shot image of game screen
#check screen for images


import win32gui

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[0]
    w = rect[0] - x
    h = rect[0] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))

def main():
    win32gui.EnumWindows(callback, None)