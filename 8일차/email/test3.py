# 데코레이터
# 다른 함수를 받아 그 함수의 기능을 추가하거나 수정할 수있는 함수


#def my_decorator(func):
#    def wrapper():
#        print("Something is happening before the function is called.")
#        func()
#        print("Something is happening after the function is called.")
#    return wrapper
#
#@my_decorator
#def say_hello():
#    print("Hello!")

#say_hello()



# 데코레이터 함수 정의
def my_decorator(func):
    # 내부 함수 정의
    def wrapper():
        print('함수가 호출되기전...')
        func()  # 입력받은 함수 호출
        print('함수 호출 후....')

    return wrapper  # 내부 함수를 반환

# 데코레이터를 사용하여 sample() 함수에 장식
@my_decorator
def sample():
    print('데코레이터 함수로 장식된 함수...')

# sample() 함수 호출
sample()