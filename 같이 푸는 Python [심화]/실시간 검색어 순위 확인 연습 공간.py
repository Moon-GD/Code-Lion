# Daum에서 원하는 지역의 현재 온도 가져오기
import requests
from bs4 import BeautifulSoup
import datetime

city_list = ['서울', '광주', '나주']

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

print('{}년 {}월 {}일 기준 날씨 정보를 가져오겠습니다\n'.format(year, month, day))
for city in city_list:
    name = city
    url = 'https://m.search.daum.net/search?nil_profile=btn&w=tot&DA=SBC&q=' + name + '+날씨'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    temp_list = soup.findAll('em', class_='txt_temp')
    temp = temp_list[0].text

    print('현재 {} 온도는 {}입니다.'.format(name, temp))

