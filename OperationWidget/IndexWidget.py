from PyQt5 import QtWidgets, QtCore, QtGui
from OperationWidget.OperationWidgetUpdater import OperationWidgetUpdater
from FontStretchingWidget import FontStretchingLabel, FontStretchingButton
from CoreConfig.ConfigDictionary import ConfigDictionary
from CoreConfig.ResourceGetter import ResourceGetter
from LogWriter import LogWriter
from PublicData.QueryDataHandler import QueryDataHandler
from CoreConfig.DefaultValues import DefaultQrConfigPathGetter
# from ThermalXmlGenerators.StandardThermalXmlGenerator import StandardThermalXmlGenerator
# from ModuleControllingCommand.ThermalPrinter import Print
from datetime import datetime
import requests
import json
import string
import random
import hashlib


# XmlGenerator = {
#     "standard": StandardThermalXmlGenerator
# }


class IndexWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout()
        self.work_widget = TextShowingLabel()
        self.control_widget = ControlWidget(self.work_widget.rest)




        layout.addWidget(self.work_widget, stretch=70)
        layout.addWidget(self.control_widget, stretch=30)

        self.setLayout(layout)

    def load(self):
        self.control_widget.hint_label.setText("")


class TextShowingLabel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("index_widget_text_label")

        layout = QtWidgets.QGridLayout()
        self.cur_button = QrButton("啟動", "Start", "")
        layout.addWidget(self.cur_button)

        # with open(DefaultQrConfigPathGetter().execute(),'r') as load_f:
        #     load_dict = json.load(load_f)
        #
        # count = 0
        # for qr_item in load_dict['qr_list']:
        #     cur_button = QrButton(qr_item['rule_name'], qr_item['rule_id'], info_shower)
        #     layout.addWidget(cur_button, count/2, count%2, 1, 1)
        #     count += 1

        self.setLayout(layout)

    def rest(self):
        self.cur_button.init_button()

class QrButton(FontStretchingButton):
    def __init__(self, rule_name, rule_id, info_shower):
        super().__init__(resize_ratio=0.3)
        # QueryDataHandler.process_status = False
        self.info_shower = info_shower
        self.rule_name = rule_name
        self.rule_id = rule_id
        self.setObjectName("main_widget_button")
        # self.setStyleSheet(
        #     """
        #       QPushButton#main_widget_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )
        self.init_button()

        self.clicked.connect(lambda: self.switch_button())

    def init_button(self):
        QueryDataHandler.process_status = False
        self.setText("開始")

    def switch_button(self):
        if QueryDataHandler.process_status is False:
            self.setText("暫停")
            QueryDataHandler.process_status = True
        else:
            self.setText("開始")
            QueryDataHandler.process_status = False
        # self.info_shower.setText("列印中 .... ")
        # random_string = ''.join(random.choice(string.ascii_uppercase) for x in range(32))
        # expiry_date = datetime.now().strftime("%Y%m%d")+"235959"
        # data_list = [
        #     random_string,
        #     ConfigDictionary.config_dict['shop_id'],
        #     ConfigDictionary.config_dict['lot_id'],
        #     self.rule_id,
        #     expiry_date
        #    ]
        # data = ",".join(data_list)
        # plain_text = data+ConfigDictionary.config_dict['api_key']
        #
        # sha = hashlib.sha256()
        # sha.update(plain_text.encode('utf-8'))
        # hashed_text = sha.hexdigest()
        # qr_content = "Off:"+data+","+hashed_text[:8]+hashed_text[-8:]
        #
        # qr_data = {
        #     'expiry_date': expiry_date,
        #     'qr_content': qr_content,
        #     'rule_name': self.rule_name
        # }
        #
        # thermal_xml_file = self.generate_thermal_xml(qr_data)
        # LogWriter().write_log("generated thermal xml is '{}'".format(thermal_xml_file))
        # try:
        #     # Print(Print.thermal_socket_client, None, thermal_xml_file).execute()
        #     self.info_shower.setText("列印完成")
        # except Exception as e:
        #     LogWriter().write_log("Thermal printer exception {}".format(e))
        #     self.info_shower.setText("印表機連線異常")

    # def generate_thermal_xml(self, qr_data):
    #     target = ConfigDictionary.config_dict['qr_format']
        # thermal_xml_file = XmlGenerator[target]().execute(qr_data)
        # return thermal_xml_file


class ControlWidget(QtWidgets.QWidget):
    first_time = True

    def __init__(self, rest_work_widget):
        super().__init__()
        self.rest_work_widget = rest_work_widget
        layout = QtWidgets.QVBoxLayout()
        self.hint_label = self.__get_hint_label()
        self.button = self.__get_confirm_button()
        layout.addWidget(self.hint_label, stretch=70)
        layout.addWidget(self.button, stretch=30)

        self.setLayout(layout)

    def __get_hint_label(self):
        hint_label = QtWidgets.QLabel()
        hint_label.setText("")
        hint_label.setAlignment(QtCore.Qt.AlignCenter)
        hint_label.setObjectName("main_widget_label")
        hint_label.setStyleSheet("color: red;")
        hint_label.setFont(QtGui.QFont("微軟正黑體", 16))

        return hint_label

    def __get_confirm_button(self):
        button = FontStretchingButton(resize_ratio=0.3)
        button.setText("進入設定頁面")
        button.setObjectName("main_widget_button")
        # button.setStyleSheet(
        #     """
        #       QPushButton#main_widget_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )
        button.clicked.connect(lambda: self.query_operation())

        return button

    def query_operation(self):
        self.rest_work_widget()
        OperationWidgetUpdater().update_widget_by_command("next")


