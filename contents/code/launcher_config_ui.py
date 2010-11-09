# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents/ui/launchers_config.ui'
#
# Created: Thu Sep 10 15:01:43 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(513, 332)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 461, 192))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 210, 461, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = KPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.remove_button = KPushButton(self.horizontalLayoutWidget)
        self.remove_button.setEnabled(False)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.move_up_button = KPushButton(self.horizontalLayoutWidget)
        self.move_up_button.setEnabled(False)
        self.move_up_button.setObjectName("move_up_button")
        self.horizontalLayout.addWidget(self.move_up_button)
        self.move_down_button = KPushButton(self.horizontalLayoutWidget)
        self.move_down_button.setEnabled(False)
        self.move_down_button.setObjectName("move_down_button")
        self.horizontalLayout.addWidget(self.move_down_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Button Title", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.add_button.setText(QtGui.QApplication.translate("Form", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("Form", "remove", None, QtGui.QApplication.UnicodeUTF8))
        self.move_up_button.setText(QtGui.QApplication.translate("Form", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.move_down_button.setText(QtGui.QApplication.translate("Form", "Move Down", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KPushButton
