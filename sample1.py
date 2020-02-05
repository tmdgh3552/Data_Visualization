# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5.QtGui import QStandardItem, QStandardItemModel

import read_all_files_in_dir
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from tkinter import filedialog

from PyQt5.QtWidgets import QMessageBox, QListView


class Ui_DataVisualization_prototype(object):

    def setupUi(self, DataVisualization_prototype):
        DataVisualization_prototype.setObjectName("DataVisualization_prototype")
        DataVisualization_prototype.resize(1024, 768)
        self.lineEdit = QtWidgets.QLineEdit(DataVisualization_prototype)
        self.lineEdit.setGeometry(QtCore.QRect(20, 400, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        ##파일명
        self.lineEdit.setFont(font)
        #self.lineEdit.setText("Insert file name to open.")
        self.lineEdit.setObjectName("openfilename")
        # if self.lineEdit.mousePressEvent():
        #     self.lineEdit.setText("")

        ## 파일을 선택 후 파일 열기 버튼
        self.Open_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Open_btn.setGeometry(QtCore.QRect(420, 400, 121, 41))
        self.Open_btn.setObjectName("Open_btn")
        if self.Open_btn.click():
            f = open("", "r")
            fileinfo = f.read()
            f.close()
            print(fileinfo)

        ## 모든 원인 체크가 끝나면 전체 저장
        self.Save_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Save_btn.setGeometry(QtCore.QRect(880, 712, 121, 41))
        self.Save_btn.setObjectName("Save_btn")
        ## checkbox -> 원인 선택지
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
        ## 파일 목록
        self.listWidget = QtWidgets.QListWidget(DataVisualization_prototype)
        self.listWidget.setGeometry(QtCore.QRect(600, 90, 401, 251))
        self.listWidget.setObjectName("listWidget")

        # files = read_all_files_in_dir.read_all_files()
        #
        # view = QListView(self)
        # model = QStandardItemModel()
        # for f in files:
        #     model.appendRow(QStandardItem(f))
        # view.setModel(model)

        ## 그래프 시각화
        self.Graphs = QtWidgets.QLabel(DataVisualization_prototype)
        self.Graphs.setGeometry(QtCore.QRect(20, 50, 521, 291))
        self.Graphs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Graphs.setObjectName("Graphs")
        # ## 파일 목록 삭제 버튼
        #         # self.pushButton = QtWidgets.QPushButton(DataVisualization_prototype)
        #         # self.pushButton.setGeometry(QtCore.QRect(880, 20, 121, 41))
        #         # self.pushButton.setObjectName("FileListDelete_btn")
        ## 원인 선택 후 결과 저장 버튼
        self.pushButton_2 = QtWidgets.QPushButton(DataVisualization_prototype)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 640, 121, 41))
        self.pushButton_2.setObjectName("ResultSave_btn")
        # ResultSave 버튼 클릭 시, "w"를 이용하여 파일 내용 뒤에 원인을 append 시키고 파일명을 원래파일명+_result.dat로 저장
        ## Open할 파일을 찾아볼 수 있게 만든 버튼
        self.Search_btn = QtWidgets.QPushButton(DataVisualization_prototype)
        self.Search_btn.setGeometry(QtCore.QRect(560, 400, 121, 41))
        self.Search_btn.setObjectName("Search_btn")
        if self.Search_btn.mousePressEvent():
            for root, dirs, files in os.walk("C:/Users/Haesung_public05/Desktop/UA3PData/UA3P-1/Haesung/"):
                for fname in files:
                    full_fname = os.path.join(root, fname)

                    print(full_fname)


        self.retranslateUi(DataVisualization_prototype)
        QtCore.QMetaObject.connectSlotsByName(DataVisualization_prototype)

    def retranslateUi(self, DataVisualization_prototype):
        _translate = QtCore.QCoreApplication.translate
        DataVisualization_prototype.setWindowTitle(_translate("DataVisualization_prototype", "DataVisualization_prototype"))
        self.Open_btn.setText(_translate("DataVisualization_prototype", "Open"))
        self.Save_btn.setText(_translate("DataVisualization_prototype", "FileSave"))
        self.checkBox.setText(_translate("DataVisualization_prototype", "원인1"))
        self.checkBox_2.setText(_translate("DataVisualization_prototype", "원인2"))
        self.checkBox_3.setText(_translate("DataVisualization_prototype", "원인3"))
        self.checkBox_4.setText(_translate("DataVisualization_prototype", "원인4"))
        self.checkBox_5.setText(_translate("DataVisualization_prototype", "원인5"))
        self.checkBox_6.setText(_translate("DataVisualization_prototype", "원인6"))
        self.Graphs.setText(_translate("DataVisualization_prototype", "그래프 표시"))
        #self.pushButton.setText(_translate("DataVisualization_prototype", "Delete"))
        self.pushButton_2.setText(_translate("DataVisualization_prototype", "ResultSave"))
        self.Search_btn.setText(_translate("DataVisualization_prototype", "Search"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataVisualization_prototype = QtWidgets.QDialog()
    ui = Ui_DataVisualization_prototype()
    ui.setupUi(DataVisualization_prototype)
    DataVisualization_prototype.show()
    sys.exit(app.exec_())
