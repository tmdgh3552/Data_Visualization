import os

# 가져올 파일들이 있는 directory path
path_dir = 'C:/Users/Haesung_public05/Desktop/test files/DATA SX NGÀY 14.01/DATA SX NG픜 14.01/TH01/'

file_list = os.listdir(path_dir)        # path 에 존재하는 파일 목록 가져오기

file_list.sort()                        # 파일 이름 순서대로 정렬


"""
    파일 이름에서 특정 부분 가져오기 예시
"""
# 'model.ckpt-3000' 와 같은 이름을 가진 파일에서 특정 정보를 가져오고 싶다먄
# ckpt.model_checkpoint_path 가 'model.ckpt-3000' 의 값을 가지고 있을 경우
#step = int(ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1])
# setp = 3000 이라는 int 값을 가지게 된다.


"""
    파일 이름에 특정 string 을 가지는 파일만 뽑아내기
"""
for item in file_list:
    # some_string 이 파일 이름에 없을 경우 -1 을 반환
    if item.find(' .dat') ==0:
        print(item)                  # some_string 을 파일이름에 포함하는 파일만 출력
##