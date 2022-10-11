from Token import Token
from TokenType import TokenType
from LexicalAnalyzer import LexicalAnalyzer

class Parser:
    def __init__(self, filename):
        self.lex = LexicalAnalyzer(filename)
    
    def parse(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.FUNCTION_TOK)
        

    def match(self, tok, tokenType):
        if (tok == None or tokenType == None):
            raise Exception('Parser Exception')
        if (tok.getTokType() != tokenType):
            raise Exception(f'')