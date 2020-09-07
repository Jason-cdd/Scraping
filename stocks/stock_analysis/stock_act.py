import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

from .stock_list import *
from .stock_analysis import *
from .stock_analysis2 import *
from .stock_analysis3 import *
from .stock_analysis4_1 import *
from .stock_analysis4_2 import *
from .stock_analysis4_3 import *
from .stock_analysis4_4 import *
from .stock_analysis4_5 import *
from .stock_analysis4_6 import *
from .stock_analysis4_7 import *


from matplotlib import pyplot as plt


# stock_code = 'sh.000001'
# stock_name = '上证综指'
# start_time = '2010-01-01'
# test_start = 247
#
# m = 1.04
#
# get_stockdata(stock_code, stock_name, start_time)
# get_data(stock_code, stock_name)
# # stock_analysis_1(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_2(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_3(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_4(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_5(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_6(stock_code, stock_name, test_start, test_end, m)
# # stock_analysis_7(stock_code, stock_name, test_start, test_end, m)
#
# for i in range(9, 10):
#     test_end = test_start + 247 * i
#     get_data_analysis4_7(stock_code, stock_name, test_start, test_end)
#     # stock_analysis_1(stock_code, stock_name, test_start, test_end, m)

list_n1 = [-29.44, -50.66, -34.47, -27.58, -29.63, -29.44, -29.44, -29.44]
list_n2 = [9.53, -20.71, 1.4, 6.35, 11.05, 14.99, 9.78, 9.53]
list_n3 = [-7.62, -21.97, -15.66, -11.52, -7.83, -5.76, -4.42, -3.51]
list_n4 = [16.28, 9.59, 17.32, 20.01, 22.27, 16.28, 16.28, 16.28]
list_n5 = [9.41, 0.36, 5.35, 6.97, 8.01, 9.05, 9.41, 9.41]
list_n6 = [2.13, 1.63, 2.11, 2.13, 2.13, 2.13, 2.13, 2.13]
list_n7 = [-1.13, -1.95, -1.13, -1.13, -1.13, -1.13, -1.13, -1.13]
list_n = [1, 2, 3, 4, 5, 6, 7, 8]

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(list_n, list_n1, c='b')
plt.plot(list_n, list_n2, c='g')
plt.plot(list_n, list_n3, c='r')
plt.plot(list_n, list_n4, c='c')
plt.plot(list_n, list_n5, c='m')
plt.plot(list_n, list_n6, c='y')
plt.plot(list_n, list_n7, c='k')
plt.legend(['n=1', 'n=2', 'n=3', 'n=4', 'n=5', 'n=6', 'n=7'], loc='best', fontsize=5)

plt.show()

np_nm = np.array([list_n1, list_n2, list_n3, list_n4, list_n5, list_n6, list_n7])
print(np_nm)
pd_nm = DataFrame(data=np_nm,
                  index=['n=1', 'n=2', 'n=3', 'n=4', 'n=5', 'n=6', 'n=7'],
                  columns=['m=1', 'm=1.01', 'm=1.02', 'm=1.03', 'm=1.04', 'm=1.05', 'm=1.06', 'm=1.07'])

print(pd_nm)

