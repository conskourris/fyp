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

# all_strategies = []
# for strategies in all_limit_exit :
# 	all_strategies += strategies

# for pattern in all_patterns_final :
# 	get_most_profitable_strategies(all_strategies, pattern)

r, s = plot_patterns_on_strategies(all_patterns_final[:-2], best_strategies[:-2], True, True)

print(zip(r, s))

# for strategy in all_limit1250_exit :
# 	for pattern in all_patterns_final :
# 		save_pattern_trading_results(pattern, strategy)

# for strategies in all_limit_exit :
# 	plot_strategies_on_pattern(strategies, abandoned_baby_bullish)



plt.show()