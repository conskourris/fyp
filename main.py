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

from trading_strategies import *
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


names = []
occs = []


# for pattern in all_patterns_final :
# 	names.append(pattern.__name__)
# 	occs.append(get_pattern_final_occurrences(pattern))

# sort = [(a, x) for a, x in sorted(zip(occs, names))]

# for i in sort :
# 	print(i)



# save_pattern_final_indexes(engulfing_bearish)


# occs = get_pattern_final_indexes(three_outside_up)

# for ticker in occs :
# 	for i in occs[ticker] :
# 		plot_around_index(ticker, i, 10)

# 		plt.show()



for pattern in all_patterns_final :
	indexes = get_pattern_indexes(pattern)
	meta_evaluate(pattern, indexes)

plt.show()