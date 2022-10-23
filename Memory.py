from LexicalAnalyzer import LexicalAnalyzer


class Memory():

    def __init__(self) -> None:
        self.mem = []

    def fetch(self, ch):
        return self.mem[self.getIndex(ch)]
    
    def store(self, ch, value):
        self.mem[self.getIndex(ch)] = value

    def getIndex(self, ch):
        if (not LexicalAnalyzer.isValidIdentifier(ch)):
            raise Exception(f'{ch} is not a valid identifier')
        if (ch - 'A' < 26):
            return ch - 'A'
        else:
            return (ch - 'a') + 26
        
    def displayMemory(self):
        for i in range(26):
            print(f'{("A" + i)}: {self.mem[i]}')
        for i in range(26):
            print(f'{("a" + i)}: {self.mem[i + 26]}')