import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from numpy import unicode
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import tkinter

class testDialog(QDialog):
    def __init__(self, parent=None):
        super(testDialog, self).__init__(parent)

        form = QGridLayout()
        form.setHorizontalSpacing(0)
        testDialog.resize(self, 1024, 768)
        testDialog.setObjectName(self, "check_program")

        self.myedit = QLineEdit()
        self.myedit.setDragEnabled(True)
        self.myedit.setAcceptDrops(True)
        self.myedit.installEventFilter(self)

        form.addWidget(self.myedit)

        self.setLayout(form)
        self.setGeometry(600, 90, 401, 251)
        self.setWindowTitle('drop test')

        self.myedit.textChanged.connect(self.editchange)  # new style signal slot connections

        # self.Open_btn = QtWidgets.QPushButton()
        # self.Open_btn.setGeometry(QtCore.QRect(520, 400, 121, 41))
        # self.Open_btn.setObjectName("Open_btn")
        # form.addWidget(self.Open_btn)

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setGeometry(QtCore.QRect(300,500,0,0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        form.addWidget(self.textEdit)


        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        form.addWidget(self.canvas)

        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setGeometry(QtCore.QRect(40, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("원인 1")
        form.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox()
        self.checkBox_2.setGeometry(QtCore.QRect(170, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setText("원인 2")
        form.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox()
        self.checkBox_3.setGeometry(QtCore.QRect(300, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setText("원인 3")
        form.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox()
        self.checkBox_4.setGeometry(QtCore.QRect(40, 670, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setText("원인 4")
        form.addWidget(self.checkBox_4)
        self.ResultSave_btn = QtWidgets.QPushButton()
        self.ResultSave_btn.setGeometry(QtCore.QRect(420, 640, 121, 41))
        self.ResultSave_btn.setObjectName("ResultSave_btn")
        form.addWidget(self.ResultSave_btn)
        self.ResultSave_btn.setText("결과 저장")
        # self.checkBox_5 = QtWidgets.QCheckBox()
        # self.checkBox_5.setGeometry(QtCore.QRect(170, 670, 110, 50))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.checkBox_5.setFont(font)
        # self.checkBox_5.setObjectName("checkBox_5")
        # self.checkBox_6 = QtWidgets.QCheckBox()
        # self.checkBox_6.setGeometry(QtCore.QRect(300, 670, 110, 50))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.checkBox_6.setFont(font)
        # self.checkBox_6.setObjectName("checkBox_6")
        # self.lineEdit = QtWidgets.QLineEdit()
        # self.lineEdit.setGeometry(QtCore.QRect(20, 400, 381, 41))
        # font = QtGui.QFont()
        # font.setPointSize(13)
        # self.lineEdit.setFont(font)
        # self.lineEdit.setText("")
        # if self.lineEdit.textChanged():
        #     linetext = self.lineEdit.text()
        #     print(linetext)
        # drag_and_drop.dragEnterEvent(self, QDragEnterEvent)
        # drag_and_drop.dropEvent(self, QDropEvent)
        # self.lineEdit.setObjectName("lineEdit")
        # self.listWidget = QtWidgets.QListWidget(DataVisualization_prototype)
        # self.listWidget.setGeometry(QtCore.QRect(600, 90, 401, 251))
        # self.listWidget.setObjectName("listWidget")

        self.Save_btn = QtWidgets.QPushButton()
        self.Save_btn.setGeometry(QtCore.QRect(880, 712, 121, 41))
        self.Save_btn.setObjectName("Save_btn")
        self.Save_btn.setText("저장")
        form.addWidget(self.Save_btn)
        # self.file_Dialog = QtWidgets.QPushButton()
        # self.file_Dialog.setGeometry(QtCore.QRect(400, 400, 121, 41))
        # self.file_Dialog.setObjectName("file_Dialog")

        # self.file_Dialog = QPushButton("File Open")
        # self.file_Dialog.clicked.connect(self.fileDialogPressed())
        # self.label = QLabel()
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.file_Dialog)
        # layout.addWidget(self.label)
        #
        # #self.setLayout(layout)

        self.graphView = QtWidgets.QTableView()
        self.graphView.setGeometry(QtCore.QRect(30, 90, 521, 251))
        self.graphView.setObjectName("graphView")

    @QtCore.pyqtSlot(str)  # int represent the column value
    def editchange(self, data):
        print
        "editchange:", unicode(data)

    def eventFilter(self, object, event):
        if (object is self.myedit):
            if (event.type() == QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()  # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    print
                    "accept"
                else:
                    event.ignore()
                    print
                    "ignore"
            if (event.type() == QtCore.QEvent.Drop):
                if event.mimeData().hasUrls():  # if file or link is dropped
                    urlcount = len(event.mimeData().urls())  # count number of drops
                    url = event.mimeData().urls()[0]  # get first url
                    object.setText(unicode(url.toLocalFile()))  # assign first url to editline
                    event.accept()  # doesnt appear to be needed
                    f = open(unicode(url.toLocalFile()),"r")
                    rcv_data = f.read()
                    f.close()
                    print(rcv_data)
                    #self.textEdit.append(rcv_data)
                    fdat_spl = rcv_data.split("\n")
                    j = 1
                    count = 0
                    for i in range(len(fdat_spl)):
                        start_info = fdat_spl[i].find("Range")
                        if start_info == 0:
                            #print(str(j) + ".")
                            self.textEdit.append(str(j)+".")
                            self.textEdit.append(str(fdat_spl[i:i + 36]))
                            count += 1
                            if count % 3 == 0:
                                j += 1

            return False  # lets the event continue to the edit
        return False


if __name__ == "__main__":
    app = QApplication([])
    dl = testDialog()
    dl.exec_()
    sys.exit(app.closeAllWindows())