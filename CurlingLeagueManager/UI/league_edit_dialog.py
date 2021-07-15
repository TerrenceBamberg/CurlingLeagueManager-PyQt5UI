import random
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from CurlingLeagueManager.UI.team_edit_dialog import EditDialogTeam
from CurlingLeagueManager.team import Team

QtBaseWindow, Ui_MainWindow = uic.loadUiType("edit_league_dialog2.ui")


class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, league=None, parent=None):
        super().__init__(parent)
        self._teams = []
        self.setupUi(self)
        #self.add_team_button.clicked.connect(self.add_team_button_clicked)
        self.edit_team_button.clicked.connect(self.edit_team_button_clicked)
        self.delete_team_button.clicked.connect(self.delete_team_button_clicked)

        if league:
            for t in league._teams:
                self.team_list_widget.addItem(str(t))

    def add_team_button_clicked(self, league):
        team_name = self.add_team_line_edit.text().strip()
        if team_name == "":
            pass
        else:
            n = random.randint(0, 22)
            team = Team(n, self.add_team_line_edit.text())
            self._teams.append(team)
            self.update_ui()


    def update_ui(self):
        self.team_list_widget.clear()
        for t in self._teams:
            self.team_list_widget.addItem(str(t))

    def update_league(self, league):
        for t in self._teams:
            league._teams.append(t)

    def edit_team_button_clicked(self):
        row = self.team_list_widget.currentRow()
        if row == -1:
            return self.warn("Select Team", "You must make a selection!")
        team = self._teams[row]
        dialog = EditDialogTeam(team)
        dialog.show()
        dialog.add_member_button.clicked.connect(dialog.add_member_button_clicked)
        # dialog.accepted.connect(edit_dialog_accepted)
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            dialog.update_team(team)
        self.update_ui()

    def warn(self, message, title):
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def delete_team_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove Team")
        dialog.setText("Are you sure you want to remove this Team?")
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)

        dialog.exec_()
        if dialog.clickedButton() == yes:
            try:
                del self._teams[self.team_list_widget.currentRow()]
                self.update_ui()
            except IndexError as e:
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())
