import pandas as pd
from pandas import DataFrame
import numpy as np

f = open("datfile_new.dat","r")
fdat = f.read()

fdat_spl = fdat.split("\n")
j = 1
count = 0
fdat_2spl = []
fdat_list = []
for i in range(len(fdat_spl)):
    start_info = fdat_spl[i].find("S1 ")
    if start_info == 0: # find 성공, 반환=0 // find 실패, 반환=-1
        print(str(j)+".")
        print(fdat_spl[i:i+34])
        count += 1
        fdat_2spl = fdat_spl[i:i+34]
        print(fdat_2spl)
        if count%3 == 0:
           j+=1
        for x in range(len(fdat_2spl)):
            fdat = fdat_2spl[x].split(" ")
            # print(fdat[1])
            print(fdat[1])
            fdat_list.append(fdat[1])
        obj = pd.Series(fdat_list)
        print(obj)

        # n = 34
        # result = [fdat_list[i * n:(i + 1) * n] for i in range((len(fdat_list) + n - 1) // n )]
        # # print(result)
        # fdat_dat = []
        # for c in range(0,34):
        #     fdat_dat.append(fdat_list[0:6528:192])
        # print("measurements: ", fdat_dat)
        # print(len(fdat_dat))
        # obj = pd.Series(fdat_dat)
        # print(obj)

#print(fdat_list)
        # fdat_3spl = fdat_2spl[i].split(" ")
        # print(fdat_3spl[1])
            # fdat_2spl = fdat_spl[2:][i].split(" ")
            # print(fdat_2spl)
            # print(fdat_2spl[1]) # S1의 첫번째 값

            # print(fdat_2spl[i])
            #print(len(fdat_list))

          #print(start_info)

#print(fdat_list[0:34])

