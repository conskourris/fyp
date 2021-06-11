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


def save_evaluation_data_400() :

    start = dt.datetime(2016, 1, 1)
    end = dt.datetime(2020, 12, 31)

    with open(f'sp400tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :

        try :
            df = data.DataReader(ticker, 'yahoo', start, end)
        except KeyError :
            pass

        df.to_csv(f'historical/{ticker}.csv')
        print(f'saved {ticker}')


def save_pattern_final_indexes_400(pattern) :
    with open(f'sp400tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        indexes, _, _ = pattern(df)
        pattern_str = pattern.__name__
        if os.path.exists(f'patterns_final_indexes/{pattern_str}') is False :
            os.mkdir(f'patterns_final_indexes/{pattern_str}')
            
        np.save(f'patterns_final_indexes/{pattern_str}/{ticker}.npy', indexes)

        print(f'Saved {ticker} of {pattern_str}')


def save_distributions() :
    rets, stds = [], []
    save_historical_data()
    for pattern, strategy in zip(all_patterns_final, best_strategies) :
        
      save_pattern_final_indexes(pattern)
      save_pattern_trading_results(pattern, strategy)

    rets, stds = plot_patterns_on_strategies(all_patterns_final, best_strategies, False)

    np.savez(f'evaluation_results/original_data_distributions_bear.npz', rets, stds)


    rets_eval, stds_eval = [], []
    save_evaluation_data_400()
    for pattern, strategy in zip(all_patterns_final, best_strategies) :
      save_pattern_final_indexes(pattern)
      save_pattern_trading_results(pattern, strategy)

    rets_eval, stds_eval = plot_patterns_on_strategies(all_patterns_final, best_strategies, False)


    np.savez(f'evaluation_results/evaluation_data_distributions_bear.npz', rets_eval, stds_eval)


def save_distribution_400() :
    # rename sp400 to sp100 pickle
    rets_eval, stds_eval = [], []
    for pattern, strategy in zip(all_patterns_final, best_strategies) :
      save_pattern_final_indexes(pattern)
      save_pattern_trading_results(pattern, strategy)

    rets_eval, stds_eval = plot_patterns_on_strategies(all_patterns_final, best_strategies, False)


    np.savez(f'evaluation_results/evaluation400_data_distributions_bear.npz', rets_eval, stds_eval)


def plot_saved_distributions() :
    original = np.load(f'evaluation_results/original_data_distributions_bear_occ.npz', allow_pickle=True)
    rets = original['arr_0']
    stds = original['arr_1']

    evaluation = np.load(f'evaluation_results/evaluation_data_distributions_bear_occ.npz', allow_pickle=True)
    rets_eval = evaluation['arr_0']
    stds_eval = evaluation['arr_1']

    plt.figure(figsize=(10, 6))
    plt.title(f'Return against volatility for bearish original and evaluation data')

    for i in range(len(rets[:-1])) :
        plt.plot(stds[i], rets[i], 'o', label=bullish_patterns[i].__name__)

    for i in range(len(rets_eval[:-1])) :
        plt.plot(stds_eval[i], rets_eval[i], 'x')

    plt.xlabel('Standard Deviation')
    plt.ylabel('Log Return')
    plt.legend(loc='best')


def save_sp400() :
    with open(f'sp100tickers.pickle', 'rb') as f:
        sp100 = pickle.load(f)

    with open(f'sp500tickers.pickle', 'rb') as f:
        sp500 = pickle.load(f)

    sp400 = []
    for t in sp500 :
        if t not in sp100 :
            sp400.append(t)

    with open("sp100tickers.pickle", "wb") as f:
        pickle.dump(sp400, f)


def compare_to_random() :
    rets, stds = [], []
    rets_rand, stds_rand = [], []
    occs = []
    z_scores = []

    for pattern, strategy in zip(bearish_patterns, best_bearish_strategies) :

        _, _, bullish = pattern(get_info=True)

        ret, std, occ = get_distribution_metrics(pattern, strategy)
        if bullish is True :
            ret_rand, std_rand, _ = get_distribution_metrics(random_bullish, strategy)
        else :
            ret_rand, std_rand, _ = get_distribution_metrics(random_bearish, strategy)

        rets.append(ret)
        stds.append(std)
        occs.append(occ)
        print(occ)
        rets_rand.append(ret_rand)
        stds_rand.append(std_rand)

        z = np.abs(ret - ret_rand) / np.sqrt(std**2 + std_rand**2)
        z_scores.append(z)

    plt.figure(figsize=(10, 6))
    plt.title(f'Return against volatility for bearish patterns and random selection')

    for i in range(len(rets[:-1])) :
        plt.plot(stds[i], rets[i], 'o', label=bearish_patterns[i].__name__)

    for i in range(len(rets_rand[:-1])) :
        plt.plot(stds_rand[i], rets_rand[i], 'x')

    plt.xlabel('Standard Deviation')
    plt.ylabel('Log Return')
    plt.legend(loc='best')

    results = [(a, b, c.__name__) for (a, b, c) in sorted(zip(z_scores, stds, bearish_patterns))]
    for r in results :
        print(r)

