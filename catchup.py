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
from evaluation_tools import *
from definitions.negative_fit import *
from definitions.negative_mav3 import *
from definitions.negative_mav4 import *
from definitions.negative_mav5 import *

definition_results = [
	'ats_fit_results',
	'ats_mav3_results',
	'ats_mav4_reselts',
	'ats_mav5_results',
	'eb_fit_results',
	'eb_mav3_results',
	'eb_mav4_results',
	'eb_mav5_results',
	'fw_fit_results',
	'fw_mav3_results',
	'fw_mav4_results',
	'fw_mav5_results',
	'tbg_fit_results',
	'tbg_mav3_results',
	'tbg_mav4_results',
	'tbg_mav5_results',
]



# plot_result_data('tbg_fit_results', use_occ=False, best_fit=True, f=1)
# plot_result_data('tbg_fit_results', use_occ=True, best_fit=True, f=2)

plot_result_data('ats_fit_results', use_occ=False, best_fit=False, f=1)
plot_result_data('ats_fit_results', use_occ=True, best_fit=False, f=2)

# plot_result_data('tbg_fit_results', use_occ=False, best_fit=True, f=1)
# plot_result_data('tbg_mav3_results', use_occ=False, best_fit=True, f=2)
# plot_result_data('tbg_mav4_results', use_occ=False, best_fit=True, f=3)
# plot_result_data('tbg_mav5_results', use_occ=False, best_fit=True, f=4)

# plot_result_data('tbg_fit_results', use_occ=True, best_fit=True, f=1)
# plot_result_data('tbg_mav3_results', use_occ=True, best_fit=True, f=2)
# plot_result_data('tbg_mav4_results', use_occ=True, best_fit=True, f=3)
# plot_result_data('tbg_mav5_results', use_occ=True, best_fit=True, f=4)

plt.show()