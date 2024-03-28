import csv        
def read_csv():
    path = 'C:/Huey/GIT/Python01-1/Day08/'
    file = path + 'custom.csv'

    with open(file, 'r', newline='', encoding='UTF-8') as file:
    # reader(파일객체, delimiter(구분기호), quotechar(문자열기호))
    # quotechar : 나뉘면 안되는 데이터를 어떤 기호로 묶을지 지정
        csv_reader = csv.reader(file, delimiter=',', quotechar="'")

        return list(csv_reader)

# 이메일 내용

custom_csv = read_csv()

# csv 파일 전체 인원에 메일 발송
for line in custom_csv:
    receiver = line[1]                      # 받는 사람
    sender = smtp_info['smtp_user_id']      # 보내는 사람
    title = line[2]
    content = line[3]

    # 메일 객체 생성
    msg = MIMEText(_text = content, _charset = "utf-8")
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    # 이메일 전송
    send_email(smtp_info, msg)