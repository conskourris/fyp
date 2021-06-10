import pandas as pd

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *


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


# best_strategies = [
# 	limit750_exit6,
# 	limit1250_exit9,
# 	limit400_exit0,
# 	limit1000_exit9,
# 	limit100_exit0,
# 	limit50_exit6,
# 	limit100_exit0,
# 	limit750_exit1,
# 	limit1250_exit9,
# 	limit750_exit1,
# 	limit1250_exit8,
# 	limit1250_exit8,
# 	limit1000_exit8,
# 	limit50_exit0,
# 	limit1250_exit2,
# 	limit0_exit1,
# 	limit0_exit6,
# 	limit50_exit0,
# 	limit500_exit8,
# 	limit500_exit7,
# 	limit400_exit0,
# 	limit1250_exit7
# ]