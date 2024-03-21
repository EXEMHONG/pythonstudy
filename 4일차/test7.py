# 모듈
'''
    모듈이란?
    : 변수나 함수 또는 클래스를 모아놓은 파이썬 파일
    - 하나의 파이썬 파일(.py)
    
    모듈 사용
    : import 모듈명
'''

import conver       #위에꺼만 쓸거면 as 로 별명은 준다음 써야함 ex        import conver as a            >      miles = a.kilometer_to_miles(150)
from conver import *
# 150km --> mukes 단위로 변경
miles = kilometer_to_miles(150)
print('150km = {} miles'.format( miles))

# 1000g --> pound 로 변환
pound = gram_to_pound(1000)
print('1000g = {} pound'.format( pound ))