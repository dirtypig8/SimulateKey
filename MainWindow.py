from PyQt5 import QtWidgets, QtGui, QtCore
from OperationWidget.OperationWidget import OperationWidget
from OperationWidget.OperationWidgetUpdater import OperationWidgetUpdater
from CoreConfig.ResourceGetter import ResourceGetter
from CoreConfig.ConfigDictionary import ConfigDictionary
from FontStretchingWidget import FontStretchingLabel
from datetime import datetime


class MainWindow:
    @staticmethod
    def get_main_window():
        main_window = QtWidgets.QWidget()
        main_window.setObjectName("main_window")
        # main_window.setStyleSheet(
        #     "QWidget#main_window{{border-image: url(\"{}\")}};".format(ResourceGetter.get_resource("Base", "base.png"))
        # )

        layout = QtWidgets.QVBoxLayout()
        operation_widget = OperationWidget()

        OperationWidgetUpdater.operation_widget = operation_widget
        OperationWidgetUpdater.operation_widget.update_current_widget_by_name("index")
        OperationWidgetUpdater.set_state("index")

        layout.addWidget(HeaderWidget().get_header_widget(), stretch=18)
        layout.addWidget(operation_widget, stretch=72)
        layout.addWidget(FooterWidget().get_footer_widget(), stretch=10)

        main_window.setLayout(layout)

        return main_window


class HeaderWidget:
    def get_header_widget(self):
        header_widget = QtWidgets.QWidget()
        header_widget.setObjectName("header_widget")
        # header_widget.setStyleSheet(
        #     "QWidget#header_widget{{border-image: url(\"{}\")}};".format(
        #         ResourceGetter.get_resource("Base", "header_logo.png")
        #     )
        # )

        layout = QtWidgets.QHBoxLayout()
        name_label = self.__get_name_label()
        # layout.addWidget(FontStretchingLabel(resize_ratio=0.7), stretch=26)
        # layout.addWidget(name_label, stretch=74)
        layout.addWidget(name_label)
        header_widget.setLayout(layout)
        return header_widget

    @staticmethod
    def __get_name_label():
        name_label = FontStretchingLabel(resize_ratio=0.6)
        name_label.setAlignment(QtCore.Qt.AlignCenter)
        name_label.setStyleSheet("color: {};".format(ConfigDictionary().config_dict["name_color"]))
        name_label.setText("{}".format("腳本"))
        return name_label


class FooterWidget:
    def get_footer_widget(self):
        footer_widget = QtWidgets.QWidget()

        layout = QtWidgets.QHBoxLayout()
        # cash_clearing_logo_button = CashClearingLogoButton()
        timer_label = self.__get_timer_label()
        author_label = self.__get_author_label()
        # layout.addWidget(cash_clearing_logo_button, stretch=1)
        # layout.addWidget(timer_label, stretch=9)
        layout.addWidget(timer_label)
        layout.addWidget(author_label)
        footer_widget.setLayout(layout)

        return footer_widget

    @staticmethod
    def __get_timer_label():
        timer_label = FontStretchingLabel(resize_ratio=0.6)
        timer_label.setAlignment(QtCore.Qt.AlignLeft)
        timer_label.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        timer = QtCore.QTimer(timer_label)
        timer.timeout.connect(lambda: timer_label.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        timer.start(1)

        return timer_label

    @staticmethod
    def __get_author_label():
        timer_label = FontStretchingLabel(resize_ratio=0.5)
        timer_label.setAlignment(QtCore.Qt.AlignRight)
        timer_label.setText("作者信箱:{}".format("dirtypig8@gmail.com"))

        return timer_label


class CashClearingLogoButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("footer_widget_logo_label")
        # self.setStyleSheet(
        #     "QPushButton#footer_widget_logo_label{{border-image: url(\"{}\")}};".format(
        #         ResourceGetter.get_resource("Base", "footer_logo.png")
        #     )
        # )

