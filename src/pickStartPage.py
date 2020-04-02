import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton
from PyQt5.uic import loadUi

import SettingView

class PickStartPage(QMainWindow):
    def __init__(self):
        super(PickStartPage, self).__init__()
        loadUi('../ui/pickStartPage.ui', self)

        self.settingsConfig = self.findChild(QPushButton, 'CreateNew_pushButton')
        self.settingsConfig.clicked.connect(self.openSettings)

        self.show()

    def openSettings(self):
        self.window = SettingView.SettingsWindow()
        self.window.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PickStartPage()
    app.exec_()

