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
from evaluate_findings import *
from evaluation_tools import *
from plotting_tools import *
from trading_tools import *

from definitions.positive_fit import *
from definitions.positive_mav3 import *
from definitions.positive_mav4 import *
from definitions.positive_mav5 import *
from definitions.negative_fit import *
from definitions.negative_mav3 import *
from definitions.negative_mav4 import *
from definitions.negative_mav5 import *
from definitions.tall_candle import *
from definitions.doji import *
from definitions.close_near_high import *
from definitions.close_near_low import *

from trading_strategies.best_strategies import *

from trading_strategies.exit_after import *
from trading_strategies.limit_exit0 import *
from trading_strategies.limit_exit1 import *
from trading_strategies.limit_exit2 import *
from trading_strategies.limit_exit3 import *
from trading_strategies.limit_exit4 import *
from trading_strategies.limit_exit5 import *
from trading_strategies.limit_exit6 import *
from trading_strategies.limit_exit7 import *
from trading_strategies.limit_exit8 import *
from trading_strategies.limit_exit9 import *

import trading_strategies.best_strategies as bs

all_limit_exit = [
	all_limit_exit0,
	all_limit_exit1,
	all_limit_exit2,
	all_limit_exit3,
	all_limit_exit4,
	all_limit_exit5,
	all_limit_exit6,
	all_limit_exit7,
	all_limit_exit8,
	all_limit_exit9
]

best_strategies = [
	limit750_exit6,
	limit1250_exit9,
	limit400_exit0,
	limit1000_exit9,
	limit100_exit0,
	limit50_exit6,
	limit100_exit0,
	limit750_exit1,
	limit1250_exit9,
	limit750_exit1,
	limit1250_exit8,
	limit1250_exit8,
	limit1000_exit8,
	limit50_exit0,
	limit1250_exit2,
	limit0_exit1,
	limit0_exit6,
	limit50_exit0,
	limit500_exit8,
	limit500_exit7,
	limit400_exit0,
	limit1250_exit7
]

best_bullish_strategies = [
	limit750_exit6,
	limit1250_exit9,
	limit1000_exit9,
	limit1250_exit9,
	limit1250_exit8,
	limit1250_exit8,
	limit1000_exit8,
	limit0_exit6,
	limit500_exit8,
	limit500_exit7,
	limit1250_exit7
]

best_bearish_strategies = [
	limit400_exit0,
	limit100_exit0,
	limit50_exit6,
	limit100_exit0,
	limit750_exit1,
	limit750_exit1,
	limit50_exit0,
	limit1250_exit2,
	limit0_exit1,
	limit50_exit0,
	limit400_exit0
]


plot_hist_trading_results(last_engulfing_bottom, exit_after_7)



# pattern = last_engulfing_bottom
# strategy = limit1250_exit9
# index_strategy = index_limit1250_exit9

# util_indexes = index_limit1250_exit9(pattern)

# returns_dict, returns = get_pattern_trading_results(pattern, strategy)
# returns_dict = returns_dict[()]

# for ticker in util_indexes :
# 	if len(returns_dict[ticker]) != len(util_indexes[ticker]) :
# 		print(f'Difference in {ticker}')



# results = [(a, b, c.__name__) for (a, b, c) in sorted(zip(rets, stds, all_patterns_final)) ]

# print(" \n ### All all patterns sorted by returns (no occ) ### \n ")

# for result in results :
# 	print(result)



plt.show()