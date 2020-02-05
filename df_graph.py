import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

f = open("datfile_sample","r")
dat_file = f.read()

fdat_spl = dat_file.split("\n")
j = 1
count = 0
odd = []
even = []
for i in range(len(fdat_spl)):
    start_info = fdat_spl[i].find("MTF Peaks")
    if start_info == 0:
        print(str(j)+".")
        print(fdat_spl[i])
        count += 1

        fdat_2spl = fdat_spl[i].split(" ")
        print(fdat_2spl)
        print(fdat_2spl[2:])
        #print(fdat_2spl[2:][0]) // list의 첫번째 인수 모두 추출
        for x in range(0,len(fdat_2spl[2:][0])):
            odd = fdat_2spl[2:][0::2]
            even = fdat_2spl[2:][1::2]
            # if float(fdat_2spl[2:][x])%2 !=0:
            #     odd.append(fdat_2spl[2:][x])
            # else:
            #     even.append(fdat_2spl[2:][x])
            ## 짝수, 홀수 값이 아니라 짝수, 홀수 자리 데이터..
        print("홀수 리스트: ",odd) # odd = S
        print("짝수 리스트: ",even) # even = T
        if count%3 == 0:
            j+=1


            plt.rcParams['figure.figsize'] = [12, 8]

            np.random.seed(123)  # for reproducibility

            index = pd.date_range("1 1 2010", periods=100, freq="m", name="Date")

            data = np.random.randn(100, 34).cumsum(axis=0)

            wide_df = pd.DataFrame(data, index,
                                   ['S1', 'T1', 'S2', 'T2', 'S3', 'T3', 'S4', 'T4', 'S5', 'T5', 'S6', 'T6', 'S7', 'T7',
                                    'S8', 'T8', 'S9', 'T9', 'S10', 'T10', 'S11', 'T11', 'S12', 'T12', 'S13', 'T13',
                                    'S14', 'T14', 'S15', 'T15', 'S16', 'T16', 'S17', 'T17'])

            wide_df.shape(100, 34)

            wide_df.head()
