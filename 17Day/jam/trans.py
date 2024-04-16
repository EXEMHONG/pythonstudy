# googletrans 모듈을 사용하여 번역하는 프로그램
from googletrans import Translator
import os

# 현재 실행 파일 경로 가져오고, 입력파일 지정하기
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 텍스트 번역 함수
def translate_text(input_file, output_file, source_lang='en', target_lang='ko'):
    # 구글 번역 객체 생성
    translator = Translator()
    
    # 파일 입력
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_text = input_file.read()
        
        # 텍스트 번역
        translated_text = translator.translate(input_text, src=source_lang, dest=target_lang)
        
        # 번역 결과 출력
        with open(output_file, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_text.text)

# 입력 파일 및 출력 파일 경로 설정
input_file = path + '/' + input('입력 파일 : ')
output_file = path + '/' + input('출력 파일 : ')

# 번역 실행
translate_text(input_file, output_file, 'en', 'ja')
print('번역이 완료되었습니다!')