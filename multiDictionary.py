import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self._inglese=d.Dictionary()
        self._italiano=d.Dictionary()
        self._spagnolo=d.Dictionary()

        self._inglese.loadDictionary("resources/English.txt")
        self._italiano.loadDictionary("resources/Italian.txt")
        self._spagnolo.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language.lower()=="italian":
            print(self._italiano)
        elif language.lower()=="english":
            print(self._inglese)
        elif language.lower()=="spanish":
            print(self._spagnolo)
        else:
            print("Lingua errata")

    def searchWord(self, words, language):
        paroleerrate=[]
        if language.lower() == "italian":
            for parola in words:
                if not(self._italiano.dizionario.__contains__(parola)):
                    paroleerrate.append(rw.RichWord(parola,False))
                else:
                    paroleerrate.append(rw.RichWord(parola, True))
            return paroleerrate
        elif language.lower() == "english":
            for parola in words:
                if not(self._inglese.dizionario.__contains__(parola)):
                    paroleerrate.append(rw.RichWord(parola,False))
                else:
                    paroleerrate.append(rw.RichWord(parola,True))
            return paroleerrate
        elif language.lower() == "spanish":
            for parola in words:
                if not(self._spagnolo.dizionario.__contains__(parola)):
                    paroleerrate.append(rw.RichWord(parola,False))
                else:
                    paroleerrate.append(rw.RichWord(parola,True))
            return paroleerrate
        else:
            print("Lingua errata")

    def searchWordLinear(self,words, language):
        trovato=False
        paroleerrate = []
        if language.lower() == "italian":
            for parola in words:
                for i in range(len(self._italiano.dizionario)):
                    if self._italiano.dizionario[i]==parola:
                        trovato=True
                        break
                if trovato:
                    paroleerrate.append(rw.RichWord(parola, True))
                else:
                    paroleerrate.append(rw.RichWord(parola, False))
            return paroleerrate
        elif language.lower() == "english":
            for parola in words:
                for i in range(len(self._inglese.dizionario)):
                    if self._inglese.dizionario[i] == parola:
                        trovato = True
                        break
                if trovato:
                    paroleerrate.append(rw.RichWord(parola, True))
                else:
                    paroleerrate.append(rw.RichWord(parola, False))
            return paroleerrate
        elif language.lower() == "spanish":
            for parola in words:
                for i in range(len(self._spagnolo.dizionario)):
                    if self._spagnolo.dizionario[i]==parola:
                        trovato=True
                        break
                if trovato:
                    paroleerrate.append(rw.RichWord(parola, True))
                else:
                    paroleerrate.append(rw.RichWord(parola, False))
            return paroleerrate
        else:
            print("Lingua errata")
    def searchWordDichotomic(self,words,language):
        trovato=False
        paroleerrate=[]
        if language.lower() == "italian":
            for paroladacercare in words:
                Primo =1
                Ultimo=len(self._italiano.dizionario)
                while (Primo<=Ultimo and not(trovato)):
                    Centro=int((Primo+Ultimo)/2)
                    if (self._italiano.dizionario[Centro]==paroladacercare):
                        trovato=True
                    elif self._italiano.dizionario[Centro]<paroladacercare:
                        Primo=Centro+1
                    else:
                        Ultimo=Centro-1
                if trovato:
                    paroleerrate.append(rw.RichWord(paroladacercare, True))
                else:
                    paroleerrate.append(rw.RichWord(paroladacercare, False))
            return paroleerrate
        elif language.lower() == "english":
            for paroladacercare in words:
                Primo = 1
                Ultimo = len(self._inglese.dizionario)
                while (Primo <= Ultimo and not (trovato)):
                    Centro = int((Primo + Ultimo) / 2)
                    if (self._inglese.dizionario[Centro] == paroladacercare):
                        trovato = True
                    elif self._inglese.dizionario[Centro] < paroladacercare:
                        Primo = Centro + 1
                    else:
                        Ultimo = Centro - 1
                if trovato:
                    paroleerrate.append(rw.RichWord(paroladacercare, True))
                else:
                    paroleerrate.append(rw.RichWord(paroladacercare, False))
            return paroleerrate
        elif language.lower() == "spanish":
            for paroladacercare in words:
                Primo = 1
                Ultimo = len(self._spagnolo.dizionario)
                while (Primo <= Ultimo and not (trovato)):
                    Centro = int((Primo + Ultimo) / 2)
                    if (self._spagnolo.dizionario[Centro] == paroladacercare):
                        trovato = True
                    elif self._spagnolo.dizionario[Centro] < paroladacercare:
                        Primo = Centro + 1
                    else:
                        Ultimo = Centro - 1
                if trovato:
                    paroleerrate.append(rw.RichWord(paroladacercare, True))
                else:
                    paroleerrate.append(rw.RichWord(paroladacercare, False))
            return paroleerrate
        else:
            print("Lingua errata")

