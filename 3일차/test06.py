# 중첩 반복문
# : 반복문 안에 또 하나의 반복문을 작성

# 구구단 전체 출력
# 2~9단이 있고
# 1~9 까지 곱함

for i in range (2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))
    print()