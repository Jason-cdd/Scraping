from .stock_list import *
from .stock_analysis import *


stock_code = 'sh.000001'
stock_name = '上证综指'
start_time = '2010-01-01'
get_stockdata(stock_code, stock_name, start_time)
get_data(stock_code, stock_name)
# stock_analysis_1(stock_code, stock_name, test_start=247, test_end=247*2, m=1.02)
# stock_analysis_2(stock_code, stock_name, test_start=247, test_end=247*2, m=1.02)
stock_analysis_3(stock_code, stock_name, test_start=247, test_end=247*2, m=1.02)