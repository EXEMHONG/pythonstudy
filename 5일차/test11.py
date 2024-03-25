# 자원을 해제하는 실행문
# 예외 발생과 상관없는 실행문에 사용
try:
    file = open('nofile.txt', 'r')
    line = file.readline()
except IOError:
    print('파일 입출력 시, 예외가 발생하였습니다')
else:
    print(line)
    file.close()        # 파일 메모리 자원 해제
finally:
    print('예외 발생과 무관하게 실행')