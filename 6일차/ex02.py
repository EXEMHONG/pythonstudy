
# 텍스트 파일 입력하기

# 파일 저장 경로
path = 'C:/Huey/GIT/Python01-1/Day06/file/'
file = open(path + 'hello.txt', 'rt', encoding = 'UTF-8')
# rt : 읽기모드 + 텍스트모드

while True:
    data = file.read(10)        # 파일로부터 글자를 10글자씩 읽어온다.
    # data = file.readline()      # 한 줄씩 읽어온다.
    if not data:
        break
    print(data, end='')

# 파일 닫기 - 메모리 해제
file.close()

