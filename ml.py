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
from ml_tools import *

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

from trading_strategies.best_strategies import *

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras import models

font = {'size'   : 14}
matplotlib.rc('font', **font)

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


model = models.load_model(f'ml_models/two_black_gapping_20days_prior')

model.summary()


# considered_days = [0, 5, 10, 20]


# for days_prior in considered_days :
# 	p_rets, p_stds, ml_rets, ml_stds = [], [], [], []

# 	for pattern, strategy, index_strategy in zip(all_patterns_final[:-2], best_strategies[:-2], index_strategies[:-2]) :
		
# 		_, _, bullish = pattern(get_info=True)

# 		if bullish is False :
# 			results = np.load(f'ml_models/evaluation/{pattern.__name__}_{days_prior}days_dist.npz', allow_pickle=True)
			
# 			pattern_return = results['arr_0'][()]
# 			pattern_std = results['arr_1'][()]
# 			ml_return = results['arr_2'][()]
# 			ml_std = results['arr_3'][()]

# 			p_rets.append(pattern_return)
# 			p_stds.append(pattern_std)
# 			ml_rets.append(ml_return)
# 			ml_stds.append(ml_std)

# 	plt.figure(figsize=(10, 6))
# 	plt.title(f'Return against volatility for bearish original and ML data ({days_prior} days)')

# 	for i in range(len(p_rets)) :
# 		plt.plot(p_stds[i], p_rets[i], 'o', label=bearish_patterns[i].__name__)

# 	for i in range(len(p_rets)) :
# 		plt.plot(ml_stds[i], ml_rets[i], 'x')

# 	plt.xlabel('Standard Deviation')
# 	plt.ylabel('Log Return')
# 	plt.legend(loc='best')


plt.show()



