 # -*- coding: utf-8 -*-
##TextLaunch##
# A launcher with text buttons instead of icons
# for people who don't like icons all the time
# By Alan D Moore http://www.alandmoore.com (me at alan d moore dot com)
# Released under the terms of the GNU GPL2 or later
# see the included "COPYING" file for details.


import pickle

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4.kio import KRun
from PyKDE4 import plasmascript
from PyKDE4 import kdeui

from launcherConfig import Launcher_Config
from launcher import Launcher
from appearanceConfig import Appearance_Config

class TextLaunch(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
        self.default_launchers = pickle.dumps([
            Launcher("Web", "konqueror", "Konqueror Web Browser"),
            Launcher("Terminal", "konsole", "Konsole X11 terminal"),
            Launcher("Home", "dolphin ~", "Home directory")
            ])
        self.mylayout = None
        self.parent=parent
       
    def init(self):
        self.setHasConfigurationInterface(True)
        #Get configuration
        self.configuration = self.config()
        self.launchers = str(self.configuration.readEntry("launchers", self.default_launchers).toString())
        self.launchers = pickle.loads(self.launchers)
        self.use_fixed_width = (self.configuration.readEntry("use_fixed_width", False).toBool())
        self.fixed_width = self.configuration.readEntry("fixed_width", 100).toInt()[0]
        self.layout_orientation = self.configuration.readEntry("layout_orientation", Qt.Horizontal).toInt()[0]
        self.background_type = self.configuration.readEntry("background_type", "default").toString()
        #basic setup
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.set_background()
        self.refresh_launchers()


    def createConfigurationInterface(self, parent):
        self.launchers_config = Launcher_Config(self)
        p = parent.addPage(self.launchers_config, "Launchers")
        p.setIcon(kdeui.KIcon("preferences-other"))

        self.appearance_config = Appearance_Config(self)
        p2 = parent.addPage(self.appearance_config, "Appearance")
        p2.setIcon(kdeui.KIcon("preferences-color"))
        self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
        self.connect(parent, SIGNAL("cancelClicked()"), self.configDenied)

    def showConfigurationInterface(self):
        self.dialog = kdeui.KPageDialog()
        self.dialog.setFaceType(kdeui.KPageDialog.List)
        self.dialog.setButtons(kdeui.KDialog.ButtonCode(kdeui.KDialog.Ok |kdeui.KDialog.Cancel))
        self.createConfigurationInterface(self.dialog)
        self.dialog.resize(640, 400)
        self.dialog.show()

    def configAccepted(self):
        self.launchers = self.launchers_config.get_launcher_list()
        self.use_fixed_width = self.appearance_config.get_use_fixed_width()
        self.fixed_width = self.appearance_config.get_fixed_width()
        self.layout_orientation = self.appearance_config.get_layout_orientation()
        self.background_type = self.appearance_config.get_background_type()
        
        self.refresh_launchers()
        self.set_background()
        #save data
        self.configuration.writeEntry("launchers", QVariant(pickle.dumps(self.launchers)))
        self.configuration.writeEntry("use_fixed_width", QVariant(self.use_fixed_width))
        self.configuration.writeEntry("fixed_width", QVariant(self.fixed_width))
        self.configuration.writeEntry("layout_orientation", QVariant(self.layout_orientation))
        self.configuration.writeEntry("background_type", QVariant(self.background_type))
        
        
    def configDenied(self):
        pass

    def set_background(self):
        if self.background_type == QString("translucent"):
            self.setBackgroundHints(Plasma.Applet.TranslucentBackground)
        else:
            self.setBackgroundHints(Plasma.Applet.DefaultBackground)

    def refresh_launchers(self):
        if self.mylayout:
            self.remove_buttons()
        self.mylayout = QGraphicsLinearLayout(self.layout_orientation, self.applet)

        for a_launcher in self.launchers:
            button = Plasma.ToolButton()
            button.setText(a_launcher.button_text)
            #Tooltips
            tt_data = Plasma.ToolTipContent(a_launcher.button_text, a_launcher.tooltip_text, QIcon())
            Plasma.ToolTipManager.self().setContent(button, tt_data)

            #fixed width or not:
            if self.use_fixed_width:
                button.nativeWidget().setFixedWidth(self.fixed_width)
            #adjust button height?
            #button.nativeWidget().setFixedHeight(20)

            #connect and add
            self.connect(button, SIGNAL("clicked()"), a_launcher.execute)
            self.mylayout.addItem(button)
        self.mylayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.mylayout)

    def remove_buttons(self):
        while self.mylayout.count() != 0:
            self.mylayout.removeItem(self.mylayout.itemAt(0))

    
        
def CreateApplet(parent):
    return TextLaunch(parent)
