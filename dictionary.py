class Dictionary:
    def __init__(self):
        self.dizionario=[]

    def loadDictionary(self,path):
        infile = open(path, "r")
        line = infile.readline()
        while line != "":
            campi = line.rstrip()
            self.dizionario.append(campi)
            line = infile.readline()
        infile.close()

    def printAll(self):
        for parola in self.dizionario:
            print(parola)


    @property
    def dict(self):
        return self.dizionario
