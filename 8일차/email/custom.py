import smtplib
from email.mime.text import MIMEText
import csv

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        server.starttls()
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        response = server.sendmail(msg['From'], msg['To'], msg.as_string())
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print('응답결과: ')
            print(response)

def read_csv():
    path = 'D:\\python\\1\\pythonstudy\\8일차\\email\\'  # 파일 경로를 올바르게 수정
    file = path + 'custom.csv'
    custom_list = []

    with open(file, 'r', newline='', encoding='UTF-8') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar="'")
        for line in csv_reader:
            custom_list.append(line)
    return custom_list

def send_emails(smtp_info):
    custom_list = read_csv()
    for line in custom_list:
        receiver = line[1]  # 받는 사람 이메일
        sender = smtp_info['smtp_user_id']  # 보내는 사람 이메일
        title = line[2]
        content = line[3]

        msg = MIMEText(_text=content, _charset="utf-8")
        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = receiver

        send_email(smtp_info, msg)

# 네이버 SMTP 서버 정보
smtp_info = {
    "smtp_server": "smtp.naver.com",
    "smtp_user_id": input('네이버 메일주소 : '),
    "smtp_user_pw": input('비밀번호 : '),
    "smtp_port": 587
}

# 이메일 전송 함수 호출
send_emails(smtp_info)