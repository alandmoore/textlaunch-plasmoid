from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdeui import *

from launcher_config_ui import Ui_Form
from launcher import Launcher


class Launcher_Config(QWidget, Ui_Form):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.launchers = parent.launchers
        self.launchers.reverse()
        #populate the table
        for launcher in self.launchers:
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(launcher.button_text))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(launcher.command_string))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(launcher.tooltip_text))
        
        self.connect(self.add_button, SIGNAL("clicked()"), self.newRow)
        self.connect(self.remove_button, SIGNAL("clicked()"), self.killRow)
        self.connect(self.tableWidget, SIGNAL("itemSelectionChanged()"), self.toggle_selection_specific_buttons)
        self.connect(self.move_up_button, SIGNAL("clicked()"), self.move_row_up)
        self.connect(self.move_down_button, SIGNAL("clicked()"), self.move_row_down)

    def newRow(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        
    def killRow(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def get_launcher_list(self):
        launchers = []
        for rownum in range(self.tableWidget.rowCount()):
            display_rownum = int(rownum) + 1
            button_text = self.tableWidget.item(rownum, 0) and unicode(self.tableWidget.item(rownum, 0).text())
            command_string = self.tableWidget.item(rownum, 1) and unicode(self.tableWidget.item(rownum, 1).text())
            tooltip_text = (self.tableWidget.item(rownum, 2) and unicode(self.tableWidget.item(rownum, 2).text())) or ""
            if (button_text is not None and  command_string is not None):               launchers.append(Launcher(button_text, command_string, tooltip_text))
            else:
                KMessageBox.error(None, "Launcher #%d could not be added, because it was missing the button text or command string." % display_rownum, "Error adding launcher")

        return launchers

    def toggle_selection_specific_buttons(self):
        enable = len(self.tableWidget.selectedItems()) > 0
        up_enable = self.tableWidget.currentRow() > 0
        down_enable = (self.tableWidget.currentRow() + 1) < self.tableWidget.rowCount()
        self.remove_button.setEnabled(enable)
        self.move_up_button.setEnabled(enable and  up_enable)
        self.move_down_button.setEnabled(enable and down_enable)
    
    def move_row_up(self):
        source = self.tableWidget.currentRow()
        destination = source - 1
        self.row_swap(source, destination)
    def move_row_down(self):
        source = self.tableWidget.currentRow()
        destination = source + 1
        self.row_swap(source, destination)

    def row_swap(self, source, destination):
        for field in range(self.tableWidget.columnCount()):
            item = self.tableWidget.takeItem(source, field)
            self.tableWidget.setItem(source, field, self.tableWidget.takeItem(destination, field))
            self.tableWidget.setItem(destination, field, item)
        self.tableWidget.setCurrentCell(destination, self.tableWidget.currentColumn())
