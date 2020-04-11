class SearchEntryGenerator:
    def __init__(self,possibleSpacesInSearch,inputString):
        self.wordArray = inputString.split(' ')
        self.maxSpaces = possibleSpacesInSearch
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(len(self.wordArray)==1 and self.counter==1):
            raise StopIteration
        self.iterateCount()
        return self.buildString()
    def removeLeadingWord(self): self.wordArray = self.wordArray[1:]
    def buildString(self): return " ".join(self.wordArray[0:self.counter])
    def iterateCount(self):
        if self.counter < self.maxSpaces:
            self.counter += 1
        else:
            self.removeLeadingWord()
            self.counter = 1
        return

if __name__ == "__main__":
    inputString = "Luang Prabang right on the river not too busy and a great night"

    for i in SearchEntryGenerator(3,inputString):
        print(i)