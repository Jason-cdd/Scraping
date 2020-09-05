import csv
from matplotlib import pyplot as plt
from datetime import datetime


def get_data(stock_code, stock_name):
    global dates, open_prices, highs, lows, closes, precloses, pctChgs
    filename = '/home/cdd/Desktop/Scraping/stocks/stock_analysis/stock_data/' + stock_code + stock_name + '.csv'
    with open(filename) as f:
        reader = csv.reader(f)

        dates, open_prices, highs, lows, closes, precloses, pctChgs = [], [], [], [], [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                open_price = float(row[1])
                high = float(row[2])
                low = float(row[3])
                close = float(row[4])
                preclose = float(row[5])
                pctChg = float(row[6])
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


def stock_analysis_1(stock_code, stock_name, test_start, test_end, m):
    """首跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            if (highs[i] - precloses[i])*100/precloses[i] > 2:
                """如果当日最大涨幅超过2%，则以2%卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (account_stocks[-1] * m)      # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
            else:
                """否则以收盘价卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (stock_nums[-1] * closes[i])  # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
        else:
            act = '空仓'
            stock_num = 0                                                   # 空仓，股票数量为0
            account_stock = 0                                               # 空仓，股票市值为0
            account_cash = account_cashes[-1]                               # 账户现金不变
            account_sum = account_sums[-1]                                  # 账户总额不变
            stock_cost = 0
            account_profit = (account_sum - 1000000) * 100 / 1000000        # 对应当日账户总收益

        """更新账户"""
        account_sums.append(account_sum)
        account_cashes.append(account_cash)
        account_stocks.append(account_stock)
        stock_nums.append(stock_num)
        stock_costs.append(stock_cost)
        account_profits.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates[test_start:test_end], account_profits, c='red')
    plt.title(stock_code)
    fig.autofmt_xdate()
    plt.show()


def stock_analysis_3(stock_code, stock_name, test_start, test_end, m):
    """连续三日下跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i] < 0 and pctChgs[i-1] and pctChgs[i-2] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            if (highs[i] - precloses[i])*100/precloses[i] > 2:
                """如果当日最大涨幅超过2%，则以2%卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (account_stocks[-1] * m)      # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
            else:
                """否则以收盘价卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (stock_nums[-1] * closes[i])  # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
        else:
            act = '空仓'
            stock_num = 0                                                   # 空仓，股票数量为0
            account_stock = 0                                               # 空仓，股票市值为0
            account_cash = account_cashes[-1]                               # 账户现金不变
            account_sum = account_sums[-1]                                  # 账户总额不变
            stock_cost = 0
            account_profit = (account_sum - 1000000) * 100 / 1000000        # 对应当日账户总收益

        """更新账户"""
        account_sums.append(account_sum)
        account_cashes.append(account_cash)
        account_stocks.append(account_stock)
        stock_nums.append(stock_num)
        stock_costs.append(stock_cost)
        account_profits.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates[test_start:test_end], account_profits, c='red')
    plt.title(stock_code)
    fig.autofmt_xdate()
    plt.show()

def stock_analysis_2(stock_code, stock_name, test_start, test_end, m):
    """连续两日下跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            if (highs[i] - precloses[i])*100/precloses[i] > 2:
                """如果当日最大涨幅超过2%，则以2%卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (account_stocks[-1] * m)      # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
            else:
                """否则以收盘价卖出"""
                stock_num = 0                                                     # 清仓，股票数量为0
                account_stock = 0                                                 # 股票市值为0
                account_cash = account_cashes[-1] + (stock_nums[-1] * closes[i])  # 账户现金
                account_sum = account_cash + account_stock                        # 当日账户总额
                stock_cost = 0
                account_profit = (account_sum - 1000000) * 100 / 1000000          # 对应当日账户总收益
        else:
            act = '空仓'
            stock_num = 0                                                   # 空仓，股票数量为0
            account_stock = 0                                               # 空仓，股票市值为0
            account_cash = account_cashes[-1]                               # 账户现金不变
            account_sum = account_sums[-1]                                  # 账户总额不变
            stock_cost = 0
            account_profit = (account_sum - 1000000) * 100 / 1000000        # 对应当日账户总收益

        """更新账户"""
        account_sums.append(account_sum)
        account_cashes.append(account_cash)
        account_stocks.append(account_stock)
        stock_nums.append(stock_num)
        stock_costs.append(stock_cost)
        account_profits.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates[test_start:test_end], account_profits, c='red')
    plt.title(stock_code)
    fig.autofmt_xdate()
    plt.show()