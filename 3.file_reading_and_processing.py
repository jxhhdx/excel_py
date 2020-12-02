import pandas as pd
import numpy as np

# data.to_excel('d:\\example.xlsx', columns=['A列'],index=False)
# sheetname=0, encoding='utf-8'
data = pd.DataFrame(np.arange(1, 10).reshape(3, 3),
                    index=['r1', 'r2', 'r3'],
                    columns=['c1', 'c2', 'c3'])
data.to_excel('d:\\example.xlsx', )

print(pd.read_excel('d:\\example.xlsx', ))
# print(data[['c1']])
# print(data.iloc[1:3])
# print(data.head(1))
# print(data[['c1', 'c2']][0:2])
print(data[(data['c1']>1)&(data['c1']==4)])
print(data.sort_values(by='c2', ascending=False))
data['总计'] = data['c1']+data['c2']+data['c3']
data = data.drop(index=['r3'], columns=['c3'])
print(data)
