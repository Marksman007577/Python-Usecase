class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


class Car:
    def __init__(self, seats, doors, headlights):
        self.seats = seats
        self.doors = doors
        self.headlights = headlights

    def enter_race_mode(self):
        self.seats = 1

