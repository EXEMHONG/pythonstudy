# 무한반복 
#   : 무조건 계속 반복하는 반복문
#     반드시, 종료조건을 넣어주어야 한다.

# break
# : 가장 가까운 반복문을 벗어나는 키워드

while True:
    name = input('윤정현 씝병신인가요?')
    # 종료조건
    if name ==  '맞습니다' or name == '씝맞습니다':
        print('정답입니다')
        break
    else: 
        print('틀렸습니다.')
        
        