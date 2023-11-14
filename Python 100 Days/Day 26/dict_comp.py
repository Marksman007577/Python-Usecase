# dictionary comprehension
import random as rnd

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_dic = {k: rnd.randint(1, 100) for k in names}
passed_students = {k: v for (k, v) in student_dic.items() if v >= 60}

# dictionary comprehension with setdefault
text = input('Enter text here:').split()
airspeed_vel = {k: len(k) for k in text}

# dictionary comprehension with another dictionary
weather_centigrade = {
    'Monday': 4,
    'Tuesday': 5,
    'Wednesday': 10,
    'Thursday': 11,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}

weather_fahrenheit = {day: round(temp * (9/5) + 32, 2) for day, temp in weather_centigrade.items()}

# results
print(student_dic)
print(passed_students)
print(text)
print(len(text))
print(airspeed_vel)
print(weather_fahrenheit)
