import pandas as pd

s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(s)

# chọn dòng theo label
d = df.loc['a']

print(d)

# Output:
#
# một    1.0
# hai    1.0
# ba     9.0
# Name: a, dtype: float64