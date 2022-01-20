import requests
import json
import datetime

city = 'Seoul'
apikey = 'e073a15785e2fd57ed4a733419f3dc27'
lang = 'kr'
units = 'metric'

apikey = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"
result = requests.get(apikey)

# 딕셔너리 타입으로 형 변환
data = json.loads(result.text)

main_data = data['main']
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

# 이쁘게 출력
print(f"{year}년 {month}월 {day}일 기준 {city} 지역 날씨입니다.")
print(f"최고 기온 {main_data['temp_max']}, 최저 기온 {main_data['temp_min']}, 체감 온도 {main_data['feels_like']}")
print(f"기압 : {main_data['pressure']}, 습도 {main_data['humidity']}")
