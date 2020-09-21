from PyQt5 import QtWidgets, QtCore, QtGui
from CoreConfig.ResourceGetter import ResourceGetter
from FontStretchingWidget import FontStretchingLabel, FontStretchingButton
from OperationWidget.OperationWidgetUpdater import OperationWidgetUpdater
from PublicData.QueryDataHandler import QueryDataHandler
from CoreConfig.ConfigDictionary import ConfigDictionary
from LogWriter import LogWriter
from CoreConfig.DefaultValues import DefaultQrConfigPathGetter

import json

total_lines = 10

class SettingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout()

        self.config_widget = ConfigWidget()
        self.control_widget = ControlWidget(self.config_widget.write_config)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.config_widget)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName("pay_widget_scroll")
        self.scrollArea.setStyleSheet("border:1;")


        layout.addWidget(self.scrollArea, stretch=70)        
        layout.addWidget(self.control_widget, stretch=30)

        self.setLayout(layout)

    def load(self):
        self.config_widget.reload_config()


class ConfigWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        self.config_label_list = list()
        for i in range(1, total_lines+1):
            new_config_label = ConfigLabel(i)
            self.config_label_list.append(new_config_label)
            layout.addWidget(new_config_label)

        self.setLayout(layout)

    def reload_config(self):
        with open(DefaultQrConfigPathGetter().execute(),'r') as load_f:
            load_dict = json.load(load_f)

        count = 0
        for qr_content in load_dict:
            config_label = self.config_label_list[count]
            config_label.name_text_area.setText(qr_content['name'])
            config_label.event_text_area.setText(qr_content.get("event", ""))
            config_label.sleep_text_area.setText(str(qr_content['sleep']))
            config_label.repeat_text_area.setText(str(qr_content.get('repeat', "")))
            count += 1

    def write_config(self):
        result_dict = list()
        for count in range(total_lines):
            config_label = self.config_label_list[count]
            name = config_label.name_text_area.text()
            event = config_label.event_text_area.text()
            sleep = config_label.sleep_text_area.text()
            repeat = config_label.repeat_text_area.text()
            
            if len(name) > 0:
                single_config = {
                    "name": name,
                    "event": event,
                    "sleep": sleep,
                    "repeat": repeat
                }

                result_dict.append(single_config)
        
        with open(DefaultQrConfigPathGetter().execute(), 'w') as fp:
            json.dump(result_dict, fp)


class ConfigLabel(QtWidgets.QWidget):
    def __init__(self, count):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()

        self.name_label = self.__get_hint_label("規則名稱{}".format(count))
        self.name_text_area = QtWidgets.QLineEdit()
        self.event_label = self.__get_hint_label("按鍵".format(count))
        self.event_text_area = QtWidgets.QLineEdit()
        self.sleep_label = self.__get_hint_label("按完後休息秒數".format(count))
        self.sleep_text_area = QtWidgets.QLineEdit()
        self.repeat_label = self.__get_hint_label("重複次數".format(count))
        self.repeat_text_area = QtWidgets.QLineEdit()

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_text_area)
        layout.addWidget(self.event_label)
        layout.addWidget(self.event_text_area)
        layout.addWidget(self.sleep_label)
        layout.addWidget(self.sleep_text_area)
        layout.addWidget(self.repeat_label)
        layout.addWidget(self.repeat_text_area)

        self.setLayout(layout)

    def __get_hint_label(self, text):
        hint_label = QtWidgets.QLabel()
        hint_label.setText(text)

        return hint_label
            
    def __get_text_area(self, text):
        text_area = QtWidgets.QLineEdit()

        return text_area


class ControlWidget(QtWidgets.QWidget):
    def __init__(self, write_config_callback):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.write_config_callback = write_config_callback
        self.hint_label = self.__get_hint_label()
        self.save_button = self.__get_save_button()
        self.back_button = self.__get_back_button()
        layout.addWidget(self.hint_label, stretch=40)
        layout.addWidget(self.save_button, stretch=30)
        layout.addWidget(self.back_button, stretch=30)

        self.setLayout(layout)

    def __get_hint_label(self):
        hint_label = QtWidgets.QLabel()
        hint_label.setText("")
        hint_label.setAlignment(QtCore.Qt.AlignCenter)
        hint_label.setObjectName("decide_widget_label")
        hint_label.setStyleSheet(
            """
              QLabel#decide_widget_label
              {{
                color: black;
              }};
            """
        )
        return hint_label

    def __get_back_button(self):
        button = FontStretchingButton(resize_ratio=0.3)
        button.setText("返回首頁")
        button.setObjectName("decide_widget_button")
        # button.setStyleSheet(
        #     """
        #       QPushButton#decide_widget_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )
        button.clicked.connect(lambda: self.go_back())

        return button

    def go_back(self):
        OperationWidgetUpdater.update_widget_by_command("back")

    def __get_save_button(self):
        button = FontStretchingButton(resize_ratio=0.3)
        button.setText("儲存設定")
        button.setObjectName("decide_widget_button")
        # button.setStyleSheet(
        #     """
        #       QPushButton#decide_widget_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )
        button.clicked.connect(lambda: self.save())

        return button

    def save(self):
        self.write_config_callback()
        self.hint_label.setText("儲存成功 請重開程式")
