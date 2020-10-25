import requests
from bs4 import BeautifulSoup
import json
import re


class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """
        根据URL获取响应内容的字符串数据
        :param url: 请求的URL
        :return: 响应内容的字符串
        """
        response = requests.get(url)  # <Response [200]>
        return response.content.decode()
        # print(home_page)

    def parse_home_page(self, home_page):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页内容
        :return: 解析后的puthon数据
        """
        # 2.从疫情首页，提取最近一日各国疫情数据
        soup = BeautifulSoup(home_page, 'lxml')  # soup和home_page区别不大
        # print(soup)
        script = soup.find(id="getListByCountryTypeService2true")
        text = script.contents
        # 3.从疫情数据中，获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text[0])[0]
        # 4.把json格式的字符串转换为Python类型
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        # 5.以json格式保存最近一日各国疫情数据
        with open(path, 'w') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析首页内容，获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3.保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    def run(self):
        self.crawl_last_day_corona_virus()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
