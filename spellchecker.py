import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multilingue=md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        testo_pulito=replaceChars(txtIn.lower())
        campi=testo_pulito.split(" ")
        tempo_iniziale=time.time()
        lista=self._multilingue.searchWordDichotomic(campi,language)
        tempo_finale=time.time()
        for parola in lista:
            if parola.corretta==False:
                print(parola)
        print(f"Time elapsed {tempo_finale-tempo_iniziale}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text
