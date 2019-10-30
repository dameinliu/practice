import numpy as np
import pandas as pd

# dates = pd.date_range('20191101', periods=6)
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# df1.loc[dates[0]:dates[1], 'E'] = 1

# print(df)
# print('==========')
# print(df.mean(1))


# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# s1 = df.sub(s, axis='index')

# # print(df)
# print('==========')
# # print(df.apply(np.cumsum))
# print(0.245316-2.076216)
# print(0.245316-2.076216-0.977736)

### 分组
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.randn(8), 'D': np.random.randn(8)})

print(df)
print('==========')
print(df.groupby('A').sum())