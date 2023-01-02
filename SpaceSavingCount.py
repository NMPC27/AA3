


class SpaceSavingCount:

    def __init__(self, k):
        self.n=0
        self.t = dict() 
        self.k = k




    def count(self, data):

        while(data != []):
            self.n += 1

            if data[0] in self.t:
                self.t[data[0]] += 1

            elif len(self.t) < self.k:
                # T <- T U {i} // add i to T basicamente adicionar ao dicionario
                self.t[data[0]] = 1

            else:
                self.t[min(self.t, key=self.t.get)] += 1 # j=argminj T[j] // j is the least frequent element in T



    def count(self, data):

        while(data != []):
            self.n += 1

            if data[0] in self.t:
                self.t[data[0]] += 1

                if len(self.t) < self.k:
                    # T <- T U {i} // add i to T basicamente adicionar ao dicionario
                    self.t[data[0]] = 1

                else:
                    self.t[min(self.t, key=self.t.get)] += 1 # j=argminj T[j] // j is the least frequent element in T