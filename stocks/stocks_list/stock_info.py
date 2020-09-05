import csv
import urllib.request as r
import threading
import clsDir


# 读取之前获取的个股csv丢入到一个列表中
def getStockList():
    stockList = []
    f = open('Desktop\\Scraping\\stocks\\stocks_list\\stock_listdata.csv', 'r', encoding='utf-8')
    f.seek(0)
    reader = csv.reader(f)

    for item in reader:
        stockList.append(item)
    f.close()
    return stockList


def downloadFile(url, filepath):
    try:
        r.urlretrieve(url, filepath)
    except Exception as e:
        print(e)
    print(filepath, "is downloaded")
    pass


# 设置信号量，控制线程并发数
sem = threading.Semaphore(100)


def downloadFileSem(url, filepath):
    with sem:
        downloadFile(url, filepath)


urlStart = 'http://quotes.money.163.com/service/chddata.html?code='
urlEnd = '&end=20190701&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'

if __name__ == '__main__':
    # 创建目录
    mkpath = "Desktop\\Scraping\\stocks\\stocks_list\\stock_info"
    # 调用函数
    clsDir.mkdir(mkpath)

    stockList = getStockList()
    stockList.pop(0)
    for s in stockList:
        scode = str(s[1])
        # 0：沪市；1：深市
        url = urlStart + ("0" if scode.startswith('6') else "1") + scode + urlEnd
        filepath = 'Desktop\\Scraping\\stocks\\stocks_list\\stock_info/' + (scode + '_' + str(s[0])) + '.csv'
        threading.Thread(target=downloadFileSem, args=(url, filepath)).start()
