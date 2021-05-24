from trading_strategies import *
from patterns_final import *
from tools import *
from evaluation_tools import *
from plotting_tools import *


def sell_after_1(pattern) :
	indexes = get_pattern_indexes(pattern)

	for ticker in indexes :
		for index in indexes[ticker] :

			
