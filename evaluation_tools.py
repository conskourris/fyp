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
from patterns import *
from tools import *
from definitions.negative_fit import *
from definitions.negative_mav3 import *
from definitions.negative_mav4 import *
from definitions.negative_mav5 import *


def plot_hist(title, data, size):
    range = max(data) - min(data)
    plt.figure(figsize=(10,6), dpi=80)
    plt.title(title)
    plt.hist(data, bins=int(range/size))
    plt.xlabel('Return')
    plt.ylabel('Occurances')
    plt.show()

    mean = sum(data)/len(data)
    std = np.std(data)

    print('Mean: ', mean)
    print('S.D: ', std)
    print('Skewness: ', skew(data))
    print('Occurances: ', len(data))

    return mean, std


def method_on_pattern(method, pattern, bullish, delay=0) :
    rets = []
    stds = []
    occs = []
    fnum = 1

    for trend in method :
        print(f'### Findings for {trend.__name__} ###')
        indexes = get_pattern_indexes(pattern)
        indexes = filter_pattern_trend(indexes, trend, delay)

        o, h, l, c, hstd, lstd, occ = meta_evaluate(pattern, indexes)
        if bullish is True : 
            rets.append(h)
            stds.append(hstd)
        else :
            rets.append(l)
            stds.append(lstd)

        occs.append(occ)

    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.set_title(f'Average price changes in returns using different trends')
    ax1.axhline(y = 0, color = 'r', linestyle = '--')
    for i in range(len(method)) :
        ax1.plot(rets[i], 'o-', label=method[i].__name__)
    ax1.set_xlabel('Days after pattern')
    ax1.set_ylabel('Change')
    ax1.set_xticks(np.arange(0, 20, 1))
    ax1.legend(loc='best')

    x = stds
    y = np.abs(rets)

    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title('Return - Volatility plot for tbg best fit')
    for i, func in enumerate(method[:10]) :
        ax.plot(x[i], y[i]*occs[i], 'o', label=func.__name__)
    ax.set_xlabel('Standard Deviation')
    ax.set_ylabel('Change')
    ax.legend(loc='best')

    return rets, stds, occs


def plot_result_data(file, funcs, use_occ=False, best_fit=False, f=1) :
    tbg_fit_results = np.load(f'definition_results/{file}.npz')
    x = tbg_fit_results['arr_1']
    y = abs(tbg_fit_results['arr_0'])
    occs = tbg_fit_results['arr_2']

    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title(f'Return - Volatility plot for {file} (use_occs={use_occ})')
    for i, func in enumerate(funcs) :
        if use_occ is True :
            y[i] = np.multiply(y[i], occs[i])

        if best_fit is True :
            a, b, c = np.polyfit(x[i], y[i], 2)
            ax.plot(x[i], a*x[i]**2 + b*x[i] + c, label=funcs[i].__name__)
        else :
            ax.plot(x[i], y[i], 'o', label=funcs[i].__name__)
        
    ax.set_xlabel('Standard Deviation')
    ax.set_ylabel('Change')
    ax.legend(loc='best')


def meta_evaluate(pattern, indexes) :
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    _, pattern_length = pattern(None, get_length=True)
    pattern_str = pattern.__name__

    opens = []
    high = []
    high_std = []
    low = []
    low_std = []
    close = []

    for days_ahead in range(0, 21) :
        occurances = 0
        change = 0

        total_open = 0
        total_high = 0
        total_low = 0
        total_close = 0

        all_highs = []
        all_lows = []

        for ticker in tickers :
            try :
                df = pd.read_csv(f'historical/{ticker}.csv')
            except :
                continue

            for i in indexes[ticker] :
                try :
                    initial = df['Open'].iloc[i+pattern_length]
                    new_open = df['Open'].iloc[i+pattern_length+days_ahead]
                    new_high = df['High'].iloc[i+pattern_length+days_ahead]
                    new_low = df['Low'].iloc[i+pattern_length+days_ahead]
                    new_close = df['Close'].iloc[i+pattern_length+days_ahead]
                    occurances += 1

                except IndexError :
                    continue

                total_open += (new_open - initial) / initial
                total_high += (new_high - initial) / initial
                total_low += (new_low - initial) / initial
                total_close += (new_close - initial) / initial

                all_highs.append((new_high - initial) / initial)
                all_lows.append((new_low - initial) / initial)
        
        try :
            opens.append(total_open/occurances)
            high.append(total_high/occurances)
            low.append(total_low/occurances)
            close.append(total_close/occurances)

            high_std.append(np.std(all_highs))
            low_std.append(np.std(all_lows))

        except ZeroDivisionError :
            opens.append(0)
            high.append(0)
            low.append(0)
            close.append(0)

            low_std.append(0)

        

        print(f'{days_ahead}', end='-')
    
    print(f'Occurances: {occurances}')

    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.set_title(f'Average price changes in OHLC after {pattern_str} appears')
    
    ax2 = ax1.twinx()
    ax1.set_xticks(np.arange(0, 20, 1))

    ax1.axhline(y = 0, color = 'r', linestyle = '--') 
    ax1.plot(opens, 'o-', label='Open')
    ax1.plot(high, 'o-', label='High')
    ax1.plot(low, 'o-', label='Low')
    ax1.plot(close, 'o-', label='Clsoe')
    ax2.plot(low_std, 'kx', label='Low Std')

    ax1.set_xlabel('Days after pattern')
    ax1.set_ylabel('Change')
    ax2.set_ylabel('Standard Deviation')
    ax1.legend(loc='best')

    return opens, high, low, close, high_std, low_std, occurances

