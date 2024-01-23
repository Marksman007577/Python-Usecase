import time, datetime

# Converting datetime Objects into Strings
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# Converting Strings into datetime Objects
dt = datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
print(dt)
dt1 = datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt1)
