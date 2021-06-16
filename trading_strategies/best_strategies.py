import pandas as pd

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *


def index_limit750_exit6(pattern) :
	wait = 6
	limit = 0.075
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1250_exit9(pattern) :
	wait = 9
	limit = 0.1250
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit400_exit0(pattern) :
	wait = 0
	limit = 0.04
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1000_exit9(pattern) :
	wait = 9
	limit = 0.1
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit100_exit0(pattern) :
	wait = 0
	limit = 0.01
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit50_exit6(pattern) :
	wait = 6
	limit = 0.0050
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit750_exit1(pattern) :
	wait = 1
	limit = 0.075
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1250_exit8(pattern) :
	wait = 8
	limit = 0.1250
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1000_exit8(pattern) :
	wait = 8
	limit = 0.1
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit50_exit0(pattern) :
	wait = 0
	limit = 0.005
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1250_exit2(pattern) :
	wait = 2
	limit = 0.1250
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit0_exit1(pattern) :
	wait = 1
	limit = 0
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit0_exit6(pattern) :
	wait = 6
	limit = 0
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit500_exit8(pattern) :
	wait = 8
	limit = 0.05
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit500_exit7(pattern) :
	wait = 7
	limit = 0.05
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


def index_limit1250_exit7(pattern) :
	wait = 7
	limit = 0.125
	indexes = get_pattern_final_indexes(pattern)
	_, length, bullish  = pattern(get_info=True)

	utilised_indexes = {}

	for ticker in indexes :
		df = pd.read_csv(f'historical/{ticker}.csv')
		
		ticker_indexes = []

		if len(indexes[ticker]) == 0 :
			utilised_indexes[ticker] = []
			continue

		for i in indexes[ticker] :

			try :
				initial = df['Open'].iloc[i+length]
				final = df['Close'].iloc[i+length+wait]
				ticker_indexes.append(i)
			except IndexError :
				continue

		utilised_indexes[ticker] = ticker_indexes

	return utilised_indexes


index_strategies = [
	index_limit750_exit6,
	index_limit1250_exit9,
	index_limit400_exit0,
	index_limit1000_exit9,
	index_limit100_exit0,
	index_limit50_exit6,
	index_limit100_exit0,
	index_limit750_exit1,
	index_limit1250_exit9,
	index_limit750_exit1,
	index_limit1250_exit8,
	index_limit1250_exit8,
	index_limit1000_exit8,
	index_limit50_exit0,
	index_limit1250_exit2,
	index_limit0_exit1,
	index_limit0_exit6,
	index_limit50_exit0,
	index_limit500_exit8,
	index_limit500_exit7,
	index_limit400_exit0,
	index_limit1250_exit7
]