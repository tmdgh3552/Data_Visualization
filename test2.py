# %%
import pandas as pd
from pandas import DataFrame
import numpy as np
from PyQt5.QtWidgets import *
from UI_Creating.dd_file_v2 import filepath
# from UI_Creating.dd_file_v2 import *

filepath_test = filepath

# %%
#print("test2:" + filepath_test)
#print("Ddddddddd")
def eventFilter(self, object, event):

def fycal():
    if filepath_test != "":
        fdat = pd.read_csv(filepath_test, sep='\s{}', engine='python') ## dd_file_v2 에서 경로 값을 받아와 실행시켜야 함.

        fdat.columns = ['data']

        # %%

        meas = (fdat[fdat['data'].str.match('\[Measurement ')])
        meas = meas.reset_index()
        meas.columns = ['num', 'data']

        # %%

        AF = fdat.iloc[8:9, :]
        AF = AF['data'].str.split('=', expand=True).loc[:, 1:]
        AF[1] = pd.to_numeric(AF[1])
        AF = AF.values[0]
        af = np.int16(AF[0] / 35).item()
        # AF 값 가져오기(위치 계산 때문에)


        # %%

        row_len = len(meas)

        # %%

        dataset = pd.DataFrame(index=range(row_len),
                               columns=['S1', 'T1', 'S2', 'T2', 'S3', 'T3', 'S4', 'T4', 'S5', 'T5', 'S6', 'T6', 'S7', 'T7',
                                        'S8', 'T8', 'S9', 'T9', 'S10', 'T10', 'S11', 'T11', 'S12', 'T12', 'S13', 'T13', 'S14',
                                        'T14', 'S15', 'T15', 'S16', 'T16', 'S17', 'T17'])

        # %%

        first = 0
        last = 1
        dtspl = []
        dtspl = pd.DataFrame(dtspl)

        for c in range(row_len):
            f = meas.num[first]
            l = meas.num[last]
            spl_data = fdat.iloc[f:l]
            spl_data

            lastm = len(spl_data)  # T17부터 S1까지 추출 위한 마지막 위치 구하기
            mtf = spl_data[lastm - 34:lastm]
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

        spl_data = fdat.iloc[f:]

        lastm = len(spl_data)  # T17부터 S1까지 추출 위한 마지막 위치 구하기
        mtf = spl_data[lastm - 34:]
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
        for i in range(192):
            for j in range(1):

                if float(dataset.iloc[i, j]) > 73.0:
                    pass
                else:
                    count += 1
            if i % 3 == 2 and count > 0: # 3번의 측정 중에서 한 번이라도 fail이 있으면 c_rate + 1
                c_rate += 1
                count = 0
        cnt_0stF = c_rate / 64 * 100
        cnt_0F = str(cnt_0stF)
        print("0.0F 불량률: " + cnt_0F + " %")

        # 0.3F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(192):
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
            if i % 3 == 2 and countt+counts > 0: # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass
        ###### 둘 중에 하나가 fail이라면 상관 없지만 둘 다 fail일 경우에 count값이 둘다 증가하는 경우가 발생. -> 처리 방법 필요. ######

        cnt_3tF = c_ratet / 64 *100
        cnt_3F = str(cnt_3tF)  # 같은 192개 기준이므로 % 평균
        print("0.3F 불량률: " + cnt_3F + " %")

        # 0.5F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(192):
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
            if i % 3 == 2 and countt+counts > 0: # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        cnt_5tF = c_ratet / 64 *100
        cnt_5F = str(cnt_5tF)  # 같은 192개 기준이므로 % 평균
        print("0.5F 불량률: " + cnt_5F + " %")

        # 0.7F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(192):
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
            if i % 3 == 2 and countt+counts > 0: # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        cnt_7tF = c_ratet / 64 *100
        cnt_7F = str(cnt_7tF)  # 같은 192개 기준이므로 % 평균
        print("0.7F 불량률: " + cnt_7F + " %")

        # 0.9F 불량률
        counts = 0
        countt = 0
        c_rates = 0
        c_ratet = 0
        for i in range(192):
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
            if i % 3 == 2 and countt+counts > 0: # 하나라도 fail이 뜬다면 카운트가 1이상, 올패스는 0
                c_ratet += 1
                counts = 0
                countt = 0
            else:
                pass

        # cnt_9sF = c_rates / 64 * 100
        cnt_9tF = c_ratet / 64 * 100
        cnt_9F = str(cnt_9tF)  # 같은 192개 기준이므로 % 평균
        print("0.9F 불량률: " + cnt_9F + " %")

        f = open(filepath_test,"r")
        fdat = f.read()

        fdat_spl = fdat.split("\n")
        j = 1
        count_h = 0
        count_i = 0 # 3번의 측정값을 구하기 위한 변수 설정
        fdat_2spl = []
        fdat_list = []
        for i in range(len(fdat_spl)):
            start_info = fdat_spl[i].find("Time") ## \n으로 split해서 result앞의 \n은 검색에 들어가지 않음......처리 방법 필요. -> Time을 중심으로 잘라서 사용. 해결.
            if start_info == 0: # find 성공, 반환=0 // find 실패, 반환=-1
               fdat_2spl = fdat_spl[i:i+2]
               print(fdat_2spl)
               fp= fdat_2spl[1].split(" ")[1]
               print(fp)
               if fp == "FAIL":
                   pass
               elif fp == "PASS":
                   count_i += 1

               else:
                   print("에러 measurement %s / 192", str(i+1))

               if i%3 == 2 and count_i == 3:
                   count_h += 1
                   count_i = 0
               elif i%3 == 2 and count_i != 3:
                   count_i = 0
               else:
                   pass
        allpathrate = count_h / 64 * 100

        print("수율: "+str(allpathrate)+" %")
        print("파일경로:" + filepath_test)
        a = [cnt_0F, cnt_3F, cnt_5F, cnt_7F, cnt_9F, allpathrate]
        return a
        ## 64개 measurement 값에 대한 3번의 측정 결과 비교 해야 함.
