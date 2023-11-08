import pandas as pd
import csv

# with pandas
df = pd.read_csv('weather_data.csv')
print(df)
print(df.nunique())
print(df.info())

temp_list = df['temp']
print(temp_list)


# with csv
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)

    temperature = []
    day_week = []
    week_condition = []

    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))

    for row in data:
        if row[0] != 'day':
            day_week.append(row[0])

    for row in data:
        if row[2] != 'condition':
            week_condition.append(row[2])

print(temperature)
print(day_week)
print(week_condition)
print(type(df))
