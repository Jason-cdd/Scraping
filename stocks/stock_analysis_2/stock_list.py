import baostock as bs
import pandas as pd


def get_stockdata(stock_code, stock_name, start_time):
    # 登陆系统
    lg = bs.login()

    # 获取沪深A股历史K线数据
    rs = bs.query_history_k_data_plus(stock_code, "date,open,high,low,close,preclose,pctChg",
                                      start_date=start_time,
                                      frequency="d", adjustflag="2")
    # adjustflag 默认前复权（1），后复权（2）,不复权（3）

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    # 结果集输出到csv文件
    result.to_csv("/home/cdd/Desktop/Scraping/stocks/stock_analysis_2/stock_data1/" + stock_code + stock_name + ".csv", index=False)
    print(result)

    # 登出系统
    bs.logout()


if __name__ == '__main__':
    get_stockdata(stock_code='sh.000001', stock_name='上证综指', start_time='2010-01-01')