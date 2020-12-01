import numpy as np
import pandas as pd

#########################################################
# numpy使用
#########################################################
# 使用numpy创建数组
a = np.array([[1, 2], [3, 4]])
# print(a * 2)
# print(np.arange(5))  # [0 1 2 3 4]
# print(np.arange(5, 10))  # [5 6 7 8 9]
# print(np.arange(5, 10, 2))  # [5 7 9]

# print(np.random.randn(3))  # 生成有三个数的数组，每一个数符合正太分布

# print(np.arange(12).reshape(3, 4))  # 三行四列的数组

# print(np.random.randint(0, 10, (4, 4)))  # 零到四的随机数，四行四列的数组

#########################################################
# pandas使用
#########################################################
b = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'sore'], index=['A', 'B', 'C'])
print(b)
print(pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'], ))
print(pd.DataFrame.from_dict({'a': [1, 3, 5], 'b': [2, 4, 6]}, orient='index'))

c = np.arange(12).reshape(3, 4)
print(pd.DataFrame(c, index=['1', '2', '3'], columns=['A', 'B', 'C', 'D']))

d = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'core'], index=['A', 'B', 'C'])
d.index.name = '公司'

d.rename(index={'A': '万科', 'B': '百度', 'C': '阿里', }, columns={'date': '日期', 'core': '分数'},
         inplace=True)  # 如果不设置inplace就不会修改原有的object
d.reset_index(inplace=True)   # 重设索引
d.set_index('日期', inplace=True)  # 将日期设置为行索引
print(d)

#########################################################
# 文件读取和写入
#########################################################
