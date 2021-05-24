import numpy as np

from definitions.doji import doji_60
from definitions.close_near_high import c_high60
from definitions.close_near_low import c_low122

def no_definition(df, index) :
    return True

downtrend = no_definition
uptrend = no_definition
is_tall = no_definition
is_doji = doji_60
close_near_high = c_high60
close_near_low = c_low122

def two_black_gapping(df={}, get_length=False):
    # bear C
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # down
        if l_1 > h_2:
            if o_2 > o_3 and o_3 > c_2 and c_2 > c_3:
                if downtrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def above_the_stomach(df={}, get_length=False):
    # bull R
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # down
        if c_1 < o_1 and c_2 > o_2 :
            if o_2 > (c_1 + o_1) / 2 :
                if downtrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def belt_hold_bearish(df={}, get_length=False):
    # bear R
    pattern_length = 1
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]

        # up
        # implement close_near_low and tall_candle
        if c_1 < o_1 :
            if o_1 == h_1 :
                if uptrend(df, i) :
                    if close_near_low(df, i) :
                        if is_tall(df, i) :

                            indexes.append(i)

    return indexes, pattern_length


def belt_hold_bullish(df={}, get_length=False):
    # bull R
    pattern_length = 1
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]

        # down
        # implement close_near_high and tall_candle
        if c_1 > o_1 :
            if o_1 == l_1  :
                if downtrend(df, i) :
                    if close_near_high(df, i) :
                        if is_tall(df, i) :

                            indexes.append(i)

    return indexes, pattern_length


def doji_star(df={}, get_length=False) :
    # bear R
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # up
        # implement is_doji on second and tall_candle on first
        if c_1 > o_1 :
            if l_2 > h_1 :
                if h_1 - l_1 > h_2 - l_2 :
                    if uptrend(df, i) :
                        if is_tall(df, i) :
                            if is_doji(df, i+1) :

                                indexes.append(i)

    return indexes, pattern_length


def engulfing_bearish(df={}, get_length=False):
    # bear R
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # up
        if c_1 > o_1 and c_2 < o_2 :
            if o_2 > c_1 and c_2 < o_1 :
                if uptrend(df, i) :
                
                    indexes.append(i)

    return indexes, pattern_length


def last_engulfing_bottom(df={}, get_length=False) :
    # bull R (bear C)
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # down
        if c_1 > o_1 and c_2 < o_2 :
            if o_2 > c_1 and c_2 < o_1 :
                if downtrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def last_engulfing_top(df={}, get_length=False):
    # bear R (bull C)
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # up
        if c_1 < o_1 and c_2 > o_2 :
            if c_2 > o_1 and o_2 < c_1 :
                if uptrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def three_outside_down(df={}, get_length=False):
    # bear R
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # up
        if c_1 > o_1 and c_2 < o_2 and c_3 < o_3 :
            if o_2 > c_1 and c_2 < o_1 :
                if c_3 < c_2 :
                    if uptrend(df, i) :

                        indexes.append(i)

    return indexes, pattern_length


def three_outside_up(df={}, get_length=False) :
    # bull R
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # down
        if c_1 < o_1 and c_2 > o_2 and c_3 > o_3 :
            if c_3 > c_2 :
                if downtrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def falling_window(df={}, get_length=False) :
    # bear C
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)):

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # down
        if c_1 < o_1 and c_2 < o_2 :
            if h_2 < l_1 :
                if downtrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def rising_window(df={}, get_length=False) :
    # bull C
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        
        # up
        if c_1 > o_1 and c_2 > o_2 :
            if l_2 > h_1 :
                if uptrend(df, i) :

                    indexes.append(i)

    return indexes, pattern_length


def three_line_strike_bearish(df={}, get_length=False) :
    # bear C (bull R)
    pattern_length = 4
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]
        o_4, h_4, l_4, c_4 = df['Open'].iloc[i+3], df['High'].iloc[i+3], df['Low'].iloc[i+3], df['Close'].iloc[i+3]

        # down
        if c_1 < o_1 and c_2 < o_2 and c_3 < o_3 and c_4 > o_4 :
            if c_1 > c_2 and c_2 > c_3 :
                if o_4 < c_3 and c_4 > o_1 :
                    if downtrend(df, i) :

                        indexes.append(i)

    return indexes, pattern_length


def three_line_strike_bullish(df={}, get_length=False) :
    # bull C (bear R)
    pattern_length = 4
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]
        o_4, h_4, l_4, c_4 = df['Open'].iloc[i+3], df['High'].iloc[i+3], df['Low'].iloc[i+3], df['Close'].iloc[i+3]

        # up
        if c_1 > o_1 and c_2 > o_2 and c_3 > o_3 and c_4 < o_4 :
            if c_1 < c_2 and c_2 < c_3 :
                if o_4 > c_3 and c_4 < o_1 :
                    if uptrend(df, i) :

                        indexes.append(i)

    return indexes, pattern_length


def three_black_crows(df={}, get_length=False) :
    # bear R
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # up 
        # implement close near low on 2nd and 3rd
        if c_1 < o_1 and c_2 < o_2 and c_3 < o_3 :
            if c_1 <= o_2 and o_2 <= o_1 :
                if c_2 <= o_3 and o_3 <= o_2 :
                    if uptrend(df, i) :
                        if close_near_low(df, i+1) :
                            if close_near_low(df, i+2) :

                                indexes.append(i)

    return indexes, pattern_length


def evening_star(df={}, get_length=False) :
    # bear R
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # up
        # implement tall_candle on 1st and 3rd
        if c_1 > o_1 and c_3 < o_3 :
            if c_2 > c_1 and o_2 > c_1 and c_2 > c_3 and o_2 > c_3 :
                if c_3 < (c_1 + o_1)/2 :
                    if uptrend(df, i) :
                        if is_tall(df, i) :
                            if is_tall(df, i+2) :

                                indexes.append(i)

    return indexes, pattern_length


def abandoned_baby_bullish(df={}, get_length=False) :
    # bull R
    pattern_length = 3
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]
        o_3, h_3, l_3, c_3 = df['Open'].iloc[i+2], df['High'].iloc[i+2], df['Low'].iloc[i+2], df['Close'].iloc[i+2]

        # down
        # implement doji on 2nd
        if c_1 < o_1 and c_3 > o_3 :
            if h_2 < l_1 and h_2 < l_3 :
                if downtrend(df, i) :
                    if is_doji(df, i+1) :

                        indexes.append(i)

    return indexes, pattern_length


def dark_cloud_cover(df={}, get_length=False) :
    # bear R
    pattern_length = 2
    indexes = []

    if get_length is True :
        return [], pattern_length

    for i in range(df.shape[0]-(pattern_length-1)) :

        o_1, h_1, l_1, c_1 = df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]
        o_2, h_2, l_2, c_2 = df['Open'].iloc[i+1], df['High'].iloc[i+1], df['Low'].iloc[i+1], df['Close'].iloc[i+1]

        # down
        # implement tall on 1st
        if c_1 > o_1 and c_2 < o_2 :
            if o_2 > c_1 and c_2 < (o_1 + c_1)/2 :
                if downtrend(df, i) :
                    if is_tall(df, i) :
                
                        indexes.append(i)

    return indexes, pattern_length



def select_at_random(df={}, get_length=False):
    pattern_length = 0
    indexes = []

    if get_length is True :
        return [], pattern_length

    select = 0.01
    for i in range(df.shape[0]):

        val = np.random.uniform()

        if val <= select:
            indexes.append(i)

    return indexes, pattern_length


all_patterns_final = [
            two_black_gapping,
            above_the_stomach,
            belt_hold_bearish,
            belt_hold_bullish,
            doji_star,
            engulfing_bearish,
            last_engulfing_bottom,
            last_engulfing_top,
            three_outside_down,
            three_outside_up,
            falling_window,
            rising_window,
            three_line_strike_bearish,
            three_line_strike_bullish,
            three_black_crows,
            evening_star,
            abandoned_baby_bullish,
            dark_cloud_cover,
            select_at_random
]

