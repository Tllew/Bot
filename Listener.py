import pyHook
import pythoncom
import time

class Listener(object):

    def beforeafter(self):
        after = time.time() - self.before
        self.before = time.time()
        return after

    def onClick(self,event):
        return self.genericAction(event)

    def onKeyboardEvent(self,event):
        return self.genericAction(event)

    def genericAction(self,event):
        button = None
        if hasattr(event, "Ascii"):
            button = event.Ascii
            if button == 27:
                self.go = False
                return False
        elif hasattr(event, "Position"):
            value = "left"
            if "right" in event.MessageName:
                value = "right"
            button = (value, event.Position)
        after = self.beforeafter()
        self.actionList.append({button:after})
        return True

    def listen(self):
        self.go = True
        self.actionList = []
        hm = pyHook.HookManager()
        hm.SubscribeMouseAllButtonsDown(self.onClick)
        hm.KeyDown = self.onKeyboardEvent
        hm.HookMouse()
        hm.HookKeyboard()
        self.before = time.time()
        while self.go:
            pythoncom.PumpWaitingMessages()
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        return self.actionList
        # "This is the end my friend"

    def main(self):
        print self.listen()

if __name__ == "__main__":
    Listener.main(Listener())