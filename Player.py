import random

class Player:
    def __init__(self, username):
        self._username = username
        self._id = random.randint(0, 999999)