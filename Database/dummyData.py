import pandas as pd
s = pd.Series(list('abca'))
pd.get_dummies(s)
print(s)
