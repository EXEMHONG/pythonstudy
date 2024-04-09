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

std_id = input('학번 : ')

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 삭제 쿼리
        sql = "DELETE FROM 학생 WHERE std_id = %s"
        result = cursor.execute(sql, std_id)  # 쿼리 실행 요청
        print('{} 행의 데이터 삭제 완료'.format(result))
        
    # 변경사항 적용
    conn.commit()

except pymysql.Error as e:
    print('MySQL Error 발생:', e)

finally:
    # 연결 종료
    conn.close()