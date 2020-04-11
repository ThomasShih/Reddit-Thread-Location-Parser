from assets.verbs import verbList
from assets.nouns import nounList
from assets.adjectives import adjectivesList
from assets.manualInput import otherWords
fillerWords = verbList + nounList + adjectivesList + otherWords
goodCharacters = ' _-\'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

class stringCleaner:
    def removeSpecialCharacters(self,string):
        string = string.replace("\n"," ")
        return "".join([c for c in string if c in goodCharacters])

    def removeFillerWords(self,string):
        stringArray = string.split(" ")
        stringArray = [word for word in stringArray if word not in (fillerWords)]
        return " ".join(stringArray)

