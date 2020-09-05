import requests
from fake_useragent import UserAgent
import re
import csv
import clsDir


def getHtml(url):
    r = requests.get(url, headers={
        'User-Agent': UserAgent().random,
    })
    r.encoding = r.apparent_encoding
    return r.text


stockUrl = 'http://86.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124064028201763104_1562133297741&pn=1&pz=100000&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f12&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f12,f14&_=1562133297790'
PATTERN_STOCK = "},{"
if __name__ == '__main__':
    # 创建目录
    mkpath = "Desktop/Scraping/stocks/stocks_list/stock_listdata"
    # 调用函数
    clsDir.mkdir(mkpath)

    html = getHtml(stockUrl)
    reslist = re.split(PATTERN_STOCK, html.replace("\"", "").replace("}]}});", ""))
    # 数据清洗：去掉非个股,个股以6（沪市）,0（深市）,3（创业板）开头
    datalist = reslist[:]
    for res in reslist:
        if not res.startswith('f12'):
            datalist.remove(res)
            continue
        res = res.replace("f12:", "").replace("f14:", "")
        if not (str(res[1]).startswith('6') or str(res[1]).startswith('3') or str(res[1]).startswith('0')):
            datalist.remove(res)
    f = open('Desktop/Scraping/stocks/stocks_list/stock_listdata.csv', 'w+', encoding='utf-8', newline="")
    writer = csv.writer(f)
    writer.writerow(('名称', '代码'))
    for data in datalist:
        stock = data.replace("f12:", "").replace("f14:", "").split(",")
        writer.writerow((stock[1].replace("*", ""), stock[0]))
    f.close()
