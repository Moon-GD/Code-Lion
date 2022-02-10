import requests
from bs4 import BeautifulSoup
import datetime

year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

print(f'{year}년 {month}월 {day}일 각 지역 온도입니다.', end="\n\n")
city_list = ['서울', '대전', '보성', '대구']
for city in city_list:
    url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=' + city + '+날씨'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    temp_list = soup.findAll('strong', class_='txt_temp')
    temp = temp_list[0].text

    print(f'{city}의 온도는 {temp} 입니다.')