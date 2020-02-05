import sys
import read_all_files_in_dir
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QListView")
        self.setFixedHeight(251)
        self.setFixedWidth(401)

        files = read_all_files_in_dir.file_list

        view = QListView(self)
        model = QStandardItemModel()
        for f in files:
            model.appendRow(QStandardItem(f))
        view.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())