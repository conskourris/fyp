import os
import bs4 as bs
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
import statistics
import requests


from patterns_final import *


def save_sp500_tickers():

    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)
    # saves list as a byte stream through pickle
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    return tickers


def save_historical_data() :

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2020, 12, 31)

    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :

        try :
            df = data.DataReader(ticker, 'yahoo', start, end)
        except KeyError :
            pass

        df.to_csv(f'historical/{ticker}.csv')
        print(f'saved {ticker}')


def run_snp(pattern, trading, days_forward):
    result = {}
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers:
        try:
            df = pd.read_csv(f'historical/{ticker}.csv')
        except:
            print(f'problem oppening {ticker}')
            continue

        indexes, pattern_length, _ = pattern(df)
        returns = trading(df, indexes, pattern_length, days_forward)
        result[f'{ticker}'] = returns

    return result


def run_ticker(ticker, pattern, strategy, days_forward):
	result = {}
	with open(f'sp100tickers.pickle', 'rb') as f:
		tickers = pickle.load(f)

	df = pd.read_csv(f'historical/{ticker}.csv')

	indexes, pattern_length, _ = pattern(df)
	returns = strategy(df, indexes, pattern_length, days_forward)
	result[f'{ticker}'] = returns

	return result


def save_pattern_indexes(pattern) :
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        indexes, _, _ = pattern(df)
        pattern_str = pattern.__name__
        np.save(f'patterns_indexes/{pattern_str}/{ticker}.npy', indexes)

        print(f'Saved {ticker} of {pattern_str}')


def save_pattern_final_indexes(pattern) :
    with open(f'sp100tickers.pickle', 'rb') as f:
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


def run_strategy_on_pattern(strategy, pattern, days_forward=0) :
    result = {}
    
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        _, pattern_length, _ = pattern(None, get_length=True)
        pattern_str = pattern.__name__
        indexes = np.load(f'patterns_indexes/{pattern_str}/{ticker}.npy')
        returns = strategy(df, indexes, pattern_length, days_forward)
        result[f'{ticker}'] = returns

    return result


def get_pattern_indexes(pattern) :
    indexes = {}
    pattern_str = pattern.__name__

    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            indexes[ticker] = np.load(f'patterns_indexes/{pattern_str}/{ticker}.npy')
        except FileNotFoundError:
            continue

    return indexes


def get_pattern_final_indexes(pattern) :
    indexes = {}
    pattern_str = pattern.__name__

    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            indexes[ticker] = np.load(f'patterns_final_indexes/{pattern_str}/{ticker}.npy')
        except FileNotFoundError:
            continue

    return indexes


def get_pattern_occurrences(pattern) :
    indexes = get_pattern_indexes(pattern)
    occs = 0
    for i in indexes :
        occs += len(indexes[i])
    
    return occs


def get_pattern_final_occurrences(pattern) :
    indexes = get_pattern_final_indexes(pattern)
    occs = 0
    for i in indexes :
        occs += len(indexes[i])
    
    return occs


def filter_pattern_trend(indexes, trend, delay=0) :
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        new_indexes = []

        for i in indexes[ticker] :
            if trend(df, i+delay) is True :
                new_indexes.append(i)

        indexes[ticker] = new_indexes

    return indexes


def average_close_high() :
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    ratios = []

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        for i in range(df.shape[0]) :
            close = df['Close'].iloc[i]
            high = df['High'].iloc[i]

            ratio = (abs(high-close) / close)
            ratios.append(ratio)


    average = statistics.mean(ratios)

    return average


def average_close_low() :
    with open(f'sp100tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    ratios = []

    for ticker in tickers :
        try :
            df = pd.read_csv(f'historical/{ticker}.csv')
        except :
            print(f'problem oppening {ticker}')
            continue

        for i in range(df.shape[0]) :
            close = df['Close'].iloc[i]
            low = df['Low'].iloc[i]

            ratio = (abs(low-close) / close)
            ratios.append(ratio)


    average = statistics.mean(ratios)

    return average


# def test_definitions(pattern, definitions, file_name) :
#     # generate and plot a pattern profile using specific definitions
#     rets, stds, occs = method_on_pattern(definitions, pattern, False, 0)
#     np.savez(f'definition_results/{file_name}.npz', rets, stds, occs)

#     # # plot saved return - risk plots of pattern profiles
#     plot_result_data(file_name, definitions, use_occ=False, best_fit=False, f=1)
#     plot_result_data(file_name, definitions, use_occ=True, best_fit=False, f=2)


