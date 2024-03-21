#이렇게적는거는 많은 모듈을 포함할 때, 모듈을 구분하기좋다(as:alias)
#import secure as c

#적은 모듈을 포함할 때, 쉽게 쓸 수 있다.
from secure import *

# 사용자 정보 마스킹하기

name = '김조은'
no = '12345-789000'
phone = '000-0000-0000'

print ( name )
print ( no )
print ( phone )
print ()

print ( secure_name(name))
print (secure_no (no))
print (secure_phone (phone))

