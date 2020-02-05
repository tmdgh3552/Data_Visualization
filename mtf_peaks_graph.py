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
        print("홀수 리스트: ",odd)
        print("짝수 리스트: ",even)
        if count%3 == 0:
            j+=1




