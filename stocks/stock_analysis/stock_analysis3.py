import csv
from matplotlib import pyplot as plt
from datetime import datetime

"""
不同下跌天数买入，第二天均以收盘价卖出策略，它和m>1.1时stock_analysis2的结果是一样的
"""
def get_data_analysis3(stock_code, stock_name, test_start, test_end, m):
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

    """首跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_1 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-1] >= 0 and pctChgs[i] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_1.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_1, c='red')
    # plt.title(stock_code + '(n=1, m=' + str(m) + ')')
    # fig.autofmt_xdate()
    # plt.show()

    """连续两日下跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_2 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-2] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
            stock_num = 0  # 清仓，股票数量为0
            account_stock = 0  # 股票市值为0
            account_cash = account_cashes[-1] + (stock_nums[-1] * closes[i])  # 账户现金
            account_sum = account_cash + account_stock  # 当日账户总额
            stock_cost = 0
            account_profit = (account_sum - 1000000) * 100 / 1000000  # 对应当日账户总收益
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
        account_profits_2.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_2, c='red')
    # plt.title(stock_code + '(n=2)')
    # fig.autofmt_xdate()
    # plt.show()

    """连续三日下跌买入策略"""
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_3 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-3] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0 and pctChgs[i-2] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_3.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_3, c='red')
    # plt.title(stock_code + '(n=3)')
    # fig.autofmt_xdate()
    # plt.show()

    """
    连续四日下跌买入策略
    """
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_4 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-4] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0 and pctChgs[i-2] < 0 and pctChgs[i-3] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_4.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_4, c='red')
    # plt.title(stock_code + '(n=4)')
    # fig.autofmt_xdate()
    # plt.show()

    """
    连续五日下跌买入策略
    """
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_5 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-5] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0 and pctChgs[i-2] < 0 \
                and pctChgs[i-3] < 0 and pctChgs[i-4] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_5.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_5, c='red')
    # plt.title(stock_code + '(n=5)')
    # fig.autofmt_xdate()
    # plt.show()

    """
    连续六日下跌买入策略
    """
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_6 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-6] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0 and pctChgs[i-2] < 0 \
                and pctChgs[i-3] < 0 and pctChgs[i-4] < 0 and pctChgs[i-5] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_6.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_6, c='red')
    # plt.title(stock_code + '(n=6)')
    # fig.autofmt_xdate()
    # plt.show()

    """
    连续七日下跌买入策略
    """
    account_sums, account_stocks, account_cashes = [1000000], [0], [1000000]            # 总账户金额、股票市值、账户现金
    stock_nums, stock_costs, account_profits_7 = [0], [], []                              # 账户股票数量、股票成本、账户收益
    acts = []
    for i in range(test_start, test_end):
        if stock_nums[-1] == 0 and pctChgs[i-7] >= 0 and pctChgs[i] < 0 and pctChgs[i-1] < 0 and pctChgs[i-2] < 0 \
                and pctChgs[i-3] < 0 and pctChgs[i-4] < 0 and pctChgs[i-5] < 0 and pctChgs[i-6] < 0:                  # 账户空仓、当日下跌买入
            act = '买入'
            stock_num = account_sums[-1] // closes[i]               # 买入股票数量
            account_stock = stock_num * closes[i]                   # 股票市值
            account_cash = account_sums[-1] - account_stock         # 现金余额
            account_sum = account_cash + account_stock              # 当日账户总额
            stock_cost = closes[i]                                  # 股票成本
            account_profit = (account_sum - 1000000)*100/1000000    # 对应当日账户总收益
        elif stock_nums[-1] != 0:
            act = '卖出'
            """以收盘价卖出"""
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
        account_profits_7.append(account_profit)
        acts.append(act)

    """绘制收益曲线"""
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates[test_start:test_end], account_profits_7, c='red')
    # plt.title(stock_code + '(n=7)')
    # fig.autofmt_xdate()
    # plt.show()

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates[test_start:test_end], account_profits_1, c='r')
    plt.plot(dates[test_start:test_end], account_profits_2, c='b')
    plt.plot(dates[test_start:test_end], account_profits_3, c='g')
    plt.plot(dates[test_start:test_end], account_profits_4, c='c')
    plt.plot(dates[test_start:test_end], account_profits_5, c='y')
    plt.plot(dates[test_start:test_end], account_profits_6, c='k')
    plt.plot(dates[test_start:test_end], account_profits_7, c='m')
    fig.autofmt_xdate()
    t1 = str((dates[test_start].strftime("%Y-%m-%d")))
    t2 = str(dates[test_end].strftime("%Y-%m-%d"))
    plt.title(stock_code + '(n=1~7, m=' + str(m) + ')' + t1 + '--' + t2)
    plt.legend(['n=1', 'n=2', 'n=3', 'n=4', 'n=5', 'n=6', 'n=7'], loc='best', fontsize=8)
    plt.savefig('/home/cdd/Desktop/Scraping/stocks/stock_analysis/stock_data/'
                + stock_code + stock_name + t1 + '--' + t2 + '(' + str(m) + ')' + '.png')
    plt.show()


