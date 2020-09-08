import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

from .stock_list import *
from .stock_analysis1 import *

stock_code = 'sz.399001'
stock_name = '深圳成指'
start_time = '2010-01-01'
test_start = 247

m = 1.04

get_stockdata(stock_code, stock_name, start_time)
get_data(stock_code, stock_name)


for i in range(9, 10):
    test_end = test_start + 247 * i
    pctchg_analysis(test_start, test_end)