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
from pandas_datareader import data
import random
import pickle
import json

from trading_strategies import *
from patterns_final import *
from tools import *
from definitions.negative_fit import *
from definitions.negative_mav3 import *
from definitions.negative_mav4 import *
from definitions.negative_mav5 import *

font = {'size'   : 14}
matplotlib.rc('font', **font)


def save_evaluation_data() :

    start = dt.datetime(1990, 1, 1)
    end = dt.datetime(1999, 12, 31)

    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :

        try :
            df = data.DataReader(ticker, 'yahoo', start, end)
        except KeyError :
            pass

        df.to_csv(f'historical/{ticker}.csv')
        print(f'saved {ticker}')


def save_distributions() :
    rets, stds = [], []
    save_historical_data()
    for pattern, strategy in zip(all_patterns_final, best_strategies) :
        
      save_pattern_final_indexes(pattern)
      save_pattern_trading_results(pattern, strategy)

    rets, stds = plot_patterns_on_strategies(all_patterns_final, best_strategies, False)

    np.savez(f'evaluation_results/original_data_distributions_bear.npz', rets, stds)


    rets_eval, stds_eval = [], []
    save_evaluation_data()
    for pattern, strategy in zip(all_patterns_final, best_strategies) :
      save_pattern_final_indexes(pattern)
      save_pattern_trading_results(pattern, strategy)

    rets_eval, stds_eval = plot_patterns_on_strategies(all_patterns_final, best_strategies, False)


    np.savez(f'evaluation_results/evaluation_data_distributions_bear.npz', rets_eval, stds_eval)


