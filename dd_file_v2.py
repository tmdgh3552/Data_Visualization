import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from numpy import unicode
import pandas as pd
import numpy as np
import os


class testDialog(QDialog):
    i = 0

    def __init__(self, parent=None):
        super(testDialog, self).__init__(parent)

        form = QGridLayout()
        form.setHorizontalSpacing(0)
        self.setMinimumSize(800, 600)
        # self.setMaximumSize(1024,768)
        testDialog.resize(self, 1024, 768)
        testDialog.setObjectName(self, "check_program")

        self.myedit = QLineEdit()
        self.myedit.setDragEnabled(True)
        self.myedit.setAcceptDrops(True)
        self.myedit.setMinimumHeight(100)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.myedit.setFont(font)

        self.myedit.installEventFilter(self)

        form.addWidget(self.myedit)

        self.setLayout(form)
        self.setGeometry(600, 90, 401, 251)
        self.setWindowTitle('drop test')

        self.myedit.setText("drop data file")

        self.myedit.textChanged.connect(self.editchange)  # new style signal slot connections
        self.list = QtWidgets.QListWidget(self)
        self.list.setGeometry(QtCore.QRect(300, 500, 0, 0))
        self.list.setEditTriggers(QtWidgets.QListWidget.NoEditTriggers)
        self.list.setAutoScroll(True)
        form.addWidget(self.list)
        self.table = QtWidgets.QTableWidget(1, 7, self)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.setGeometry(QtCore.QRect(300, 610, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.setObjectName("불량률 계산")
        self.table.setHorizontalHeaderLabels(
            [" Pallet No. ", "0.0F 불량률", "0.3F 불량률", "0.5F 불량률", "0.7F 불량률", "0.9F 불량률", " 수율 "])

        form.addWidget(self.table)
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(300, 800, 0, 0))
        form.addWidget(self.label)

    def setTableWidgetData(self, fy_and_allpathrate_list):

        self.table.setItem(testDialog.i, 0, QTableWidgetItem(fy_and_allpathrate_list[6]))
        self.table.setItem(testDialog.i, 1, QTableWidgetItem(fy_and_allpathrate_list[0] + " %"))
        self.table.setItem(testDialog.i, 2, QTableWidgetItem(fy_and_allpathrate_list[1] + " %"))
        self.table.setItem(testDialog.i, 3, QTableWidgetItem(fy_and_allpathrate_list[2] + " %"))
        self.table.setItem(testDialog.i, 4, QTableWidgetItem(fy_and_allpathrate_list[3] + " %"))
        self.table.setItem(testDialog.i, 5, QTableWidgetItem(fy_and_allpathrate_list[4] + " %"))
        self.table.setItem(testDialog.i, 6, QTableWidgetItem(fy_and_allpathrate_list[5] + " %"))
        self.table.insertRow(testDialog.i + 1)
        testDialog.i = testDialog.i + 1
        print(testDialog.i)

    avg0 = 0.0
    avg3 = 0.0
    avg5 = 0.0
    avg7 = 0.0
    avg9 = 0.0
    avg_allpass = 0.0

    def calculateTable(self, fy_and_allpathrate_list):

        testDialog.avg0 += float(fy_and_allpathrate_list[0])
        testDialog.avg3 += float(fy_and_allpathrate_list[1])
        testDialog.avg5 += float(fy_and_allpathrate_list[2])
        testDialog.avg7 += float(fy_and_allpathrate_list[3])
        testDialog.avg9 += float(fy_and_allpathrate_list[4])
        testDialog.avg_allpass += float(fy_and_allpathrate_list[5])
        # print(testDialog.avg0)
        # print(testDialog.avg3)
        # print(testDialog.avg5)
        # print(testDialog.avg7)
        # print(testDialog.avg9)
        # print(testDialog.avg_allpass)

    @QtCore.pyqtSlot(str)  # int represent the column value
    def mouseclicked(self):
        return self.myedit.clear()

    def editchange(self, data):
        print("editchange: %s", unicode(data))
        # self.table.clear()
        return unicode(data)

    def fycal(self, filepath, file_name):
        file_dat = pd.read_csv(filepath, sep='\s{}', engine='python')  ## dd_file_v2 에서 경로 값을 받아와 실행시켜야 함.

        file_dat.columns = ['data']

        # %%

        meas = (file_dat[file_dat['data'].str.match('\[Measurement ')])
        meas = meas.reset_index()
        meas.columns = ['num', 'data']

        # %%

        AF = file_dat.iloc[8:9, :]
        AF = AF['data'].str.split('=', expand=True).loc[:, 1:]
        AF[1] = pd.to_numeric(AF[1])
        AF = AF.values[0]
        af = np.int16(AF[0] / 35).item()
        # AF 값 가져오기(위치 계산 때문에)

        # %%

        row_len = len(meas)

        # %%

        dataset = pd.DataFrame(index=range(row_len),
                               columns=['S1', 'T1', 'S2', 'T2', 'S3', 'T3', 'S4', 'T4', 'S5', 'T5', 'S6', 'T6',
                                        'S7', 'T7',
                                        'S8', 'T8', 'S9', 'T9', 'S10', 'T10', 'S11', 'T11', 'S12', 'T12', 'S13',
                                        'T13', 'S14',
                                        'T14', 'S15', 'T15', 'S16', 'T16', 'S17', 'T17'])

        # %%

        first = 0
        last = 1
        dtspl = []
        dtspl = pd.DataFrame(dtspl)

        for c in range(row_len):
            f = meas.num[first]
            l = meas.num[last]
            split_data = file_dat.iloc[f:l]
            # spl_data

            lastm = len(split_data)  # T17부터 S1까지 추출 위한 마지막 위치 구하기
            mtf = split_data[lastm - 34:lastm]
            mtf = mtf['data'].str.split(' ', expand=True)
            mtf = mtf.reset_index()
            del mtf['index']

            m = 0
            mtf = mtf.iloc[m:m + 34, af + 2:af + 3].values
            x = 0
            y = 1
            for n in mtf:
                dataset.iloc[c:c + 1, x:y] = n
                x += 1
                y += 1

            first += 1
            last += 1

            if first == len(meas) - 1:
                break

        split_data = file_dat.iloc[f:]

        lastm = len(split_data)  # T17부터 S1까지 추출 위한 마지막 위치 구하기
        mtf = split_data[lastm - 34:]
        mtf = mtf['data'].str.split(' ', expand=True)
        mtf = mtf.reset_index()
        del mtf['index']

        m = 0
        mtf = mtf.iloc[m:m + 34, af + 1:af + 2].values

        x = 0
        y = 1
        c += 1
        for n in mtf:
            dataset.iloc[c:c + 1, x:y] = n
            x += 1
            y += 1

        last += 1

        # %%

        print(dataset)

        # %%

        count = 0
        # 0.0F 불량률
        c_rate = 0
        for i in range(row_len):
            for j in range(1):

                if float(dataset.iloc[i, j]) > 73.0:
                    pass
                else:
                    count += 1
            if i % 3 == 2 and count > 0:  # 3번의 측정 중에서 한 번이라도 fail이 있으면 c_rate + 1
                c_rate += 1
                count = 0
        cnt_0stF = round(c_rate / (row_len / 3) * 100, 2)
        cnt_0F = str(cnt_0stF)
        print("0.0F 불량률: " + cnt_0F + " %")

        # 0.3F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(row_len):
            for j in range(18, 24, 2):

                if float(dataset.iloc[i, j]) > 62.0:
                    pass
                else:
                    counts += 1

            for j in range(19, 25, 2):

                if float(dataset.iloc[i, j]) > 50.0:
                    pass
                else:
                    countt += 1
            if i % 3 == 2 and countt + counts > 0:  # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        cnt_3tF = round(c_ratet / (row_len / 3) * 100, 2)
        cnt_3F = str(cnt_3tF)
        print("0.3F 불량률: " + cnt_3F + " %")

        # 0.5F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(row_len):
            for j in range(26, 32, 2):

                if float(dataset.iloc[i, j]) > 55.0:
                    pass
                else:
                    counts += 1

            for j in range(27, 33, 2):

                if float(dataset.iloc[i, j]) > 52.0:
                    pass
                else:
                    countt += 1
            if i % 3 == 2 and countt + counts > 0:  # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        cnt_5tF = round(c_ratet / (row_len / 3) * 100, 2)
        cnt_5F = str(cnt_5tF)
        print("0.5F 불량률: " + cnt_5F + " %")

        # 0.7F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(row_len):
            for j in range(2, 8, 2):

                if float(dataset.iloc[i, j]) > 55.0:
                    pass
                else:
                    counts += 1

            for j in range(3, 9, 2):

                if float(dataset.iloc[i, j]) > 40.0:
                    pass
                else:
                    countt += 1
            if i % 3 == 2 and countt + counts > 0:  # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        cnt_7tF = round(c_ratet / (row_len / 3) * 100, 2)
        cnt_7F = str(cnt_7tF)
        print("0.7F 불량률: " + cnt_7F + " %")

        # 0.9F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(row_len):
            for j in range(10, 16, 2):

                if float(dataset.iloc[i, j]) > 36.0:
                    pass
                else:
                    counts += 1

            for j in range(11, 17, 2):

                if float(dataset.iloc[i, j]) > 25.0:
                    pass
                else:
                    countt += 1
            if i % 3 == 2 and countt + counts > 0:  # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        # cnt_9sF = c_rates / 64 * 100
        cnt_9tF = round(c_ratet / (row_len / 3) * 100, 2)
        cnt_9F = str(cnt_9tF)
        print("0.9F 불량률: " + cnt_9F + " %")

        f = open(filepath, "r")
        # print("여기")
        fdat = f.read()

        fdat_spl = fdat.split("\n")
        j = 1
        count_allpass = 0
        count_pass = 0  # 3번의 측정값을 구하기 위한 변수 설정
        fdat_2spl = []
        fdat_list = []
        fp_sum = []
        for i in range(len(fdat_spl)):
            start_info = fdat_spl[i].find(
                "Time")  ## \n으로 split해서 result앞의 \n은 검색에 들어가지 않음......처리 방법 필요. -> Time을 중심으로 잘라서 사용. 해결.
            if start_info == 0:  # find 성공, 반환=0 // find 실패, 반환=-1
                fdat_2spl = fdat_spl[i:i + 2]
                fp = fdat_2spl[1].split(" ")[1]

                fp_sum.append(fp)

        for j in range(row_len):

            if fp_sum[j] == "FAIL":
                pass
            elif fp_sum[j] == "PASS":
                count_pass += 1

                if j % 3 == 2 and count_pass == 3 and count_pass != 0:
                    count_allpass += 1
                    count_pass = 0

                elif j % 3 == 2 and count_pass != 3:

                    count_pass = 0
                else:
                    pass
            else:

                pass

        allpathrate = str(round(count_allpass / (row_len / 3) * 100, 2))

        print("수율: " + allpathrate + " %")
        print("파일경로:" + filepath)
        print(file_name)
        fy_and_allpathrate_list = [cnt_0F, cnt_3F, cnt_5F, cnt_7F, cnt_9F, allpathrate, file_name]
        filepath = filepath.replace(".dat", ".fld")
        print(filepath)
        if os.path.isfile(filepath):
            pass
        else:
            f = open(filepath, "w+")
            f.write(str(fy_and_allpathrate_list))
            f.close()
        return fy_and_allpathrate_list
        ## n개 measurement 값에 대한 3번의 측정 결과 비교 해야 함.

    def eventFilter(self, object, event):

        if (object is self.myedit):
            if (event.type() == QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()  # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    print("accept")
                else:
                    event.ignore()
                    print("ignore")
            if (event.type() == QtCore.QEvent.Drop):

                if event.mimeData().hasUrls():  # if file or link is dropped
                    urlcount = len(event.mimeData().urls())  # count number of drops
                    url = event.mimeData().urls()[0]  # get first url
                    object.setText(unicode(url.toLocalFile()))  # assign first url to editline
                    event.accept()  # doesnt appear to be needed
                    filepath = unicode(url.toLocalFile())
                    print("dd파일 경로:" + filepath)
                    total_filepath = testDialog.folderopen(self, filepath)
                    for file_lp in range(len(total_filepath[0])):
                        print(total_filepath[0][file_lp])
                        # print(total_filepath[file_lp])
                        fld_path = total_filepath[0][file_lp].replace(".dat", ".fld")
                        if os.path.isfile(fld_path):  # fld 파일 있는지 유무 검사
                            # FLD 파일 읽어와야함
                            # print(fld_path)
                            f = open(fld_path, "r")
                            fld_content = f.read()  # setTableWidgetData 함수 부름 인수 : 리스트 전달
                            fld_content_strip = fld_content.strip("[]")
                            fld_content_strip = fld_content_strip.replace("'", "")
                            fld_content_strip = fld_content_strip.split(",")
                            print(type(fld_content_strip))

                            # b = []
                            # for a in fld_content:
                            #     b.append(a)
                            # print(b)
                            self.setTableWidgetData(fld_content_strip)  # fld 내용 리스트로 전달
                            self.calculateTable(fld_content_strip)
                        else:
                            self.setTableWidgetData(
                                testDialog.fycal(self, total_filepath[0][file_lp], total_filepath[1][file_lp]))
                            self.calculateTable(
                                testDialog.fycal(self, total_filepath[0][file_lp], total_filepath[1][file_lp]))
                        self.list.addItem(total_filepath[0][file_lp])
                    self.label.setText(
                        "합계: \t\t" + "0.0F 평균" + "\t\t" + "0.3F 평균" + "\t\t" + "0.5F 평균" + "\t\t" + "0.7F 평균" + "\t\t" + "0.9F 평균" + "\t\t" + "수율 평균"
                        + "\n" + "\t\t" + str(round(testDialog.avg0 / testDialog.i, 2)) + "\t\t" + str(
                            round(testDialog.avg3 / testDialog.i, 2))
                        + "\t\t" + str(round(testDialog.avg5 / testDialog.i, 2)) + "\t\t" + str(
                            round(testDialog.avg7 / testDialog.i, 2))
                        + "\t\t" + str(round(testDialog.avg9 / testDialog.i, 2)) + "\t\t" + str(
                            round(testDialog.avg_allpass / testDialog.i, 2)))

            return False  # lets the event continue to the edit
        return False

    def folderopen(self, filepath):
        full_fname = []
        file_name_list = []
        full_path_name = []
        for root, dirs, files in os.walk(filepath):
            for fname in files:

                if fname.endswith(".dat") == True:
                    full_fname.append(os.path.join(root, fname))
                    file_name_list.append(fname)

        full_path_name.insert(0, full_fname)
        full_path_name.insert(1, file_name_list)
        print(full_path_name)
        return full_path_name  ## 이렇게 재정의 해서 처리해도 되는 건가..


if __name__ == "__main__":
    app = QApplication([])
    dl = testDialog()
    dl.exec_()
    sys.exit(app.closeAllWindows())
