import win32gui as w




def Window_lw(x1, y1, x2, y2):
    """finds the length and width of a rectangular
    box between two coordinates if the coordinates are
    located at the top left and bottom right corners of the rectangle"""

    l = y2 - y1
    w = x2 - x1

    return(w, l)

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


#work within each Blue stack window / setup for testing right now
for i in window_list:
    print(i[2])
    print()
    print(i[1])
    print()
    print()


x1, y1, x2, y2 = window_list[0][1]

W, L = Window_lw(x1, y1, x2, y2)

p.moveTo(x1, y1)