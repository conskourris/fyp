import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np
import mplfinance as mpf
import pandas as pd
import pandas_datareader as web
import random
import pickle

def plot_around_index(ticker, i, day_range):

	try :
		df = pd.read_csv('historical/{}.csv'.format(ticker), parse_dates=True, index_col=0)

		mpf.plot(df[i-day_range : i+day_range], type='candle', ylabel_lower='', figsize=(10,6))

	except IndexError :
		pass