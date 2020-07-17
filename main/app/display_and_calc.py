import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from container.display.app.display import Display
from container.calc.app.calc import Calc


class DisplayAndCalc():
    def __init__(self):
        self._display = Display()
        self._calc = Calc()

    def ShowCalc(self):
        data = self._calc.calc()
        self._display.show(data)
        return data


if __name__ == "__main__":
    run = DisplayAndCalc()
    run.ShowCalc()
