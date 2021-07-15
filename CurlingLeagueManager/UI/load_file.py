import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from CurlingLeagueManager.team_member import TeamMember

QtBaseWindow, Ui_MainWindow = uic.loadUiType("edit_team_dialog.ui")


class LoadFile(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
