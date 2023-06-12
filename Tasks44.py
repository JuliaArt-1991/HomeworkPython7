import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.loc[data['whoAmI'] == 'robot', 'rob'] = '1'
data.loc[data['whoAmI'] != 'robot', 'rob'] = '0'
data.loc[data['whoAmI'] == 'human', 'hum'] = '1'
data.loc[data['whoAmI'] != 'human', 'hum'] = '0'
print(data)



