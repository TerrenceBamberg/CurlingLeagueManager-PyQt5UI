import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from CurlingLeagueManager.team_member import TeamMember

QtBaseWindow, Ui_MainWindow = uic.loadUiType("edit_team_dialog.ui")


class EditDialogTeam(QtBaseWindow, Ui_MainWindow):
    def __init__(self, team=None, parent=None):
        super().__init__(parent)
        self._team_members = []
        self.setupUi(self)
        #self.add_team_button.clicked.connect(self.add_team_button_clicked)
        self.edit_member_button.clicked.connect(self.edit_member_button_clicked)
        self.delete_member_button.clicked.connect(self.delete_member_button_clicked)

        if team:
            for m in team._members:
                self.member_list_widget.addItem(str(m))

    def add_member_button_clicked(self, team):
        member_name = self.add_member_name_line_edit.text().strip()
        member_email = self.add_member_email_line_edit.text().strip()
        if member_name == "":
            pass
        else:
            member = TeamMember(1, member_name, member_email)
            self._team_members.append(member)
            self.update_ui()


    def update_ui(self):
        self.member_list_widget.clear()
        for m in self._team_members:
            self.member_list_widget.addItem(str(m))

    def update_team(self, team):
        for m in self._team_members:
            team._members.append(m)

    def edit_member_button_clicked(self):
        row = self.member_list_widget.currentRow()
        if row == -1:
            return self.warn("Select Member", "You must make a selection!")
        member = self._team_members[row]
        member.name = self.add_member_name_line_edit_2.text().strip()
        member.email = self.add_member_email_line_edit_2.text().strip()
        self.update_ui()

    def warn(self, message, title):
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def delete_member_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove Team")
        dialog.setText("Are you sure you want to remove this Team Member?")
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)

        dialog.exec_()
        if dialog.clickedButton() == yes:
            try:
                del self._team_members[self.member_list_widget.currentRow()]
                self.update_ui()
            except IndexError as e:
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialogTeam()
    window.show()
    sys.exit(app.exec_())
