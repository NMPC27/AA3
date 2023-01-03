from math import floor
from random import randint

class CsurosCounter():
    def __init__(self, d): # d >=1
        self.m = 2**d
        self.dict=dict()

    # x é o valor do counter para determinada letra
    def increment(self,x):
        t = floor(x/self.m)

        while t>0:
            if randint(0,1) == 1: 
                return x

            t=t-1

        return x + 1

    def count(self, data):

        while(data != ''):
            if data[0] == '\n' or data[0] == ' ':
                data = data[1:]
                continue


            if data[0] in self.dict:
                self.dict[data[0]] = self.increment(self.dict[data[0]])
            else:
                self.dict[data[0]] = 1 # é na boa ficar assim pq o increment ia dar 1 obrigatoriamente

            data = data[1:]


d=14 # d >=1 , quanto maior o d mais exato é o resultado
files=["en","fr","gr"]

for file in files:
    f = open("books/"+file+".txt", "r")
    data = f.read().upper()

    counter = CsurosCounter(d)
    counter.count(data)

    sorted_dict={k: v for k, v in sorted(counter.dict.items(), key=lambda item: item[1])}
    print(sorted_dict)
    f.close()

