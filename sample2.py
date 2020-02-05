# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataVisualization_prototype(object):
    def setupUi(self, DataVisualization_prototype):
        DataVisualization_prototype.setObjectName("DataVisualization_prototype")
        DataVisualization_prototype.resize(1024, 768)
        self.Open_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Open_btn.setGeometry(QtCore.QRect(420, 400, 121, 41))
        self.Open_btn.setObjectName("Open_btn")
        self.Save_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Save_btn.setGeometry(QtCore.QRect(880, 712, 121, 41))
        self.Save_btn.setObjectName("Save_btn")
        self.checkBox = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox.setGeometry(QtCore.QRect(40, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox_3.setGeometry(QtCore.QRect(300, 610, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox_4.setGeometry(QtCore.QRect(40, 670, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox_5.setGeometry(QtCore.QRect(170, 670, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(DataVisualization_prototype)
        self.checkBox_6.setGeometry(QtCore.QRect(300, 670, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.lineEdit = QtWidgets.QLineEdit(DataVisualization_prototype)
        self.lineEdit.setGeometry(QtCore.QRect(20, 400, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(DataVisualization_prototype)
        self.listWidget.setGeometry(QtCore.QRect(600, 90, 401, 251))
        self.listWidget.setObjectName("listWidget")
        self.Graphs = QtWidgets.QLabel(DataVisualization_prototype)
        self.Graphs.setGeometry(QtCore.QRect(20, 50, 521, 291))
        self.Graphs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Graphs.setObjectName("Graphs")
        self.ResultSave_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.ResultSave_btn.setGeometry(QtCore.QRect(420, 640, 121, 41))
        self.ResultSave_btn.setObjectName("ResultSave_btn")
        self.Search_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Search_btn.setGeometry(QtCore.QRect(560, 400, 121, 41))
        self.Search_btn.setObjectName("Search_btn")

        self.retranslateUi(DataVisualization_prototype)
        QtCore.QMetaObject.connectSlotsByName(DataVisualization_prototype)

    def retranslateUi(self, DataVisualization_prototype):
        _translate = QtCore.QCoreApplication.translate
        DataVisualization_prototype.setWindowTitle(_translate("DataVisualization_prototype", "Dialog"))
        self.Open_btn.setText(_translate("DataVisualization_prototype", "Open"))
        self.Save_btn.setText(_translate("DataVisualization_prototype", "FileSave"))
        self.checkBox.setText(_translate("DataVisualization_prototype", "원인1"))
        self.checkBox_2.setText(_translate("DataVisualization_prototype", "원인2"))
        self.checkBox_3.setText(_translate("DataVisualization_prototype", "원인3"))
        self.checkBox_4.setText(_translate("DataVisualization_prototype", "원인4"))
        self.checkBox_5.setText(_translate("DataVisualization_prototype", "원인5"))
        self.checkBox_6.setText(_translate("DataVisualization_prototype", "원인6"))
        self.Graphs.setText(_translate("DataVisualization_prototype", "그래프 표시"))
        self.ResultSave_btn.setText(_translate("DataVisualization_prototype", "ResultSave"))
        self.Search_btn.setText(_translate("DataVisualization_prototype", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataVisualization_prototype = QtWidgets.QDialog()
    ui = Ui_DataVisualization_prototype()
    ui.setupUi(DataVisualization_prototype)
    DataVisualization_prototype.show()
    sys.exit(app.exec_())
