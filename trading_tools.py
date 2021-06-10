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
from pandas_datareader import data
import random
import pickle
import json

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *
from trading_strategies import *

font = {'size'   : 14}
matplotlib.rc('font', **font)


def save_pattern_trading_results(pattern, strategy) :

	rets_dict, rets_list = strategy(pattern)

	if os.path.exists(f'trading_results/{strategy.__name__}') is False :
		os.mkdir(f'trading_results/{strategy.__name__}')

	np.savez(f'trading_results/{strategy.__name__}/{pattern.__name__}.npz', rets_dict, rets_list)
	print(f'saved {strategy.__name__} for {pattern.__name__}')


def get_pattern_trading_results(pattern, strategy) :

	results = np.load(f'trading_results/{strategy.__name__}/{pattern.__name__}.npz', allow_pickle=True)
	print(f'got {strategy.__name__} for {pattern.__name__}')
	dict_results = results['arr_0']
	list_results = results['arr_1']

	return dict_results, list_results


def plot_hist_trading_results(pattern, strategy) :

	_, data = get_pattern_trading_results(pattern, strategy)

	if len(data) == 0 :
		return None, None

	rng = max(data) - min(data)
	mean = sum(data)/len(data)
	std = np.std(data)
	occurances = len(data)

	plt.figure(figsize=(10,6))
	plt.title(f'Distribution of return of {strategy.__name__} on {pattern.__name__}')
	plt.hist(data, bins=int(rng/0.005))
	plt.vlines(mean, 0, occurances/10)
	plt.xlabel('Return')
	plt.ylabel('Occurances')

	print('Mean: ', mean)
	print('S.D: ', std)
	print('Skewness: ', skew(data))
	print('Occurances: ', occurances)

	return mean, std


def get_distribution_metrics(pattern, strategy, occ=False) :

	_, data = get_pattern_trading_results(pattern, strategy)

	if occ is True :
		ret = sum(data)
	else :
		ret = sum(data) / len(data)

	std = np.std(data)

	return ret, std


def plot_patterns_on_strategy(patterns, strategy, occ=False) :

	returns = []
	stds = []
	labels = []

	plt.figure(figsize=(10, 6))
	plt.title(f'Return against volatility for patterns on {strategy.__name__}')

	counter = 0
	for pattern in patterns :
		counter += 1
		_, data = get_pattern_trading_results(pattern, strategy)

		if occ is True :
			ret = sum(data)
		else :
			ret = sum(data)/len(data)
		std = np.std(data)

		returns.append(ret)
		stds.append(std)

		if counter <= 10 :
			plt.plot(std, ret, 'o', label=pattern.__name__)

		else :
			plt.plot(std, ret, 'x', label=pattern.__name__)
		print(f'Occurances: {len(data)}')

	plt.xlabel('Volatility')
	plt.ylabel('Return')
	plt.legend(loc='best')

	return returns, stds


def plot_strategies_on_pattern(strategies, pattern, occ=False) :

	returns = []
	stds = []
	labels = []

	plt.figure(figsize=(10, 6))
	plt.title(f'Return against volatility for strategies on {pattern.__name__}')

	counter = 0
	for strategy in strategies :
		counter += 1

		_, data = get_pattern_trading_results(pattern, strategy)

		if occ is True :
			ret = sum(data)
		else :
			ret = sum(data)/len(data)
		std = np.std(data)

		returns.append(ret)
		stds.append(std)

		if counter <= 10 :
			plt.plot(std, ret, 'o', label=strategy.__name__)

		else :
			plt.plot(std, ret, 'x', label=strategy.__name__)

		print(f'Occurances: {len(data)}')

	plt.xlabel('Volatility')
	plt.ylabel('Return')
	plt.legend(loc='best')

	return returns, stds


def plot_patterns_on_strategies(patterns, strategies, bullish, occ=False) :

	returns = []
	stds = []
	labels = []

	plt.figure(figsize=(10, 6))
	plt.title(f'Return against volatility for patterns on their optimal strategy')

	counter = 0
	for i, pattern in enumerate(patterns) :
		_, _, nature = pattern(get_info=True)

		if nature == bullish :
			counter += 1
			_, data = get_pattern_trading_results(pattern, strategies[i])

			if occ is True :
				ret = sum(data)
			else :
				ret = sum(data)/len(data)
			std = np.std(data)

			returns.append(ret)
			stds.append(std)

			if counter <= 10 :
				plt.plot(std, ret, 'o', label=pattern.__name__)

			else :
				plt.plot(std, ret, 'x', label=pattern.__name__)
			print(f'Occurances: {len(data)}')

		else :
			pass

	plt.xlabel('Volatility')
	plt.ylabel('Return')
	plt.legend(loc='best')

	return returns, stds


def get_most_profitable_strategies(strategies, pattern, occ=False) :
	amount = 10
	returns = []
	stds = []
	labels = []

	for strategy in strategies :

		_, data = get_pattern_trading_results(pattern, strategy)

		if occ is True :
			ret = sum(data)
		else :
			ret = sum(data)/len(data)
		std = np.std(data)

		returns.append(ret)
		stds.append(std)
		labels.append(strategy.__name__)

	max_returns = []
	max_stds = []
	max_labels = []

	for i in range(amount) :
		index = returns.index(max(returns))

		max_returns.append(returns.pop(index))
		max_stds.append(stds.pop(index))
		max_labels.append(labels.pop(index))

	plt.figure(figsize=(10, 6))
	plt.title(f'Return against volatility for most profitable strategies on {pattern.__name__}')
	for i in range(len(max_returns)) :
		plt.plot(max_stds[i], max_returns[i], 'o', label=max_labels[i])
	plt.xlabel('Standard Deviation')
	plt.ylabel('Log Return')
	plt.legend(loc='best')

	return max_returns, max_stds
