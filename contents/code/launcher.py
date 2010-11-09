from PyKDE4.kio import KRun

class Launcher():
    def __init__(self, button_text, command_string, tooltip_text=None):
        self.button_text = button_text
        self.command_string = command_string
        self.tooltip_text = tooltip_text

    def execute(self):
        KRun.runCommand(self.command_string, None)
