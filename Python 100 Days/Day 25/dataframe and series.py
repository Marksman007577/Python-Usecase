import pandas as pd
import numpy as np
df = pd.read_csv('weather_data.csv')


# converting dataframe to list or dictionary
df_dict = df.to_dict()
df_list = df['temp'].to_list()

print(df_dict)
print(df_list)

temp_sum = df['temp'].sum()
temp_len = len(df['temp'])
avg_val = round(temp_sum/temp_len, 2)
print(temp_sum)
print(temp_len)
print(avg_val)

max_val = 0
min_val = -1

for num in df['temp']:
    if num > max_val:
        max_val = num


for num in df.temp:
    if num > 0 and num < min_val:
        min_val = num

print(f'Max Value: {max_val}')
print(f'Min Value: {min_val}')
print(df[df.temp == df.temp.max()])
print(' ')
print(df[df.condition == 'Sunny'])
