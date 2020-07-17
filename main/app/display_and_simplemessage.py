import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from container.display.app.display import Display
from container.simplemessage.app.simplemessage import SimpleMessage


class DisplayAndSimpleMessage():
    def __init__(self):
        self._display = Display()
        self._simplemessage = SimpleMessage()

    def ShowSimpleMessage(self):
        data = self._simplemessage.simplemessage()
        self._display.show(data)
        return data


if __name__ == "__main__":
    run = DisplayAndSimpleMessage()
    run.ShowSimpleMessage()
