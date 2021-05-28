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
from trading_strategies import *


def save_pattern_trading_results(pattern, strategy) :

	rets_dict, rets_list = strategy(pattern)

	if os.path.exists(f'trading_results/{strategy}') is False :
		os.mkdir(f'trading_results/{strategy.__name__}')

	np.savez(f'trading_results/{strategy.__name__}/{pattern.__name__}.npz', rets_dict, rets_list)
	print(f'saved {strategy.__name__} for {pattern.__name__}')


def get_pattern_trading_results(pattern, strategy) :

	results = np.load(f'trading_results/{strategy.__name__}/{pattern.__name__}.npz')
	print(f'got {strategy.__name__} for {pattern.__name__}')

	return results['arr_0'], results['arr_1']


def plot_hist_trading_results(pattern, strategy) :

	pass
