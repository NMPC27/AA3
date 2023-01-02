from math import floor
from random import randint

class CsurosCounter():
    def __init__(self, d): # d >=2 
        self.x = 0
        self.m = 2**d

    def increment(self):
        t = floor(self.x/self.m)

        while t>0:
            if randint(0,1) == 1: 
                return self.x

        return self.x + 1
