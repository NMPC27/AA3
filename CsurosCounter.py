from math import floor
from random import randint

chars = ["\n"," ",",",".","!","?",";",":","'","\"","(",")","[","]","{","}","<",">","/","\\",
        "|","@","#","$","%","^","&","*","-","+","=","_","~","`"
        "©"," ","‰","¨","´","¹","»","®","¢","ª","ˆ","¯","«","¼","©","¤"]


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
            if data[0] in chars:
                data = data[1:]
                continue


            if data[0] in self.dict:
                self.dict[data[0]] = self.increment(self.dict[data[0]])
            else:
                self.dict[data[0]] = 1 # é na boa ficar assim pq o increment ia dar 1 obrigatoriamente

            data = data[1:]


files=["en","fr","gr"]

avg_dict=dict()

for d in range(1,15): # d >=1 , quanto maior o d mais exato é o resultado
    print(d)
    for file in files:
        avg_dict=dict()
        for i in range(10):

            f = open("books/"+file+".txt", "r")
            data = f.read().upper()

            counter = CsurosCounter(d)
            counter.count(data)

            f.close()

            avg_dict={k: avg_dict.get(k, 0) + counter.dict.get(k, 0) for k in set(avg_dict) | set(counter.dict)}




        avg_dict={k: v for k, v in sorted(avg_dict.items(), key=lambda item: item[1],reverse=True)}
        soma=sum(avg_dict.values())

        f = open("results/CsurosCounter_"+file+"_"+str(d)+".csv", "w",encoding="utf-8")
        f.write("char,count,percentage")

        for key in avg_dict:
            f.write("\n"+key+","+str(avg_dict[key]/10)+","+str(avg_dict[key]/soma*100))
        f.close()


