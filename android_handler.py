from pathlib import Path
from PIL import Image

import os

class AndroidHandler:
    def tap_screen(self, x: int, y: int) -> None:
        self._run_shell_command('input tap ' + str(x) + ' ' + str(y))

    def get_screen(self) -> Image:
        screenshot_file_name = 'scrn.png'
        screenshot_file = Path(screenshot_file_name)

        if screenshot_file.exists():
            screenshot_file.unlink()

        self._run_shell_command('screencap -p /sdcard/' + screenshot_file_name)
        self._run_adb_command('pull /sdcard/'+ screenshot_file_name)
        self._run_shell_command('rm /sdcard/' + screenshot_file_name)

        return Image.open(screenshot_file_name)

    def _run_shell_command(self, command: str) -> None:
        self._run_adb_command('shell ' + command)

    def _run_adb_command(self, command: str) -> None:
        os.system('adb ' + command)