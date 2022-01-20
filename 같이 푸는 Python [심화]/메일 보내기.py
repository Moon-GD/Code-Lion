# 사전 준비 :
# 1. 계정 imap 활성화
# 2. 계정 외부 활동의 접근 허용

import smtplib
from email.message import EmailMessage  # MIME 기능을 사용하기 위한 모듈, 기능

SMTP_SERVER = "smtp.gmail.com"
# 지메일 포트 번호 : 465
SMTP_PORT = 465

message = EmailMessage()
message.set_content("email.message 모듈의 EmailMessage 기능을 사용하여 작성한 본문입니다.")

# SMTP 연결하기

## 일반적으로는 SMTP 방식으로 서버와 연결하면 되지만
## 지메일 같이 SSL 방식으로 암호화된 서버는 SMTP_SSL을 통해 추가적인 정보를 제공해야 한다.
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# SMTP 로그인하기
id = "king4mun@likelion.org"
password = "6f7472mun"
smtp.login(id, password=password)

smtp.send_message()
smtp.quit()
