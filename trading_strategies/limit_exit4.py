import pandas as pd

from trading_strategies import *
from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *


def limit0_exit4(pattern) :
	wait = 4
	limit = 0
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit10_exit4(pattern) :
	wait = 4
	limit = 0.001
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit25_exit4(pattern) :
	wait = 4
	limit = 0.0025
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit50_exit4(pattern) :
	wait = 4
	limit = 0.005
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit75_exit4(pattern) :
	wait = 4
	limit = 0.0075
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit100_exit4(pattern) :
	wait = 4
	limit = 0.01
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit125_exit4(pattern) :
	wait = 4
	limit = 0.0125
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit150_exit4(pattern) :
	wait = 4
	limit = 0.015
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit175_exit4(pattern) :
	wait = 4
	limit = 0.0175
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit200_exit4(pattern) :
	wait = 4
	limit = 0.02
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break


			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit250_exit4(pattern) :
	wait = 4
	limit = 0.025
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit300_exit4(pattern) :
	wait = 4
	limit = 0.03
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit400_exit4(pattern) :
	wait = 4
	limit = 0.04
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit500_exit4(pattern) :
	wait = 4
	limit = 0.05
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit750_exit4(pattern) :
	wait = 4
	limit = 0.075
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit1000_exit4(pattern) :
	wait = 4
	limit = 0.10
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


def limit1250_exit4(pattern) :
	wait = 4
	limit = 0.125
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	rets_dict = {}
	rets_list = []

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')

		ticker_rets = []

		if len(indexes[ticker]) == 0 :
			continue

		count = 0
		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				count += 1
			except IndexError :
				continue

			for j in range(0, wait + 1) :

				if bullish is True and df['High'].iloc[i+length+j] > initial * (1 + limit) :
					final = initial * (1 + limit)
					break
				elif bullish is False and df['Low'].iloc[i+length+j] < initial * (1 - limit) :
					final = initial * (1 - limit)
					break

			if bullish : 
				ret = np.log(final / initial)
			else :
				ret = np.log(initial / final)

			ticker_rets.append(ret)

		rets_dict[ticker] = ticker_rets
		rets_list += ticker_rets

	return rets_dict, rets_list


all_limit_exit4 = [
	limit0_exit4,
	limit10_exit4,
	limit50_exit4,
	limit100_exit4,
	limit150_exit4,
	limit200_exit4,
	limit300_exit4,
	limit400_exit4,
	limit500_exit4,
	limit750_exit4,
	limit1000_exit4,
	limit1250_exit4
]
