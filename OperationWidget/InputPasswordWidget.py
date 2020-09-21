from PyQt5 import QtWidgets, QtCore, QtGui
from CoreConfig.ConfigDictionary import ConfigDictionary
from FontStretchingWidget import FontStretchingLabel, FontStretchingButton
from OperationWidget.OperationWidgetUpdater import OperationWidgetUpdater
from CoreConfig.ResourceGetter import ResourceGetter

import os
import json



class InputPasswordWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout()

        self.__text_showing_label = TextShowingLabel()
        self.control_widget = ControlWidget()

        layout.addWidget(self.__text_showing_label, stretch=60)
        layout.addWidget(self.control_widget, stretch=40)

        self.setLayout(layout)

    def load(self):
        self.control_widget.clear_hint()
        self.control_widget.keyboard.clear_text()


class TextShowingLabel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QGridLayout()

        self.setLayout(layout)


class ControlWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()

        self.input_passwd = self.__set_text_info("請輸入密碼")
        self.passwd_line = QtWidgets.QLineEdit()
        self.passwd_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hint_label = self.__get_hint_label()
        self.keyboard = KeyboardWidget(self.passwd_line.setText)

        layout.addWidget(self.input_passwd, 0, 0, 1, 1)
        layout.addWidget(self.passwd_line, 0, 1, 1, 1)
        layout.addWidget(self.__confirm_button(), 1, 0, 1, 1)
        layout.addWidget(self.__cancel_button(), 1, 1, 1, 1)
        layout.addWidget(self.hint_label, 3, 0, 1, 2)
        layout.addWidget(self.keyboard, 2, 0, 1, 2)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 3)
        layout.setRowStretch(3, 1)

        self.setLayout(layout)

    def __set_text_info(self, text):
        textLabel = FontStretchingLabel(resize_ratio=0.5)
        textLabel.setAlignment(QtCore.Qt.AlignLeft)
        textLabel.setText(text)

        return textLabel

    def clear_hint(self):
        self.hint_label.setText("")

    def __get_hint_label(self):
        hint_label = QtWidgets.QLabel()
        hint_label.setText("")
        hint_label.setAlignment(QtCore.Qt.AlignCenter)

        return hint_label

    def send_command(self):
        passwd = self.passwd_line.text()
        self.passwd_line.clear()
        self.keyboard.clear_text()
        if passwd == ConfigDictionary().config_dict["password"]:
            OperationWidgetUpdater.update_widget_by_command("next")
        else:
            self.hint_label.setText("密碼輸入錯誤")

    def __confirm_button(self):
        update_button = FontStretchingButton(resize_ratio=0.3)
        update_button.setText("確定")
        update_button.setObjectName("input_passwd_widget_confirm_button")
        # update_button.setStyleSheet(
        #     """
        #       QPushButton#input_passwd_widget_confirm_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )

        update_button.clicked.connect(lambda: self.send_command())

        return update_button

    def __cancel_button(self):
        cancel_button = FontStretchingButton(resize_ratio=0.3)
        cancel_button.setText("取消")
        cancel_button.setObjectName("input_passwd_widget_cancel_button")
        # cancel_button.setStyleSheet(
        #     """
        #       QPushButton#input_passwd_widget_cancel_button
        #       {{
        #         color: white;
        #         border-image: url(\"{}\");
        #       }}
        #     """.format(ResourceGetter.get_resource("Base", "confirm_button.png"))
        # )

        cancel_button.clicked.connect(lambda: OperationWidgetUpdater.update_widget_by_command("back"))

        return cancel_button


class KeyboardWidget(QtWidgets.QWidget):
    def __init__(self, qedit_set_text):
        super().__init__()
        self.qedit_set_text = qedit_set_text
        self.inputted_text = str()

        layout = QtWidgets.QGridLayout()

        self.__add_character_input_key_to_layout(layout)
        self.clear_button = self.__add_clear_button_to_layout(layout)

        self.setLayout(layout)

    def clear_text(self):
        self.inputted_text = str()
        self.qedit_set_text("")

    def __add_character_input_key_to_layout(self, layout):
        for i in range(0, 4, 1):  # 0-3
            layout.addWidget(self.__get_single_character_input_key(str(i)), 0, i, 1, 1)

        for i in range(4, 8, 1):  # 4-7
            layout.addWidget(self.__get_single_character_input_key(str(i)), 1, i - 4, 1, 1)

        for i in range(8, 10, 1):  # 8-9
            layout.addWidget(self.__get_single_character_input_key(str(i)), 2, i - 8, 1, 1)

    def __get_single_character_input_key(self, character):
        button = FontStretchingButton(resize_ratio=0.5)
        button.setObjectName("input_tax_code_widget_key_{}".format(character))
        button.setText(character)
        button.clicked.connect(lambda: self.insert_new_text(character))

        return button

    def insert_new_text(self, ch):
        self.inputted_text += ch
        self.qedit_set_text(self.inputted_text)

    def __add_clear_button_to_layout(self, layout):
        button = FontStretchingButton(resize_ratio=0.5)
        button.setObjectName("input_tax_code_widget_clear")
        button.setText("清除")
        button.clicked.connect(lambda: self.clear_text())

        layout.addWidget(button, 2, 2, 1, 2)

        return button
