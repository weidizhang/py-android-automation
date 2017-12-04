from pathlib import Path
from PIL import Image

import subprocess

class AndroidHandler:
    def __init__(self, screen_image_rotation: int = 0):
        'screen_image_rotation is given in degrees'

        self.set_screen_rotation(screen_image_rotation)

    def tap_screen(self, x: int, y: int) -> None:
        self.run_shell_command('input tap ' + str(x) + ' ' + str(y))

    def swipe_screen(self, x_initial: int, y_initial: int, x_final: int, y_final: int, duration_ms: int) -> None:
        self.run_shell_command('input swipe ' + x_initial + ' ' + y_initial + ' ' + x_final + ' ' + y_final + ' ' + duration_ms)

    def hold_press_screen(self, x: int, y: int, duration_ms: int) -> None:
        self.swipe_screen(x, y, x, y, duration_ms)

    def navigate_back(self) -> None:
        self.run_shell_command('input keyevent KEYCODE_BACK')

    def navigate_home(self) -> None:
        self.run_shell_command('input keyevent KEYCODE_HOME')

    def navigate_app_switcher(self) -> None:
        self.run_shell_command('input keyevent KEYCODE_APP_SWITCH')

    def set_screen_rotation(self, degrees: int) -> None:
        self._screen_rotation = degrees

    def get_screen(self) -> Image:
        screenshot_file_name = 'scrn.png'
        screenshot_file = Path(screenshot_file_name)

        if screenshot_file.exists():
            screenshot_file.unlink()

        self.run_shell_command('screencap -p /sdcard/' + screenshot_file_name)
        self.run_adb_command('pull /sdcard/'+ screenshot_file_name)
        self.run_shell_command('rm /sdcard/' + screenshot_file_name)

        screen_image = Image.open(screenshot_file_name)
        if self._screen_rotation != 0:
            screen_image = screen_image.rotate(self._screen_rotation, expand = True)

        return screen_image

    def launch_app(self, package_name: str) -> None:
        self.run_shell_command('monkey -p ' + package_name + ' 1')

    def stop_app(self, package_name: str) -> None:
        self.run_shell_command('am force-stop ' + package_name)

    def run_shell_command(self, command: str) -> None:
        self.run_adb_command('shell ' + command)

    def run_adb_command(self, command: str) -> None:
        adb_process = subprocess.Popen('adb ' + command)
        adb_process.wait()
