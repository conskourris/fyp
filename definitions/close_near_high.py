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

# average abs(high - close) / close = 0.0119
def no_trend(df, index) :
    return True
    

def c_high140(df, index) :
	prices = []
	magnitude = 0.0140

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high119(df, index) :
	prices = []
	magnitude = 0.0119

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high100(df, index) :
	prices = []
	magnitude = 0.0100

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high80(df, index) :
	prices = []
	magnitude = 0.008

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high60(df, index) :
	prices = []
	magnitude = 0.006

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high40(df, index) :
	prices = []
	magnitude = 0.004

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high20(df, index) :
	prices = []
	magnitude = 0.002

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high15(df, index) :
	prices = []
	magnitude = 0.0015

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high10(df, index) :
	prices = []
	magnitude = 0.0010

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high5(df, index) :
	prices = []
	magnitude = 0.0005

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


def c_high1(df, index) :
	prices = []
	magnitude = 0.0001

	c = df['Close'].iloc[index]
	h = df['High'].iloc[index]
	size = np.abs((h - c) / c)

	if size > magnitude :
		return False

	return True


c_highs = [
	no_trend,
	c_high140,
	c_high119,
	c_high100,
	c_high80,
	c_high60,
	c_high40,
	c_high20,
	c_high15,
	c_high10,
	c_high5,
	c_high1
]