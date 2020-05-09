import pandas as pd

data = pd.read_csv('test3.csv')
# data.groupby('City')
# test = data[data.duplicated(['City'], keep=False)]
# print(data.to_string())
# print(test.to_string())
# vec = data.groupby('City')[['Inmates Positive']].apply(lambda x: x.values.tolist())
# print(vec[0])
# print (type(vec))
# data = data.sort_values(by = 'Inmates Positive', ascending=True)
# print (data)
print(data['Inmates Positive'].max())