from creating_class import Car, User

car_owner = Car(seats=6, doors=2,headlights=6)

user_1 = User(user_id='MY23', username='Markonikov')
user_2 = User(user_id='MY24', username='Marko')
user_1.follow(user_2)

print(car_owner)
print(car_owner.seats)
print(car_owner.doors)
print(car_owner.headlights)
print(' ')
print(user_1)
print(user_1.id)
print(user_1.username)
print(f'user 1 has {user_1.followers} follower(s)')
print(f'user 1 follows {user_1.following} person(s)')
print(f'user 2 has {user_2.followers} followers')
print(f'user 2 follows {user_2.following} person(s)')