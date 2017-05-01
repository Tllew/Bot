import win32api, win32con, time, random

class Press(object):
    def moveAndClick(self,button,x,y,seconds):
        win32api.SetCursorPos((x,y))
        down = win32con.MOUSEEVENTF_LEFTDOWN
        up = win32con.MOUSEEVENTF_LEFTUP
        if button == "right":
            down = win32con.MOUSEEVENTF_RIGHTDOWN
            up = win32con.MOUSEEVENTF_RIGHTUP

        win32api.mouse_event(down, x, y, 0, 0)
        time.sleep(seconds)
        win32api.mouse_event(up, x, y, 0, 0)

    def mouse(self,event,seconds):
        button = event[0]
        xy = event[1]
        x = int(random.gauss(xy[0],3))
        y = int(random.gauss(xy[1],3))

        self.moveAndClick(button,x,y,seconds)

    def key(self,button,seconds):
        win32api.keybd_event(button,0,0,0)
        time.sleep(seconds)
        win32api.keybd_event(button,0,win32con.KEYEVENTF_KEYUP,0)

    def keyOrMouse(self,event):
        event = tuple(item for sublist in event.items() for item in sublist)
        action = event[0]
        seconds = random.gauss(event[1],event[1]/10)
        if isinstance(event[0],tuple):
            self.mouse(action, seconds)
        else:
            self.key(action, seconds)

    def runEvents(self,events):
        for event in events:
            self.keyOrMouse(event)

    def main(self):
        events = [{('left', (500, 500)): 1.6800000667572021}, {27: 2.427000045776367}] #left click somewhere and then click escape
        self.runEvents(events)

if __name__ == "__main__":
    Press.main(Press())

