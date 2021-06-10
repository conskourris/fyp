import os
import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import matplotlib
import numpy as np
from math import floor
from scipy.stats import skew
import mplfinance as mpf
import pandas as pd
import pandas_datareader as web
import random
import pickle
import json

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *
from trading_tools import *

from trading_strategies.best_strategies import *

# from keras.models import Sequential
from sklearn.model_selection import train_test_split

font = {'size'   : 14}
matplotlib.rc('font', **font)


def save_train_test_dicts(pattern, strategy, index_strategy, days_prior) :

	indexes = index_strategy(pattern)

	with open(f'sp100tickers.pickle', 'rb') as f:
		tickers = pickle.load(f)

	returns_dict, returns = get_pattern_trading_results(pattern, strategy)
	returns_dict = returns_dict[()]

	x_train_dict, x_test_dict = {}, {} 
	y_train_dict, y_test_dict = {}, {}

	_, pattern_length, _ = pattern(get_info=True)

	for ticker in tickers :
		x_ticker = []
		y_ticker = []
		try :
			df = pd.read_csv(f'historical/{ticker}.csv')
		except :
			continue

		for n, i in enumerate(indexes[ticker]) :

			occurrence_data = []

			ref = df['Open'].iloc[i]
			occ_ref = df['Volume'].iloc[i]

			for x in range(days_prior+pattern_length) :
				occurrence_data.append(df['Open'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['High'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Low'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Close'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Volume'].iloc[i-days_prior+x]/occ_ref)

			x_ticker.append(occurrence_data)
			y_ticker.append(returns_dict[ticker][n])

		x_ticker = np.array(x_ticker)
		y_ticker = np.array(y_ticker)

		x_train, x_test, y_train, y_test = train_test_split(x_ticker, y_ticker, test_size=0.3, random_state=42)

		x_train_dict[ticker] = x_train
		x_test_dict[ticker] = x_test
		y_train_dict[ticker] = y_train
		y_test_dict[ticker] = y_test

	if os.path.exists(f'train_test_results/{pattern.__name__}') is False :
		os.mkdir(f'train_test_results/{pattern.__name__}')

	np.savez(f'train_test_results/{pattern.__name__}/{days_prior}days.npz', x_train_dict, x_test_dict, y_train_dict, y_test_dict)

	return x_train_dict, x_test_dict, y_train_dict, y_test_dict


def get_train_test_dicts(pattern, strategy, days_prior) :

	results = np.load(f'train_test_results/{pattern.__name__}/{days_prior}days.npz', allow_pickle=True)
	print(f'got {strategy.__name__} for {pattern.__name__}')

	x_train_dict = results['arr_0'][()]
	x_test_dict = results['arr_1'][()]
	y_train_dict = results['arr_2'][()]
	y_test_dict = results['arr_3'][()]

	return x_train_dict, x_test_dict, y_train_dict, y_test_dict


def flatten_dict(dictionary) :
	flat = []
	for k in dictionary :
		for l in dictionary[k] :
			flat.append(l)

	return flat
