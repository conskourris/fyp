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



# generate and plot a pattern profile using specific definitions
# rets, stds, occs = method_on_pattern(positive_trends, three_line_strike_bullish, True, 1)
# np.savez('definition_results/three_line_strike_bullish.npz', rets, stds, occs)

# # # plot saved return - risk plots of pattern profiles
plot_result_data('three_line_strike_bullish', positive_trends, use_occ=False, best_fit=False, f=1)
plot_result_data('three_line_strike_bullish', positive_trends, use_occ=True, best_fit=False, f=2)


plt.show()
