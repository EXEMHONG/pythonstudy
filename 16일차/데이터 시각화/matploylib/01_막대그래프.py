# 막대 그래프
import matplotlib.pyplot as plt
# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 데이터
names = ['apple', 'grape', 'strawberry']
values = [50, 120, 70]
colors = ['red', 'blue', 'green']

# 막대그래프 설정
# plt.bar (x축 데이타, y축 데이터 )
plt.bar(names, values, align='center', color=colors )

# 제목 및 라벨
plt.title('과일 판매량')
plt.xlabel('과일')
plt.ylabel('판매량')

# y축 최소값, 최대값 지정
#plt.ylim(0, 200)
# 0~200 까지 10 단위를 눈금 지정
plt.yticks( range(0, 200, 50))


# 그래프 이미지 저장
plt.savefig('막대그래프.png', dpi=400, bbox_inches='tight')

# 그래프 출력
plt.show()