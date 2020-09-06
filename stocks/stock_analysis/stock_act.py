from .stock_list import *
from .stock_analysis import *
from .stock_analysis2 import *
from .stock_analysis3 import *
from matplotlib import pyplot as plt


stock_code = 'sh.000001'
stock_name = '上证综指'
start_time = '2010-01-01'
test_start = 247

m = 1

get_stockdata(stock_code, stock_name, start_time)
# get_data(stock_code, stock_name)
# stock_analysis_1(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_2(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_3(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_4(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_5(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_6(stock_code, stock_name, test_start, test_end, m)
# stock_analysis_7(stock_code, stock_name, test_start, test_end, m)

for i in range(1, 10):
    test_end = test_start + 247 * i
    get_data_analysis3(stock_code, stock_name, test_start, test_end, m)
