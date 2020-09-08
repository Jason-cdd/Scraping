import csv
import pygal
from matplotlib import pyplot as plt
from datetime import datetime

"""本部分主要统计各涨跌幅的概率分布"""

def get_data(stock_code, stock_name):
    global dates, open_prices, highs, lows, closes, precloses, pctChgs, pctChgs_highs
    filename = '/home/cdd/Desktop/Scraping/stocks/stock_analysis_2/stock_data1/' + stock_code + stock_name + '.csv'
    with open(filename) as f:
        reader = csv.reader(f)

        dates, open_prices, highs, lows, closes, precloses, pctChgs, pctChgs_highs = [], [], [], [], [], [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                open_price = round(float(row[1]), 2)
                high = round(float(row[2]), 2)
                low = round(float(row[3]), 2)
                close = round(float(row[4]), 2)
                preclose = round(float(row[5]), 2)
                pctChg = round(float(row[6]), 2)
                pctChgs_high = round(((high - preclose)*100 / preclose), 2)
            except ValueError:
                pass
            else:
                dates.append(current_date)
                open_prices.append(open_price)
                highs.append(high)
                lows.append(low)
                closes.append(close)
                precloses.append(preclose)
                pctChgs.append(pctChg)
                pctChgs_highs.append(pctChgs_high)


def pctchg_analysis(test_start, test_end):
    pct07, pct06_7, pct05_6, pct04_5, pct03_4, pct02_3, pct01_2, pct00_1 = \
        [], [], [], [], [], [], [], []

    pct0, pct10_1, pct11_2, pct12_3, pct13_4, pct14_5, pct15_6, pct16_7, pct17 = \
        [], [], [], [], [], [], [], [], []

    for i in range(test_start, test_end+1):
        p = pctChgs[i]
        if p <= -7:
            pct07.append(p)
        elif -7 < p <= -6:
            pct06_7.append(p)
        elif -6 < p <= -5:
            pct05_6.append(p)
        elif -5 < p <= -4:
            pct04_5.append(p)
        elif -4 < p <= -3:
            pct03_4.append(p)
        elif -3 < p <= -2:
            pct02_3.append(p)
        elif -2 < p <= -1:
            pct01_2.append(p)
        elif -1 < p < 0:
            pct00_1.append(p)
        elif p == 0:
            pct0.append(p)
        elif 0 < p <= 1:
            pct10_1.append(p)
        elif 1 < p <= 2:
            pct11_2.append(p)
        elif 2 < p <= 3:
            pct12_3.append(p)
        elif 3 < p <= 4:
            pct13_4.append(p)
        elif 4 < p <= 5:
            pct14_5.append(p)
        elif 5 < p <= 6:
            pct15_6.append(p)
        elif 6 < p <= 7:
            pct16_7.append(p)
        elif 7 < p:
            pct17.append(p)

    frequencies = []
    for list in (pct07, pct06_7, pct05_6, pct04_5, pct03_4, pct02_3, pct01_2, pct00_1,
                 pct0, pct10_1, pct11_2, pct12_3, pct13_4, pct14_5, pct15_6, pct16_7, pct17):
        frequency = len(list)
        frequencies.append(frequency)

    pctdata = pygal.Bar()
    pctdata.x_labels = ['07', '06_7', '05_6', '04_5', '03_4', '02_3', '01_2', '00_1', '0',
                        '10_1', '11_2', '12_3', '13_4', '14_5', '15_6', '16_7', '17']
    pctdata.add('pctdata_close', frequencies)
    pctdata.render_to_file('pctdata_close.svg')