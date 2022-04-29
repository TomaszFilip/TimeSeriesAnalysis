# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:13:32 2022

@author: Tomasz Filip
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./IBM.csv', index_col=[0])
print(data.shape)
data.head()