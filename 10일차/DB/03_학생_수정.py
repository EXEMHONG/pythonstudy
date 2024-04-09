import pymysql

# MySQL 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

std_id = input('수정할 학생의 학번을 입력하세요: ')

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 수정할 데이터 입력 받기
        new_name = input('새로운 이름: ')
        new_age = input('새로운 나이: ')
        new_grade = input('새로운 학년: ')
        
        # 데이터 수정 쿼리
        sql = "UPDATE 학생 SET 이름 = %s, 나이 = %s, 학년 = %s WHERE std_id = %s"
        result = cursor.execute(sql, (new_name, new_age, new_grade, std_id))  # 쿼리 실행 요청
        print('{} 행의 데이터 수정 완료'.format(result))
        
    # 변경사항 적용
    conn.commit()

except pymysql.Error as e:
    print('MySQL Error 발생:', e)

finally:
    # 연결 종료
    conn.close()

