import typing
import os
import datetime
import itertools

class logging:

    def __init__(self):
        self.theme = "\033[38;5;253m"

        self.list = ['\x1b[38;2;255;20;0m', '\x1b[38;2;255;40;0m', '\x1b[38;2;255;60;0m', '\x1b[38;2;255;80;0m',
                     '\x1b[38;2;255;100;0m', '\x1b[38;2;255;120;0m', '\x1b[38;2;255;140;0m', '\x1b[38;2;255;160;0m',
                     '\x1b[38;2;255;180;0m', '\x1b[38;2;255;200;0m', '\x1b[38;2;255;220;0m', '\x1b[38;2;255;240;0m',
                     '\x1b[38;2;220;255;0m', '\x1b[38;2;200;255;0m', '\x1b[38;2;180;255;0m', '\x1b[38;2;160;255;0m',
                     '\x1b[38;2;140;255;0m', '\x1b[38;2;120;255;0m', '\x1b[38;2;100;255;0m', '\x1b[38;2;80;255;0m',
                     '\x1b[38;2;60;255;0m', '\x1b[38;2;40;255;0m', '\x1b[38;2;20;255;0m', '\x1b[38;2;0;255;0m',
                     '\x1b[38;2;0;255;20m', '\x1b[38;2;0;255;40m', '\x1b[38;2;0;255;60m', '\x1b[38;2;0;255;80m',
                     '\x1b[38;2;0;255;100m', '\x1b[38;2;0;255;120m', '\x1b[38;2;0;255;140m', '\x1b[38;2;0;255;160m',
                     '\x1b[38;2;0;255;180m', '\x1b[38;2;0;255;200m', '\x1b[38;2;0;255;220m', '\x1b[38;2;0;255;240m',
                     '\x1b[38;2;0;220;255m', '\x1b[38;2;0;200;255m', '\x1b[38;2;0;180;255m', '\x1b[38;2;0;160;255m',
                     '\x1b[38;2;0;140;255m', '\x1b[38;2;0;120;255m', '\x1b[38;2;0;100;255m', '\x1b[38;2;0;80;255m',
                     '\x1b[38;2;0;60;255m', '\x1b[38;2;0;40;255m', '\x1b[38;2;0;20;255m', '\x1b[38;2;0;0;255m',
                     '\x1b[38;2;20;0;255m', '\x1b[38;2;40;0;255m', '\x1b[38;2;60;0;255m', '\x1b[38;2;80;0;255m',
                     '\x1b[38;2;100;0;255m', '\x1b[38;2;120;0;255m', '\x1b[38;2;140;0;255m', '\x1b[38;2;160;0;255m',
                     '\x1b[38;2;180;0;255m', '\x1b[38;2;200;0;255m', '\x1b[38;2;220;0;255m', '\x1b[38;2;240;0;255m',
                     '\x1b[38;2;255;0;220m', '\x1b[38;2;255;0;200m', '\x1b[38;2;255;0;180m', '\x1b[38;2;255;0;160m',
                     '\x1b[38;2;255;0;140m', '\x1b[38;2;255;0;120m', '\x1b[38;2;255;0;100m', '\x1b[38;2;255;0;80m',
                     '\x1b[38;2;255;0;60m', '\x1b[38;2;255;0;40m', '\x1b[38;2;255;0;20m', '\x1b[38;2;255;0;0m']

        self.list.reverse()

        self.mainColors = itertools.cycle(self.list)

    def getTime(self):
        currentTime = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-2]
        return currentTime

    def default(self, text: str, end=None):
        print(
            "{0}[{1}{2}{0}] {0}{3}".format(
                self.theme, next(self.mainColors), self.getTime(), text
            ),
            end=end
        )

    def success(self, text: str, end=None):
        lime = "\x1b[38;2;0;255;0m"
        print(
            "{0}[{1}{2}{0}] {0}{3}{4}{0}".format(
                self.theme, next(self.mainColors), self.getTime(), lime, text
            ),
            end=end
        )

    def error(self, text: str, end=None):
        red = "\x1b[38;2;255;0;0m"
        print(
            "{0}[{1}{2}{0}] {0}{3}{4}{0}".format(
                self.theme, next(self.mainColors), self.getTime(), red, text
            ),
            end=end
        )

    def warn(self, text: str, end=None):
        red = "\x1b[38;2;220;225;0m"
        print(
            "{0}[{1}{2}{0}] {0}{3}{4}{0}".format(
                self.theme, next(self.mainColors), self.getTime(), red, text
            ),
            end=end
        )

    def title(self, text: str):
        if os.name == "nt": os.system("title {}".format(text))
