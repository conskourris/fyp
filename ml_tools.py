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

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras import models

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *
from trading_tools import *

from trading_strategies.best_strategies import *

# from keras.models import Sequential
from sklearn.model_selection import train_test_split

font = {'size'   : 14}
matplotlib.rc('font', **font)


def save_train_test_dicts(pattern, strategy, index_strategy, days_prior) :

	indexes = index_strategy(pattern)

	with open(f'sp100tickers.pickle', 'rb') as f:
		tickers = pickle.load(f)

	returns_dict, returns = get_pattern_trading_results(pattern, strategy)
	returns_dict = returns_dict[()]

	x_train_dict, x_test_dict = {}, {} 
	y_train_dict, y_test_dict = {}, {}

	_, pattern_length, _ = pattern(get_info=True)

	for ticker in tickers :
		x_ticker = []
		y_ticker = []
		try :
			df = pd.read_csv(f'historical/{ticker}.csv')
		except :
			continue

		for n, i in enumerate(indexes[ticker]) :

			occurrence_data = []

			ref = df['Open'].iloc[i]
			occ_ref = df['Volume'].iloc[i]

			for x in range(days_prior+pattern_length) :
				occurrence_data.append(df['Open'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['High'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Low'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Close'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Volume'].iloc[i-days_prior+x]/occ_ref)

			x_ticker.append(occurrence_data)
			y_ticker.append(returns_dict[ticker][n])

		x_ticker = np.array(x_ticker)
		y_ticker = np.array(y_ticker)

		x_train, x_test, y_train, y_test = train_test_split(x_ticker, y_ticker, test_size=0.3, random_state=42)

		x_train_dict[ticker] = x_train
		x_test_dict[ticker] = x_test
		y_train_dict[ticker] = y_train
		y_test_dict[ticker] = y_test

	if os.path.exists(f'train_test_results/{pattern.__name__}') is False :
		os.mkdir(f'train_test_results/{pattern.__name__}')

	np.savez(f'train_test_results/{pattern.__name__}/{days_prior}days.npz', x_train_dict, x_test_dict, y_train_dict, y_test_dict)

	return x_train_dict, x_test_dict, y_train_dict, y_test_dict


def save_train_test_data(pattern, strategy, index_strategy, days_prior) :

	indexes = index_strategy(pattern)

	with open(f'sp100tickers.pickle', 'rb') as f:
		tickers = pickle.load(f)

	returns_dict, returns = get_pattern_trading_results(pattern, strategy)
	returns_dict = returns_dict[()]

	x_train_dict, x_test_dict = {}, {} 
	y_train_dict, y_test_dict = {}, {}

	_, pattern_length, _ = pattern(get_info=True)

	x_ticker = []
	y_ticker = []

	for ticker in tickers :
		
		try :
			df = pd.read_csv(f'historical/{ticker}.csv')
		except :
			continue
		for n, i in enumerate(indexes[ticker]) :

			occurrence_data = []

			ref = df['Open'].iloc[i]
			occ_ref = df['Volume'].iloc[i]

			for x in range(days_prior+pattern_length) :
				occurrence_data.append(df['Open'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['High'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Low'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Close'].iloc[i-days_prior+x]/ref)
				occurrence_data.append(df['Volume'].iloc[i-days_prior+x]/occ_ref)

			x_ticker.append(occurrence_data)
			y_ticker.append(returns_dict[ticker][n])

	x_ticker = np.array(x_ticker)
	y_ticker = np.array(y_ticker)

	x_train, x_test, y_train, y_test = train_test_split(x_ticker, y_ticker, test_size=0.3, random_state=42)

	if os.path.exists(f'train_test_results/{pattern.__name__}') is False :
		os.mkdir(f'train_test_results/{pattern.__name__}')

	np.savez(f'train_test_results/{pattern.__name__}/{days_prior}days.npz', x_train, x_test, y_train, y_test)

	return x_train, x_test, y_train, y_test


def get_train_test_dicts(pattern, strategy, days_prior) :

	results = np.load(f'train_test_results/{pattern.__name__}/{days_prior}days.npz', allow_pickle=True)
	print(f'got {strategy.__name__} for {pattern.__name__}')

	x_train_dict = results['arr_0'][()]
	x_test_dict = results['arr_1'][()]
	y_train_dict = results['arr_2'][()]
	y_test_dict = results['arr_3'][()]

	return x_train_dict, x_test_dict, y_train_dict, y_test_dict


def flatten_dict(dictionary) :
	flat = []
	for k in dictionary :
		for l in dictionary[k] :
			flat.append(l)

	return flat


def get_train_test_data(pattern, strategy, days_prior) :
	X_train, X_test, y_train_raw, y_test_raw = get_train_test_dicts(pattern, strategy, days_prior)

	# X_train = flatten_dict(X_train_dict)
	X_train = np.array(X_train)

	# X_test = flatten_dict(X_test_dict)
	X_test = np.array(X_test)

	# y_train_raw = flatten_dict(y_train_dict)
	y_train = [(1 if x >= 0 else 0) for x in y_train_raw]
	y_train = np.array(y_train)

	# y_test_raw = flatten_dict(y_test_dict)
	y_test = [(1 if x >= 0 else 0) for x in y_test_raw]
	y_test = np.array(y_test)


	scaler = preprocessing.StandardScaler()
	# scaler = preprocessing.MinMaxScaler(feature_range = (0, 1))
	X_train_norm = scaler.fit_transform(X_train)
	X_test_norm = scaler.fit_transform(X_test)

	X_train_norm = np.reshape(X_train_norm, (X_train_norm.shape[0], int(X_train_norm.shape[1]/5), 5))
	X_test_norm = np.reshape(X_test_norm, (X_test_norm.shape[0], int(X_test_norm.shape[1]/5), 5))

	return X_train_norm, X_test_norm, y_train, y_test


def save_lstm_model(pattern, strategy, days_prior) :

	_, length, _ = pattern(get_info=True)
	dimention = (length + days_prior)

	X_train_norm, X_test_norm, y_train, y_test = get_train_test_data(pattern, strategy, days_prior)

	model = Sequential()

	model.add(LSTM(256, return_sequences=True, input_shape=(dimention, 5)))
	model.add(LSTM(16))
	model.add(Dense(1, activation="sigmoid"))

	model.compile(loss = "binary_crossentropy",  optimizer = "adam", metrics = ['accuracy'])
	# model.compile(loss = "mean_squared_error",  optimizer = "adam", metrics = ['mse'])
	model.fit(X_train_norm, y_train, epochs=2, batch_size=64)


	_, accuracy = model.evaluate(X_test_norm, y_test)
	preds = model.predict_classes(X_test_norm)

	print(f'Model for {pattern}')
	print('Accuracy: %.2f' % (accuracy*100))

	print(np.sum(y_test)/len(y_test))

	model.save(f'ml_models/{pattern.__name__}_{days_prior}days_prior')

	return model


def test_lstm_model(pattern, strategy, days_prior) :
	
	model = models.load_model(f'ml_models/{pattern.__name__}_{days_prior}days_prior')

	_, X_test_norm, _, y_test = get_train_test_data(pattern, strategy, days_prior)

	_, accuracy = model.evaluate(X_test_norm, y_test)
	preds = model.predict_classes(X_test_norm)

	print(f'Model for {pattern.__name__}')
	print(f'Accuracy: {accuracy}')

	profitability = np.sum(y_test)/len(y_test)

	print(profitability)

	return preds, accuracy, profitability


def save_ml_evaluations() :
	considered_days = [0, 5, 10, 20]

	preds, label, accs, profs = [], [], [], []

	for pattern, strategy, index_strategy in zip(all_patterns_final[:-2], best_strategies[:-2], index_strategies[:-2]) :
		for days_prior in considered_days :
			pred, acc, prof = test_lstm_model(pattern, strategy, days_prior)
			label.append(f'{pattern.__name__} - Days: {days_prior}')
			preds.append(pred)
			accs.append(acc)
			profs.append(prof)


	for a, b, c in zip(label, accs, profs) :
		print(f'{a} - Acc: {b} - Profs: {c}')

	np.savez(f'ml_models/evaluation/{pattern.__name__}_{days_prior}days_prior.npz', preds, accs, profs)


def save_ml_performances() :
	considered_days = [0, 5, 10, 20]

	results = np.load(f'ml_models/evaluation/pattern_ml_evaluation_results.npz', allow_pickle=True)

	preds = results['arr_0'][()]
	accs = results['arr_1'][()]
	profs = results['arr_2'][()]


	counter = 0
	for pattern, strategy, index_strategy in zip(all_patterns_final[:-2], best_strategies[:-2], index_strategies[:-2]) :
		for days_prior in considered_days :
			_, _, _, returns = get_train_test_dicts(pattern, strategy, days_prior)

			pattern_return = np.sum(returns)
			pattern_std = np.std(returns)

			ml_returns = []
			for p, r in zip(preds[counter], returns) :
				if p == 1 :
					ml_returns.append(r)

			ml_return = np.sum(ml_returns)
			ml_std = np.std(ml_returns)

			print(pattern_return, ml_return)

			np.savez(f'ml_models/evaluation/{pattern.__name__}_{days_prior}days_dist.npz', pattern_return, pattern_std, ml_return, ml_std)
			counter += 1