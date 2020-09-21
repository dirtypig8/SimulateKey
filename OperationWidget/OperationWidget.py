from PyQt5 import QtWidgets

from OperationWidget.IndexWidget import IndexWidget
from OperationWidget.SettingWidget import SettingWidget
from OperationWidget.InputPasswordWidget import InputPasswordWidget

import gc
from LogWriter import LogWriter


class OperationWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.widget_dict = dict()

        self.widget_dict["index"] = self.addWidget(IndexWidget())
        self.widget_dict["setting"] = self.addWidget(SettingWidget())
        self.widget_dict["input_password"] = self.addWidget(InputPasswordWidget())

    def update_current_widget_by_name(self, widget_name):
        index = self.widget_dict[widget_name]
        self.setCurrentIndex(index)

        LogWriter().write_log("update_current_widget_by_name '{}'".format(widget_name))

        current_widget = self.currentWidget()
        if widget_name == "index":
            gc.collect()

        if hasattr(current_widget, "load"):
            current_widget.load()
