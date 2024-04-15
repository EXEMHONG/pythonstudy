# 히스토그램
import matplotlib.pyplot as plt
import numpy as np


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'



# 학생들의 성적 분포를 히스토그램응 출력
# 데이터
score = np.random.normal(loc= 70, scale= 10, size= 500 )

#히스토그램 그래프 설정
plt.hist(score, edgecolor = 'black', color='blue')

# 제목 및 라벨
plt.title('학생들의 성적 분포')
plt.xlabel('성적')
plt.ylabel('빈도')

# 그래프 이미지 저장
plt.savefig('히스토그램.png' , dpi=400)

# 그래프 출력
plt.show()