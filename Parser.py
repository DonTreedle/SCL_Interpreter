from LexicalAnalyzer import LexicalAnalyzer

class Parser:
    def __init__(self, filename):
        self.lex = LexicalAnalyzer(filename)
    
    def parse(self):
        tok = self.lex.getNextToken()
