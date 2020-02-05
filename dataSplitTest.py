import string
import re

f = open("C:/Users/Haesung_public05/Desktop/test1.dat","r")
tdat = f.read()

#print(tdat)
mc ={}
# tdat_1spl = tdat.split("\n")
#print(tdat_1spl)
# regex = re.compile("^S1|^T1|^S2|^T2|^S3|^T3|^S4|^T4|^S5|^T5|^S6|^T6|^S7|^T7|^S8|^T8|^S9|^T9")
#  # "|^S10|^T10|^S11|^T11|^S12|^T12|^S13|^T13|^S14|^T14|^S15|^T15|^S16"
#  #                   "|^T16|^S17|^T17")
#  ## S10 T10 부터는 S1 T1이 처리해줌.
lines= []
lines = tdat.split("\n")
## T17까지 한 번 돌면 2.을 format해야 함.
##
line_num = 1
line_count = 1
for each_line in lines:
    #print(each_line)
    if each_line.find('S1') > -1:
        if len(each_line) >= 24 and len(each_line)< 26:
            # print(each_line, len(each_line))
            rs= str(line_num) + " "+ each_line
            print(rs)
            line_count +=1
            if line_count >= 9 and line_count % 9 ==1:
                line_num += 1
    # elif each_line.find("T1") > -1:
    #     print(each_line, len(each_line))
    # elif each_line.find("S2") > -1:
    #     print(each_line, len(each_line))
    # elif each_line.find("T2") > -1:
    #     print(each_line, len(each_line))
    else:
        pass


f.close()
#
# for each_line in tdat:
#     tdat_1spl = tdat.split("\n")
#     if each_line.find("S1") > 0:
#         print(each_line)
#     else:
#         pass
# p = re.compile('[A-Z][0-9]+')
# m = p.match("S1")
# print(m)
# regex = re.compile("^Range of Valid EFL")
# for i in range(len(tdat_1spl)):
#     mc = regex.findall(tdat_1spl[i])
#
#     if not mc:
#          mc.pop()
#     print(mc)
# print(tdat_1spl)
# print(len(tdat_1spl))
# search = "S"
# i=0
# split_list= []
# for s in tdat_1spl:
#     if "S" in s:
#         split_list.append(s)
# print(split_list)

# result = {}
# result[0] = tdat_1spl[191:225]
# print(result[0])
# result[1] = tdat_1spl[348:382]
# print(result[1])
# j = 0
# for i in range(2,9):
#
#     result[i] = tdat_1spl[505+(156*j):539+(156*j)]
#     j+=1
#
#     print(result[i])
#
# result[10] = tdat_1spl[507+(156*8):541+(156*8)]
# print(result[10])
#
# result[11] = tdat_1spl[508+(156*9):542+(156*9)]
# print(result[11])
#
# result[12] = tdat_1spl[509+(156*10):543+(156*10)]
# print(result[12])
#
# result[13] = tdat_1spl[510+(156*11):544+(156*11)]
# print(result[13])
#
# result[14] = tdat_1spl[511+(156*12):545+(156*12)]
# print(result[14])
#
# j=1
# k=13
# for i in range(15,36):
#     result[i] = tdat_1spl[511+j+(156*k):545+j+(156*k)]
#     k+=1
#     j+=1
#     print(result[i])
#
# j=1
# k=35
# for i in range(37,99):
#     result[i] = tdat_1spl[511 + j + (156 * k):545 - j + (156 * k)]
#     k+=1
#     j+=1
#     print(result[i])
#
# # j=1
# # k=35
# # for i in range(38,50):
# #     result[i] = tdat_1spl[511 + j + (156 * k):545 - j + (156 * k)]
# #     k+=1
# #     j+=1
# #     print(result[i])