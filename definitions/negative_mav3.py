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

def negative_mav_3day_2(df, index) :
    days = 3
    windows = 2

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_3(df, index) :
    days = 3
    windows = 3

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_4(df, index) :
    days = 3
    windows = 4

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_4(df, index) :
    days = 3
    windows = 4

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_5(df, index) :
    days = 3
    windows = 5

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_6(df, index) :
    days = 3
    windows = 6

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_7(df, index) :
    days = 3
    windows = 7

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True


def negative_mav_3day_8(df, index) :
    days = 3
    windows = 8

    averages = df['Close'][index+1-days-windows:index+1].rolling(days).sum()

    if index < days + windows :
        return False

    for w in range(windows) :
        if averages[index-w] > averages[index-(w+1)] :
            return False

    return True

def no_trend(df, index) :
    return True

negative_mav3 = [
                    no_trend,
                     negative_mav_3day_2,
                     negative_mav_3day_3,
                     negative_mav_3day_4,
                     negative_mav_3day_5,
                     negative_mav_3day_6,
                     negative_mav_3day_7,
                     negative_mav_3day_8
]