import requests
from bs4 import BeautifulSoup
import json
import re

# 1.发送请求，获取疫情首页
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')  # <Response [200]>
home_page = response.content.decode()
# print(home_page)

# 2.从疫情首页，提取最近一日各国疫情数据
soup = BeautifulSoup(home_page, 'lxml')  # soup和home_page区别不大
# print(soup)
script = soup.find(id="getListByCountryTypeService2true")
print(script)
text = script.contents
print(text)

# 3.从疫情数据中，获取json格式的字符串
json_str = re.findall(r'\[.+\]', text[0])[0]
print(json_str)

# 4.把json格式的字符串转换为Python类型
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)

# 5.以json格式保存最近一日各国疫情数据
# with open('data/last_day_corona_virus.json', 'w') as fp:
#     json.dump(last_day_corona_virus, fp, ensure_ascii=False)
