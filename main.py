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



# for pattern in all_patterns_final :
# 	for strategy in all_limit_exit9 :
# 		save_pattern_trading_results(pattern, strategy)

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

all_limit100_exit = [
	limit100_exit0,
	limit100_exit1,
	limit100_exit2,
	limit100_exit3,
	limit100_exit4,
	limit100_exit5,
	limit100_exit6,
	limit100_exit7,
	limit100_exit8,
	limit100_exit9,
]

for pattern in all_patterns_final :
	for strategy in new_le9 :
		save_pattern_trading_results(pattern, strategy)

# for strategies in all_limit_exit :
# 		plot_strategies_on_pattern(strategies, abandoned_baby_bullish)


# for pattern in all_patterns_final :
# 	plot_strategies_on_pattern(all_limit_exit[5], pattern, True)

# plot_strategies_on_pattern(all_limit_exit[5], three_line_strike_bullish)
# plot_strategies_on_pattern(all_exit_after, three_line_strike_bullish)

# for strategy in all_limit_exit6 :
# 	plot_patterns_on_strategy(bullish_patterns, strategy)

os.system('say "run complete"')

# plt.show()