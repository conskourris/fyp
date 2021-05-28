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

def negative_fit_2(df, index) :
    prices = []
    days = 2

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_3(df, index) :
    prices = []
    days = 3

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_4(df, index) :
    prices = []
    days = 4

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_5(df, index) :
    prices = []
    days = 5

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_6(df, index) :
    prices = []
    days = 6

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_7(df, index) :
    prices = []
    days = 7

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_8(df, index) :
    prices = []
    days = 8

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_9(df, index) :
    prices = []
    days = 9

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_10(df, index) :
    prices = []
    days = 10

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_11(df, index) :
    prices = []
    days = 11

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def negative_fit_12(df, index) :
    prices = []
    days = 12

    while days >= 0:
        prices.append(df['Close'].iloc[index-days])
        days -=1

    fit = np.polyfit(range(len(prices)), prices, 1)

    if fit[0] < 0 :
        return True
    
    return False 


def no_trend(df, index) :
    return True


negative_trends = [
                   no_trend,
                   negative_fit_2,
                   negative_fit_3,
                   negative_fit_4,
                   negative_fit_5,
                   negative_fit_6,
                   negative_fit_7,
                   negative_fit_8,
                   negative_fit_9,
                   negative_fit_10              
]