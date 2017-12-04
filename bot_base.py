import android_handler
import pixel_check

import abc
import time

class BotBase(abc.ABC):
    def __init__(self, loop_sleep_time: int):
        'loop_sleep_time is given in seconds'

        self._android_handler = android_handler.AndroidHandler()
        self._pixel_check = pixel_check.PixelCheck()

        self._loop_sleep = loop_sleep_time

    def run(self) -> None:
        while True:
            self.do_events()
            self.wait(self._loop_sleep)

    def wait(self, seconds: float) -> None:
        time.sleep(seconds)

    @abc.abstractmethod
    def do_events(self) -> None:
        'To be implemented by an extended class'
        pass
