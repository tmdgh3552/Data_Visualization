# %%


# %%

import pandas as pd
from pandas import DataFrame
import numpy as np

# %%

fdat = pd.read_csv("datfile_new.dat", sep='\s{}', engine='python')
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
f = meas.num[first]
c = 0
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
for n in range(192):
    cm1 = dataset.iloc[:n, 0:2]
# cm1
# 0.0F 불량률
for j in range(1):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 73.0:
            pass
        else:
            count += 1
cnt_0F = str(count / 192 * 100)
print("0.0F 불량률: " + cnt_0F + " %")

# 0.3F 불량률
counts = 0
countt = 0
for j in range(18, 24, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 62.0:
            pass
        else:
            counts += 1
for j in range(19, 25, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 50.0:
            pass
        else:
            countt += 1
cnt_3sF = counts / 192 * 100
cnt_3tF = countt / 192 * 100
cnt_3F = str((cnt_3sF + cnt_3tF) / 2)  # 같은 192개 기준이므로 % 평균
print("0.3F 불량률: " + cnt_3F + " %")

# 0.5F 불량률
counts = 0
countt = 0
for j in range(26, 32, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 55.0:
            pass
        else:
            counts += 1
for j in range(27, 33, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 42.0:
            pass
        else:
            countt += 1
cnt_5sF = counts / 192 * 100
cnt_5tF = countt / 192 * 100
cnt_5F = str((cnt_5sF + cnt_5tF) / 2)  # 같은 192개 기준이므로 % 평균
print("0.5F 불량률: " + cnt_5F + " %")

# 0.7F 불량률
counts = 0
countt = 0
for j in range(2, 8, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 55.0:
            pass
        else:
            counts += 1
for j in range(3, 9, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 40.0:
            pass
        else:
            countt += 1
cnt_7sF = counts / 192 * 100
cnt_7tF = countt / 192 * 100
cnt_7F = str((cnt_7sF + cnt_7tF) / 2)  # 같은 192개 기준이므로 % 평균
print("0.7F 불량률: " + cnt_7F + " %")

# 0.9F 불량률
counts = 0
countt = 0
for j in range(10, 16, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 36.0:
            pass
        else:
            counts += 1
for j in range(11, 17, 2):
    for i in range(192):
        if float(dataset.iloc[i, j]) > 25.0:
            pass
        else:
            countt += 1
cnt_9sF = counts / 192 * 100
cnt_9tF = countt / 192 * 100
cnt_9F = str((cnt_9sF + cnt_9tF) / 2)  # 같은 192개 기준이므로 % 평균
print(countt)
print("0.9F 불량률: " + cnt_9F + " %")




