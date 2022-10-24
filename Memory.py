from LexicalAnalyzer import LexicalAnalyzer


class Memory():

    def __init__(self) -> None:
        self.mem = {}

    def store(self, name, value, *type):
        if (name in self.mem):
            self.mem[self.getIndex(name)] = (self.mem[self.getIndex(name)][0], value)
        else:
            self.mem[self.getIndex(name)] = (type, value)

    def fetch(self, name):
        return self.mem[self.getIndex(name)]

    def getIndex(self, name):
        if (not self.isValidIdentifier(name)):
            raise Exception(f'{name} is not a valid identifier')
        return name
    
    def isValidIdentifier(self, ch) -> bool:
        return ch.isalpha()

    def displayMemory(self):
        for i in range(26):
            print(f'{("A" + i)}: {self.mem[i]}')
        for i in range(26):
            print(f'{("a" + i)}: {self.mem[i + 26]}')