class Token:
    def __init__(self, rowNumber, colNumber, lexeme, tokType):
        if (rowNumber <= 0):
            raise Exception("invalid row number")
        if (colNumber <= 0):
            raise Exception("invalid column number")
        if (lexeme == ""):
            raise Exception("invalid lexeme")
        if not tokType:
            raise Exception(f"invalid token type: {tokType}, {lexeme}")
        self.rowNumber = rowNumber
        self.colNumber = colNumber
        self.lexeme = lexeme
        self.tokType = tokType
    
    def getRowNumber(self):
        return self.rowNumber
    def getColNumber(self):
        return self.colNumber
    def getLexeme(self):
        return self.lexeme
    def getTokType(self):
        return self.tokType