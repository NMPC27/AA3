


class SpaceSavingCount:

    def __init__(self, k):
        self.n=0
        self.t = dict() 
        self.k = k




    def count(self, data):

        while(data != ''):
            if data[0] == '\n' or data[0] == ' ':
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





k=10
files=["en","fr","gr"]

for file in files:
    f = open("books/"+file+".txt", "r")
    data = f.read().upper()

    counter = SpaceSavingCount(k)
    counter.count(data)
    print(counter.t)
    f.close()