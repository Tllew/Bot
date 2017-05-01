import Press, Listener, random

class RecordAndPlay(object):

    def main(self):
        events = Listener.Listener().listen()
        Press.Press().runEvents(events)

if __name__ == "__main__":
    RecordAndPlay.main(RecordAndPlay())