import re  # 정규 표현식 사용을 위한 모듈
import smtplib  # smtp 연결을 위한 모듈
from email.message import EmailMessage  # MIME 메일 방식을 사용하기 위한 모듈
import imghdr  # 이미지 확장자를 읽어오기 위한 모듈

# smtp 연결을 위한 정보
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# SSL을 통한 smtp 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# 로그인 정보
mail_id = "king4mun@likelion.org"
mail_pw = "6f7472mun"

# smtp 객체를 통해 지메일 로그인
smtp.login(mail_id, password=mail_pw)

# 메일 표준 방식인 MIME을 사용하는 EmailMessage 객체 생성
message = EmailMessage()

# emailmessage 객체 해더 작성
message["Subject"] = "제목 입니다. (최종)"
message["From"] = mail_id
message["To"] = mail_id

# emailmessage 본문 작성
message.set_content("본문 내용입니다. (최종) 요새 열정이 다시 조금씩 불타는 중")

# 이미지 읽어오기
with open("logo.png", "rb") as image:
    image_file = image.read()

# 혹시 모를 이미지 확장자 변환을 대비하여 유연하게 subtype 지정
image_type = imghdr.what("logo", image_file)

# image file 첨부
message.add_attachment(image_file, maintype="image", subtype=image_type)

# 수신인 메일 유효성 체크
reg = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,3}$"
isOk = re.match(reg, message["To"])

if bool(isOk):
    smtp.send_message(message)
    print("정상적으로 전송되었습니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")

# smtp 연결 해제
smtp.quit()
