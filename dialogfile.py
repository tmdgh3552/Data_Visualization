# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogUpload.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter.filedialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 117)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label.setObjectName("label")
        self.btn_file = QtWidgets.QPushButton(Dialog)
        self.btn_file.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.btn_file.setObjectName("btn_file")

        # self.btn_file.clicked.connect(self.fileSearch)

        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(150, 90, 81, 23))
        self.btn_close.setObjectName("btn_close")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_file_upload = QtWidgets.QPushButton(Dialog)
        self.btn_file_upload.setGeometry(QtCore.QRect(240, 90, 81, 23))
        self.btn_file_upload.setObjectName("btn_file_upload")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def fileSearch(self):
    #     #
    #     #     file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Choose a file')
    #     #     if file != None:
    #     #         data = file.read()
    #     #     file.close()
    #     #     #return data
    #     #     print(data)


        # fileName = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)")
        # if fileName:
        #     print(fileName)
        # buttonReply = QMessageBox.question(self, "Message Box", "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No,
        #                                    QMessageBox.No)
        # if buttonReply == QMessageBox.Yes:
        #     print("Yes clicked.")
        # else:
        #     print("No clicked.")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "업로드 할 파일을 선택하세요."))
        self.btn_file.setText(_translate("Dialog", "파일 찾기"))
        self.btn_close.setText(_translate("Dialog", "취소"))
        self.btn_file_upload.setText(_translate("Dialog", "등록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
