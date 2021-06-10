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

from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *
from trading_tools import *
from ml_tools import *

from definitions.positive_fit import *
from definitions.positive_mav3 import *
from definitions.positive_mav4 import *
from definitions.positive_mav5 import *
from definitions.negative_fit import *
from definitions.negative_mav3 import *
from definitions.negative_mav4 import *
from definitions.negative_mav5 import *
from definitions.tall_candle import *
from definitions.doji import *
from definitions.close_near_high import *
from definitions.close_near_low import *

from trading_strategies.exit_after import *
from trading_strategies.limit_exit0 import *
from trading_strategies.limit_exit1 import *
from trading_strategies.limit_exit2 import *
from trading_strategies.limit_exit3 import *
from trading_strategies.limit_exit4 import *
from trading_strategies.limit_exit5 import *
from trading_strategies.limit_exit6 import *
from trading_strategies.limit_exit7 import *
from trading_strategies.limit_exit8 import *
from trading_strategies.limit_exit9 import *

from trading_strategies.best_strategies import *

from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


pattern = last_engulfing_bottom
strategy = limit1250_exit9
index_strategy = index_limit1250_exit9
days_prior = 10

_, length, _ = pattern(get_info=True)
dimention = (length + days_prior)

# save_train_test_dicts(pattern, strategy, index_strategy, days_prior)

X_train_dict, X_test_dict, y_train_dict, y_test_dict = get_train_test_dicts(pattern, strategy, days_prior)

X_train = flatten_dict(X_train_dict)
X_train = np.array(X_train)

X_test = flatten_dict(X_test_dict)
X_test = np.array(X_test)


y_train_raw = flatten_dict(y_train_dict)
y_train = [(1 if x >= 0 else 0) for x in y_train_raw]
y_train = np.array(y_train)

y_test_raw = flatten_dict(y_test_dict)
y_test = [(1 if x >= 0 else 0) for x in y_test_raw]
y_test = np.array(y_test)

scaler = preprocessing.StandardScaler()
# scaler = preprocessing.MinMaxScaler(feature_range = (0, 1))
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.fit_transform(X_test)
# X_train_norm = X_train
# X_test_norm = X_test

X_train_norm = np.reshape(X_train_norm, (X_train_norm.shape[0], int(X_train_norm.shape[1]/5), 5))
X_test_norm = np.reshape(X_test_norm, (X_test_norm.shape[0], int(X_test_norm.shape[1]/5), 5))


model = Sequential()
# model.add(Dense(25, activation="relu", input_dim=dimention))
# model.add(Dense(5, activation="relu"))
model.add(LSTM(32, return_sequences=True, input_shape=(dimention, 5)))
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(128))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss = "binary_crossentropy",  optimizer = "adam", metrics = ['accuracy'])
# model.compile(loss = "mean_squared_error",  optimizer = "adam", metrics = ['mse'])
model.fit(X_train_norm, y_train, epochs=10, batch_size=64)


_, accuracy = model.evaluate(X_test_norm, y_test)
preds = model.predict_classes(X_test_norm)
print(preds)
print('Accuracy: %.2f' % (accuracy*100))

print(np.sum(y_test)/len(y_test))




plt.show()



