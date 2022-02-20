import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

'''obj = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
python_dict = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
pd_series = pd.Series(python_dict)
pd_series.name = 'population'
pd_series.index.name = 'state'
print(obj)
print("---------")
print(obj.index)
print("---------")
print(obj['a'])
print("---------")
print(pd_series)
print("-----Next is DataFrame-----")'''
'''data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        }
frame = pd.DataFrame(data,
                     index=['line1', 'line2', 'line3', 'line4', 'line5', 'line6'],
                     columns=['state', 'year', 'pop'])
print(frame)
print("---------")
print(frame['year'])
print("---------")
print(frame.loc['line1'])'''
frame = pd.DataFrame(np.random.randn(4, 3),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
