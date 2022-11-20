from Token import Token
from TokenType import TokenType, ValueType, OperatorType

class LexicalAnalyzer:

    def __init__(self, fileName):
        self.tokens = []
        self.sourceCode = open(fileName)
        self.lineNumber = 1
        while(line := self.sourceCode.readline()):
            self.line = line
            self.processLine(self.line, self.lineNumber)
            self.lineNumber += 1
        self.tokens.append(Token(self.lineNumber, 1, "EOS", TokenType.EOS_TOK))
    
    def processLine(self, line, lineNumber):
        if (line == None or lineNumber < 1):
            raise Exception(f"Lexical Exception: Line = {line}LineNumber = {lineNumber}")
        index = 0
        count = 0
        index = self.skipWhiteSpace(line, index)
        isDisplay = False
        while (index < len(line)):
            count += 1
            lexeme = self.getLexeme(line, lineNumber, index)
            tokType = self.getTokenType(lexeme, lineNumber, index, isDisplay)
            if(tokType == None):
                break
            elif(tokType == TokenType.PRINT_TOK):
                line = self.splitOnComma()
                isDisplay = True
            elif(tokType == TokenType.L_PAREN_TOK):
                line = self.splitOnParen(tokType)
                lexeme = "("
            if(tokType == TokenType.DESC_TOK):
                self.skipDescription(lineNumber)
                index += len(lexeme)
                index = self.skipWhiteSpace(line, index)
                continue
            self.tokens.append(Token(lineNumber, index + 1, lexeme, tokType))
            
            index += len(lexeme)
            index = self.skipWhiteSpace(line, index)

    def getTokenType(self, lexeme, lineNumber, colNumber, isDisplay):
        if (lexeme == None or lineNumber < 1 or colNumber < 0):
            raise Exception("Lexical Exception")
        tokType = None
        if(lexeme[0].isalpha()):
            if(lexeme == "if"):
                tokType = TokenType.IF_TOK
            elif(lexeme == "function"):
                tokType = TokenType.FUNCTION_TOK
            elif(lexeme == "endfun"):
                tokType = TokenType.ENDFUN_TOK
            elif(lexeme == "else"):
                tokType = TokenType.ELSE_TOK
            elif(lexeme == "for"):
                tokType = TokenType.FOR_TOK
            elif(lexeme == "while"):
                tokType = TokenType.WHILE_TOK
            elif(lexeme == "display"):
                tokType = TokenType.PRINT_TOK
            elif(lexeme == "description"):
                tokType = TokenType.DESC_TOK
            elif(lexeme == "symbol"):
                tokType = TokenType.SYM_TOK
            elif(lexeme == "import"):
                tokType = TokenType.IMP_TOK
            elif(lexeme == "implementations"):
                tokType = TokenType.IMPLE_TOK
            elif(lexeme == "return"):
                tokType = TokenType.RETURN_TOK
            elif(lexeme == "type"):
                tokType = TokenType.TYPE_TOK
            elif(lexeme == "integer"):
                tokType = ValueType.INT_TOK
            elif(lexeme == "variables"):
                tokType = TokenType.VARS_TOK
            elif(lexeme == "is"):
                tokType = TokenType.IS_TOK
            elif(lexeme == "define"):
                tokType = TokenType.DEFINE_TOK
            elif(lexeme == "of"):
                tokType = TokenType.OF_TOK
            elif(lexeme == "type"):
                tokType = TokenType.TYPE_TOK
            elif(lexeme == "double"):
                tokType = ValueType.DOUBLE_TOK
            elif(lexeme == "set"):
                tokType = TokenType.SET_TOK
            elif(lexeme == "exit"):
                tokType = TokenType.EXIT_TOK
            elif(lexeme == "global"):
                tokType = TokenType.GLOB_TOK
            elif(lexeme == "declarations"):
                tokType = TokenType.DECL_TOK
            elif(lexeme == "unsigned"):
                tokType = TokenType.UNSIGN_TOK
            elif(lexeme == "short"):
                tokType = ValueType.SHORT_TOK
            elif(lexeme == "long"):
                tokType = ValueType.LONG_TOK
            elif(lexeme == "byte"):
                tokType = ValueType.BYTE_TOK
            elif(lexeme == "begin"):
                tokType = TokenType.BEGIN_TOK
            elif(lexeme == "band"):
                tokType = TokenType.BAND_TOK
            elif(lexeme == "bor"):
                tokType = TokenType.BOR_TOK
            elif(lexeme == "bxor"):
                tokType = TokenType.BXOR_TOK
            elif(lexeme == "negate"):
                tokType = TokenType.BNOT_TOK
            elif(lexeme == "lshift"):
                tokType = TokenType.L_SHIFT_TOK
            elif(lexeme == "rshift"):
                tokType = TokenType.R_SHIFT_TOK
            elif(len(self.tokens) > 1 and (self.tokens[-1].getTokType() in (TokenType.SYM_TOK, TokenType.DEFINE_TOK, TokenType.FUNCTION_TOK, TokenType.ENDFUN_TOK, TokenType.SET_TOK, TokenType.ASSIGN_TOK, OperatorType.BAND_TOK, OperatorType.BOR_TOK, OperatorType.BXOR_TOK, OperatorType.BNOT_TOK, TokenType.L_PAREN_TOK)) or isDisplay):
                if(self.isValidIdentifier(lexeme[0])):
                    tokType = TokenType.ID_TOK
                else:
                    raise Exception(f"invalid lexeme at row number {lineNumber  + 1} and column {colNumber + 1}, lexeme: {lexeme}")
            else:
                raise Exception(f"invalid lexeme at row number {lineNumber} and column {colNumber}, lexeme: {lexeme}, line: {self.line}")
        elif(lexeme[0].isdigit()):
            if(self.allDigits(lexeme)):
                tokType = ValueType.CONST_TOK
            elif(lexeme[-1] == 'h'):
                tokType = ValueType.HEX_TOK
            elif(lexeme.isdecimal()):
                tokType = ValueType.CONST_TOK
            else:
                raise Exception(f"invalid lexeme at row number {lineNumber  + 1} and column {colNumber + 1}, lexeme: {lexeme}")
        elif(lexeme == "+"):
            tokType = OperatorType.ADD_TOK
        elif(lexeme == "-"):
            tokType = OperatorType.SUB_TOK
        elif(lexeme == "*"):
            tokType = OperatorType.MUL_TOK
        elif(lexeme == "/"):
            tokType = OperatorType.DIV_TOK
        elif(lexeme == "\\"):
            tokType = OperatorType.REV_DIV_TOK
        elif(lexeme == "^"):
            tokType = OperatorType.EXP_TOK
        elif(lexeme == "%"):
            tokType = OperatorType.MOD_TOK
        elif(lexeme == "="):
            tokType = TokenType.ASSIGN_TOK
        elif(lexeme[0] == "("):
            tokType = TokenType.L_PAREN_TOK
        elif(lexeme[-1] == ")"):
            tokType = TokenType.R_PAREN_TOK
        elif(lexeme == ">="):
            tokType = OperatorType.GE_TOK
        elif(lexeme == ">"):
            tokType = OperatorType.GT_TOK
        elif(lexeme == "<="):
            tokType = OperatorType.LE_TOK
        elif(lexeme == "=="):
            tokType = OperatorType.EQ_TOK
        elif(lexeme == "!="):
            tokType = OperatorType.NE_TOK
        elif(lexeme == ":"):
            tokType = TokenType.COL_TOK
        elif(lexeme[0] == "\""):
            tokType = ValueType.STRING_TOK
        elif(lexeme[0:2] == "//"):
            self.skipLineComment(colNumber, lineNumber)
            return None
        else:
            raise Exception(f"invalid lexeme at row number {lineNumber  + 1} and column {colNumber + 1}, lexeme: {lexeme}")
        return tokType

    def allDigits(self, s):
        if(s == None):
            raise Exception("Lexical Exception")
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def getLexeme(self, line, lineNumber, index):
        if (line == None or lineNumber < 1 or index < 0):
            raise Exception("Lexical Exception")
        i = index
        if (line[i] == '\"'):
            i += 1
            while(i < len(line) and not line[i] == '\"'):
                i += 1
            return line[index:i+1]
        while(i < len(line) and not line[i].isspace()):
            i += 1
        return line[index:i]
    
    def skipWhiteSpace(self, line, index):
        if (line == None or index < 0):
            raise Exception("Lexical Exception")
        while (index < len(line) and line[index].isspace()):
            index += 1
        return index
    
    def skipDescription(self, lineNumber):
        while(line := self.sourceCode.readline()):
            lineNumber += 1
            index = 0
            index = self.skipWhiteSpace(line, index)
            lexeme = self.getLexeme(line, lineNumber, index)
            if(lexeme == "*/"):
                self.lineNumber = lineNumber
                return
    
    def skipLineComment(self, index, lineNumber):
        comment = self.line[index:-1]
        #self.tokens.append(Token(lineNumber + 1, index + 1, comment, TokenType.COMMENT_TOK))
        #self.sourceCode.readline()
        return

    def splitOnComma(self):
        line = self.line
        line = " ".join(line.split(", "))
        return line
    
    def splitOnParen(self, tokType):
        line = self.line
        if (tokType == TokenType.L_PAREN_TOK):
            line = line.replace("(", "( ")
            line = line.replace(")", " )")
        return line
    
    def getNextToken(self) -> Token:
        if not self.tokens:
            raise Exception("Lexical Exception")
        return self.tokens.pop(0)
    
    def getLookaheadToken(self) -> Token:
        if not self.tokens:
            raise Exception("Lexical Exception")
        return self.tokens[0]
    
    def isValidIdentifier(self, ch) -> bool:
        return ch.isalpha()
    
    def isValidType(self, type) -> bool:
        return type in ValueType

    def printLex(self):
        for i in self.tokens:
            print(f"The next token type is: {i.getTokType()}\tNext lexeme is: {i.getLexeme()}\tLine Number: {i.getRowNumber()}")