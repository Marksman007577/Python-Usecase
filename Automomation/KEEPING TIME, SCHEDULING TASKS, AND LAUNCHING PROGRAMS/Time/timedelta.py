import datetime, time

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print(delta.total_seconds())
print(str(delta))