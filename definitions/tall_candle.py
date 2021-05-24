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


def tall_100(df, index) :
	prices = []
	magnitude = 0.0100

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True

# this is the average candlesick height of all S&P100
def tall_119(df, index) :
	prices = []
	magnitude = 0.0100

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True

# this is the average candlestick hight of AAPL
def tall_145(df, index) :
	prices = []
	magnitude = 0.0145

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_150(df, index) :
	prices = []
	magnitude = 0.015

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_175(df, index) :
	prices = []
	magnitude = 0.0175

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_200(df, index) :
	prices = []
	magnitude = 0.02

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_225(df, index) :
	prices = []
	magnitude = 0.0225

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_250(df, index) :
	prices = []
	magnitude = 0.0250

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_275(df, index) :
	prices = []
	magnitude = 0.0275

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_300(df, index) :
	prices = []
	magnitude = 0.03

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_350(df, index) :
	prices = []
	magnitude = 0.0350

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_400(df, index) :
	prices = []
	magnitude = 0.04

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_450(df, index) :
	prices = []
	magnitude = 0.045

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True
	

def tall_500(df, index) :
	prices = []
	magnitude = 0.05

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_600(df, index) :
	prices = []
	magnitude = 0.060

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def tall_750(df, index) :
	prices = []
	magnitude = 0.075

	c = df['Close'].iloc[index]
	o = df['Open'].iloc[index]
	size = np.abs((c - o) / o)

	if size < magnitude :
		return False

	return True


def no_trend(df, index) :
    return True


tall_candles = [
	no_trend,
	tall_100,
	tall_119,
	tall_145,
	tall_150,
	tall_175,
	tall_200,
	tall_225,
	tall_250,
	tall_275,
	tall_300,
	tall_350,
	tall_400,
	tall_500,
	tall_600,
	tall_750
]
