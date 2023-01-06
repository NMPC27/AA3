
chars = ["\n"," ",",",".","!","?",";",":","'","\"","(",")","[","]","{","}","<",">","/","\\",
        "|","@","#","$","%","^","&","*","-","+","=","_","~","`"
        "©"," ","‰","¨","´","¹","»","®","¢","ª","ˆ","¯","«","¼","©","¤"]
        


class SpaceSavingCount:

    def __init__(self, k):
        self.n=0
        self.t = dict() 
        self.k = k




    def count(self, data):

        while(data != ''):
            if data[0] in chars:
                data = data[1:]
                continue

            self.n += 1

            if data[0] in self.t:
                self.t[data[0]] += 1

            elif len(self.t) < self.k:
                # T <- T U {i} // add i to T basicamente adicionar ao dicionario
                self.t[data[0]] = 1

            else:
                self.t[min(self.t, key=self.t.get)] += 1
                self.t[data[0]] = self.t.pop(min(self.t, key=self.t.get))

            data = data[1:]




#k=3,5,10
k=10
files=["en","fr","gr"]

for file in files:
    avg_dict=dict()
    for i in range(10):
        f = open("books/"+file+".txt", "r")
        data = f.read().upper()

        counter = SpaceSavingCount(k)
        counter.count(data)
        f.close()

        avg_dict={k: avg_dict.get(k, 0) + counter.t.get(k, 0) for k in set(avg_dict) | set(counter.t)}

    avg_dict={k: v for k, v in sorted(avg_dict.items(), key=lambda item: item[1],reverse=True)}
    soma=sum(avg_dict.values())

    f = open("results/SpaceSavingCount_"+file+"_"+str(k)+".csv", "w")
    f.write("char,count,percentage")

    for key in avg_dict:
        f.write("\n"+key+","+str(avg_dict[key]/10)+","+str(avg_dict[key]/soma*100))
    f.close()