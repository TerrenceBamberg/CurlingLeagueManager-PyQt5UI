import sys
import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from CurlingLeagueManager import league_database
from CurlingLeagueManager.UI.league_edit_dialog import EditDialog
from CurlingLeagueManager.UI.load_file import LoadFile
from CurlingLeagueManager.league import League


QtBaseWindow, Ui_MainWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self._leagues = []
        self.add_button.clicked.connect(self.add_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.import_button.clicked.connect(self.import_button_clicked)

    def import_button_clicked(self):
        dialog = LoadFile()
        dialog.show()

    def add_button_clicked(self):
        league_name = self.add_line_edit.text().strip()
        if league_name == "":
            pass
        else:
            n = random.randint(0, 22)
            league = League(n, self.add_line_edit.text())
            self._leagues.append(league)
            self.update_ui()

    def update_ui(self):
        self.league_list_widget.clear()
        for l in self._leagues:
            self.league_list_widget.addItem(str(l))

    def edit_button_clicked(self):
        row = self.league_list_widget.currentRow()
        if row == -1:
            return self.warn("Select League", "You must make a selection!")
        league = self._leagues[row]
        dialog = EditDialog(league)
        dialog.show()
        dialog.add_team_button.clicked.connect(dialog.add_team_button_clicked)
        #dialog.accepted.connect(edit_dialog_accepted)
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            dialog.update_league(league)
        self.update_ui()

    def warn(self, message, title):
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def delete_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove League")
        dialog.setText("Are you sure you want to remove this league?")
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)

        dialog.exec_()
        if dialog.clickedButton() == yes:
            try:
                del self._leagues[self.league_list_widget.currentRow()]
                self.update_ui()
            except IndexError as e:
                pass







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())