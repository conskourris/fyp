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


def no_trend(df, index) :
    return True

# this is the average candlestick hight of AAPL
def doji_145(df, index) :
	prices = []
	magnitude = 0.0145

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True

	# this is the average candlesick height of all S&P100
def doji_119(df, index) :
	prices = []
	magnitude = 0.0119

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_100(df, index) :
	prices = []
	magnitude = 0.0100

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_80(df, index) :
	prices = []
	magnitude = 0.0080

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_60(df, index) :
	prices = []
	magnitude = 0.0060

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_40(df, index) :
	prices = []
	magnitude = 0.0040

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_20(df, index) :
	prices = []
	magnitude = 0.0020

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_15(df, index) :
	prices = []
	magnitude = 0.0015

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_10(df, index) :
	prices = []
	magnitude = 0.0010

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_5(df, index) :
	prices = []
	magnitude = 0.0005

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


def doji_1(df, index) :
	prices = []
	magnitude = 0.0001

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size > magnitude :
		return False

	return True


dojis = [
	no_trend,
	doji_145,
	doji_119,
	doji_100,
	doji_80,
	doji_60,
	doji_40,
	doji_20,
	doji_15,
	doji_10,
	doji_5,
	doji_1
]