import android_handler
import pixel_check

import abc
import time

class BotBase(abc.ABC):
    def __init__(self, loop_sleep_time: float = 0.1, screen_image_rotation: int = 0):
        'loop_sleep_time is given in seconds'

        self._android_handler = android_handler.AndroidHandler(screen_image_rotation)
        self._pixel_check = pixel_check.PixelCheck()

        self.set_loop_sleep(loop_sleep_time)

    def run(self) -> None:
        while True:
            self._do_events()
            self.wait(self._loop_sleep)

    def wait(self, seconds: float) -> None:
        time.sleep(seconds)

    def set_loop_sleep(self, seconds: float) -> None:
        self._loop_sleep = seconds

    @abc.abstractmethod
    def _do_events(self) -> None:
        'To be implemented by an extended class'
        pass

    def _log_message(self, message: str) -> None:
        current_time = time.strftime('%c')
        print('[' + current_time + '] ' + message)
