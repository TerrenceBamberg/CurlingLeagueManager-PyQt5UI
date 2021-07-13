import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

QtBaseWindow, Ui_MainWindow = uic.loadUiType("main_window.ui")

#from league_database import LeagueDatabase

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self._leagues = []
        self.add_button.clicked.connect(self.add_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)

    def add_button_clicked(self):
        league_name = self.add_line_edit.text().strip()
        if league_name == "":
            pass
        else:
            self.league_list_widget.addItem(league_name)
            self._leagues.append(league_name)
            print("clicked")

    def update_ui(self):
        self.league_list_widget.clear()
        for l in self._leagues:
            self.league_list_widget.addItem(str(l))

    def edit_button_clicked(self):
        row = self.league_list_widget.currentRow()
        league = self._leagues[row]
        #dialog = EditDialog(league)

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