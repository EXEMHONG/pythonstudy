# pip install pymysql
import pymysql

# mysql 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM 학생"
        cursor.execute(sql)
        
        student = cursor.fetchall()
        
        for student in student:
            print( student )
except pymysql.MySQLError as e:
    print('Mysql 에러 : ', e)
finally:
    conn.close()