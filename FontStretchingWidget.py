from PyQt5 import QtWidgets, QtGui


class FontStretchingLabel(QtWidgets.QLabel):
    def __init__(self, resize_ratio: float):
        super().__init__()
        self.resize_ratio = resize_ratio
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setFont(QtGui.QFont("微軟正黑體"))

    def resizeEvent(self, *args, **kwargs):
        font = self.font()
        font.setPixelSize(self.height() * self.resize_ratio)
        self.setFont(font)


class FontStretchingButton(QtWidgets.QPushButton):
    def __init__(self, resize_ratio: float):
        super().__init__()
        self.resize_ratio = resize_ratio
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setFont(QtGui.QFont("微軟正黑體"))

    def resizeEvent(self, *args, **kwargs):
        font = self.font()
        font.setPixelSize(self.height() * self.resize_ratio)
        self.setFont(font)
