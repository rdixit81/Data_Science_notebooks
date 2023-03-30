# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:04:54 2021

@author: rajvardhan dixit
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2017, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head())
