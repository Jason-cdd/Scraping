import requests
from bs4 import BeautifulSoup
import json
import re
from tqdm import tqdm


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

    def parse_home_page(self, home_page, tag_id):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页内容
        :return: 解析后的puthon数据
        """
        # 2.从疫情首页，提取最近一日各国疫情数据
        soup = BeautifulSoup(home_page, 'lxml')  # soup和home_page区别不大
        script = soup.find(id=tag_id)
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
        last_day_corona_virus = self.parse_home_page(home_page, tag_id='getListByCountryTypeService2true')
        # 3.保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        # 1.加载各国疫情数据
        with open('data/last_day_corona_virus.json') as fp:
            last_day_corona_virus = json.load(fp)
        # print(last_day_corona_virus)
        # 定义列表，用于存储各国从1月23号至今的json数据
        corona_virus_data = []
        # 2.遍历各国疫情数据，获取统计的URL
        for country in tqdm(last_day_corona_virus, '采集1月23号以来各国疫情数据'):
            # 3.发送请求，获取各国从1月23号至今的json数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # print(statistics_data_json_str)
            # 4.把json数据转换为Python类型数据，添加列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus_data.extend(statistics_data)
        # 5.把列表以json格式保存为文件
        self.save(corona_virus_data, 'data/corona_virus_data.json')

    def crawl_last_day_corona_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        """
        # 1.发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析疫情首页，获取最近一日各省疫情数据
        last_day_corona_virus_of_china = self.parse_home_page(home_page, tag_id='getAreaStat')
        # 3.保存数据
        self.save(last_day_corona_virus_of_china, 'data/last_day_corona_virus_of_china.json')

    def run(self):
        self.crawl_last_day_corona_virus()
        # self.crawl_corona_virus()
        self.crawl_last_day_corona_virus_of_china()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
