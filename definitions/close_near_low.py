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

# average abs(high - close) / close = 0.0122
def no_trend(df, index) :
    return True
    

def c_low140(df, index) :
	prices = []
	magnitude = 0.0140

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True

def c_low122(df, index) :
	prices = []
	magnitude = 0.0122

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low100(df, index) :
	prices = []
	magnitude = 0.0100

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low80(df, index) :
	prices = []
	magnitude = 0.008

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low60(df, index) :
	prices = []
	magnitude = 0.006

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low40(df, index) :
	prices = []
	magnitude = 0.004

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low20(df, index) :
	prices = []
	magnitude = 0.002

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low15(df, index) :
	prices = []
	magnitude = 0.0015

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low10(df, index) :
	prices = []
	magnitude = 0.0010

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low5(df, index) :
	prices = []
	magnitude = 0.0005

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


def c_low1(df, index) :
	prices = []
	magnitude = 0.0001

	c = df['Close'].iloc[index]
	l = df['Low'].iloc[index]
	size = np.abs((l - c) / c)

	if size > magnitude :
		return False

	return True


c_lows = [
	no_trend,
	c_low140,
	c_low122,
	c_low100,
	c_low80,
	c_low60,
	c_low40,
	c_low20,
	c_low15,
	c_low10,
	c_low5,
	c_low1
]
