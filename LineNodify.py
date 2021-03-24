import requests
import os.path
import time
import random


class LineNodify:
    def __init__(self, token):
        self.token = token

    def execute(self, msg, image_path=None, pic_url=None, sticker_id=None, package_id=None):
        headers = {
            "Authorization": "Bearer " + self.token,
        }
        files = {}
        params = {'message': msg}

        if image_path and os.path.isfile(image_path):
            files = {"imageFile": open(image_path, "rb")}

        # stickerPackageId貼圖主題編號
        # stickerIdLine 貼圖編號
        if sticker_id and package_id:
            params = {**params, "stickerId": sticker_id, "stickerPackageId": package_id}

        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params, files=files)

    def send(self, message, image_path=None, sticker_id=None, package_id=None):
        """Examples:
            notify.send("text test")
            notify.send("image test", image_path='./test.jpg')
            notify.send("sticker test", sticker_id=283, package_id=4)
            notify.send("image & sticker test", image_path='./test.jpg', sticker_id=283, package_id=4)
        :param message: string
        :param image_path: string
        :param sticker_id: integer
        :param package_id: integer
        :return:

        """
        headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {"message": message, "imageFile": image_path}

        if sticker_id and package_id:
            params = {**params, "stickerId": sticker_id, "stickerPackageId": package_id}

        r =requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
        print(r.status_code)

if __name__ == '__main__':
    token = 'cKM2GgU5QbXalTbS7WPGBQoQ9RYjeVClo9muqcSjqtn'
    message = ['我是小仙女，東昇你好帥！', '嗨囉嗨囉', "明天晚上要不要吃飯阿", "小妹本人住在台北哦",
               '\n阿鐘是誰?阿鐘我本人拉\n\n\n李東穎，我幹崊涼拉']
    bot = LineNodify(token)
    # picurl  = 'https // scontent.ftpe7 - 2.fna.fbcdn.net / v / t1.0 - 1 / 12745966_1069703949754501_3553874664941181396_n.jpg?_nc_cat104 & _nc_ocAQn3ZFYMbr17ZdLYJ25dGbbp1hEA3XNrE8tpO6d2Fsd3jWBkgaZejswMLhCSjQL9uW4 & _nc_ht = scontent.ftpe7 - 2.fna & oh = 742bb80d2c169132126fc354293b7b78 & oe = 5E0D9BFB'
    # picurl = 'https://scontent.ftpe7-2.fna.fbcdn.net/v/t1.0-1/12745966_1069703949754501_3553874664941181396_n.jpg?_nc_cat=104&_nc_oc=AQn3ZFYMbr17ZdLYJ25dGbbp1hEA3XNrE8tpO6d2Fsd3jWBkgaZejswMLhCSjQL9uW4&_nc_ht=scontent.ftpe7-2.fna&oh=742bb80d2c169132126fc354293b7b78&oe=5E0D9BFB'
    # bot.send("TEST", image_path='./test.png')
    bot.execute("TEST", pic_url='https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2017-07/fa2c3d72-7fad-4ccf-9857-e90af952b956_m.jpg')
