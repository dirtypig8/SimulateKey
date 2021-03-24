from PIL import ImageGrab
from LineNodify import LineNodify
from datetime import datetime
import time
import os


class ScreenInformProcess:
    def __init__(self):
        self.line_token = 'cKM2GgU5QbXalTbS7WPGBQoQ9RYjeVClo9muqcSjqtn'
        self.line_notify = LineNodify(self.line_token)
        self.sleep_sec = 60

    def execute(self):
        while True:
            try:
                now_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                img_path = self.get_screen_shots_path(file_name=now_time)

                message = '\n{}'.format(now_time)
                self.line_notify.execute(message, image_path=img_path)
            except Exception as e:
                print(e)
            finally:
                self.del_file(img_path)
            time.sleep(self.sleep_sec)

    def get_screen_shots_path(self, file_name='screen_shots'):
        path = '.\\{}.jpg'.format(file_name)
        im = ImageGrab.grab()
        im.save(path)
        return path

    def del_file(self, filepath):
        try:
            os.remove(filepath)
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")