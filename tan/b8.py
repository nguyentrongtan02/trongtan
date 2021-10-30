import pandas as pd

data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
ser = pd.Series(data,index=['a','c','b','d','e','f'])

print(ser[-3:])

# Output:
#
# d     2.0
# e     NaN
# f    10.0
# dtype: float64