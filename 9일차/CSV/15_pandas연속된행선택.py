import pandas as pd
import sys

path = 'D:/python/pythonstudy/9일차/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file, header=None)

#drop()
# : 데이터프레임의 특정 행을 삭제하는 함수
data_frame = data_frame.drop([0,1,2,16,17,18])

# iloc[0]
# : index를 기준으로 특정 행,열을 선택하는 함수
data_frame.columns = data_frame.iloc[0]

# reindex()
# : 데이터프레임에서 행을 재구성하는 함수

# data_frame.reindex(data_frame.index,drop(3))
# - 인덱스 3인 행을 삭제 후, 삭제된 새로운 데이터프레임을 재구성하여 반환


new_index = range( len(data_frame))
data_frame = data_frame.reindex(new_index)

print('reindex() : 인덱스 재구성 후')
print(data_frame)
data_frame.to_csv(output_file, index=False)