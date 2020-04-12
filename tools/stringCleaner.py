goodCharacters = ' _-\'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

class stringCleaner:
    def removeSpecialCharacters(self,string):
        string = string.replace("\n"," ")
        return "".join([c for c in string if c in goodCharacters])

    def removeFillerWords(self,string):
        stringArray = string.split(" ")
        return " ".join(stringArray)

