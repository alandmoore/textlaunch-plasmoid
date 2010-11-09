from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdeui import *

from appearance_config_ui import Ui_Form


class Appearance_Config(QWidget, Ui_Form):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.parent=parent
        self.setupUi(self)
        if self.parent.use_fixed_width:
            self.fixed_width_button.click()
            self.width_slider.setValue(parent.fixed_width)
        else:
            self.auto_width_button.click()

        if self.parent.layout_orientation == Qt.Horizontal:
            self.horizontal_layout_button.click()
        else:
            self.vertical_layout_button.click()

        if self.parent.background_type == QString("translucent"):
            self.translucent_background_button.click()
        else:
            self.default_background_button.click()


    def get_use_fixed_width(self):
        return self.fixed_width_button.isChecked()

    def get_fixed_width(self):
        return self.width_slider.value()

    def get_layout_orientation(self):
        if self.vertical_layout_button.isChecked():
            return Qt.Vertical
        else:
            return Qt.Horizontal

    def get_background_type(self):
        if self.translucent_background_button.isChecked():
            return QString("translucent")
        else:
            return QString("default")
