import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from numpy import integer

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
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

            mydict = {"S": odd, "T": even}
            display(pd.DataFrame(mydict))

            plt.axis([0,100,0,100])
            plt.axis(option='equal')
            plt.xlim(0,100)
            plt.ylim(0,100)
            plt.xscale('linear')
            plt.yscale('linear')
            #plt.plot(odd,even)
            x = np.arange(0,100,100)
            y = np.arange(0,100,100)
            plt.plot(odd, 'r--', marker='o')
            plt.plot(even, 'b', marker='x')
            x+=1





            #even = np.arange(50, 100, 20)


            plt.show()