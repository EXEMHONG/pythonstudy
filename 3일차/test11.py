# 문자열 내장 함수
'''
    (참조) 모든 문자는 각각 문자 코드를 가지고 있다.
           (아스키 코드,, 유니코드)
           
    1. chr() 함수
    : 특정 문자의 유니코드 값을 입력하면,
      해당 문자를 반환하는 함수
      
    2. ord() 함수
    : 특정 문자를 입력하면,
      해당 문자의 유니코드를 반환하는 함수
      
    3. eval() 함수
    : 표현식을 문자열로 입력하면 표현식의 연산결과를 반환하는 함수
    ex) eval('100 + 200') --> 300
        a = 10
        eval('a * 5)    --> 50
        
    4. format() 함수
    : 전달받은 값과 포맷코드에 따른 형식 문자열을 반환하는 함수
    # 천 단위 구분 기호로 쉼표(,) 를 사용
    ex) format(10000000, ',') --> 100,00,000
    
    5. str() 함수
    : 전달받은 인수를 문자열로 변환하는 함수
    ex) str(10) --> '10'
'''

# chr 
print ( chr(97))        # a
print ( chr(98))        # b
print ( chr(99))        # c
# ord
print ( ord('a'))       #97
print ( ord('b'))       #98
print ( ord('c'))       #99
# eval
expr = input('수식을 입력 : ')  # '100+200'
result = eval(expr)
print('계산결과 : {}'.format(result))
# format
print( format(1000000, ','))
# str
print( str(1.5))
