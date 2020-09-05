import pandas as pd

st_data = pd.read_csv('/home/cdd/Desktop/Scraping/stocks/stock_analysis/stock_data/sh.000001上证综指.csv')
print(st_data.iloc[0:3, 1])