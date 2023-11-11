import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('2018_Central_Park_Squirrel_Census.csv')
squirrel_color = df['Primary Fur Color']
squirrel_color = squirrel_color.dropna(how='all')

fur_color_dict = {}

for color in squirrel_color:
    fur_color_dict.setdefault(color, 0)
    fur_color_dict[color] += 1

header = ['Fur Color', 'Count']

fur_color_df = pd.DataFrame(fur_color_dict.items(), columns=header).sort_values(ascending=False, by='Count')
fur_color_df.to_csv('squirrel_count.csv', sep=',', index=True, encoding='utf-8')
