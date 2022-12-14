from Arithmetic import BinaryExpression, BooleanExpression, Constant, Expression, Id, Operator, RelativeOperator
from Memory import Memory
from Program import Program
from Statement import Block, DefineStatement, ForStatement, IfStatement, PrintStatement, Statement, WhileStatement, Iter, AssignmentStatement
from Token import Token
from TokenType import TokenType
from LexicalAnalyzer import LexicalAnalyzer

class Parser:
    def __init__(self, filename):
        self.lex = LexicalAnalyzer(filename)
        self.memory = Memory()
    
    def parse(self) -> Program: #imports -> symbols -> global declarations -> implementations
        tok = self.lex.getNextToken()
        blks = []
        while(tok.getTokType() != TokenType.EOS_TOK):
            if (tok.getTokType() == TokenType.IMP_TOK):
                self.getImports()
            if (tok.getTokType() == TokenType.SYM_TOK):
                self.getSymbols()
            if (tok.getTokType() == TokenType.GLOB_TOK):
                self.getGlobalDeclarations()
            if (tok.getTokType() == TokenType.IMPLE_TOK):
                blks.append(self.getFunctions())
            tok = self.lex.getNextToken()
        print('no errors found\n\n')
        return Program(blks)
        
    def getImports(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.STRING_TOK)

    def getSymbols(self) -> Statement:
        var = self.createId()
        expr = self.getArithmeticExpression()
        
        return AssignmentStatement(var, expr)

    def getGlobalDeclarations(self) -> Block:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.DECL_TOK)
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.VARS_TOK):
            varsblk = self.getBlock()
        
        return varsblk
        
    def getBlock(self) -> Block:
        blk = Block()
        tok = self.lex.getLookaheadToken()
        while (self.isValidStartOfStatement(tok)):
            stmt = self.getStatement()
            blk.add(stmt)
            tok = self.lex.getLookaheadToken()
        
        return blk

    def getFunctions(self):
        blks = []
        tok = self.lex.getLookaheadToken()
        while (tok.getTokType() == TokenType.FUNCTION_TOK):
            blks.append(self.getFunction())
            tok = self.lex.getLookaheadToken()
        return blks

    def getFunction(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.FUNCTION_TOK)
        functionName = self.createId(TokenType.FUNCTION_TOK)
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.IS_TOK)
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.VARS_TOK):
            varsblk = self.getBlock()
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.BEGIN_TOK):
            funcblk = self.getBlock()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.EXIT_TOK)
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ENDFUN_TOK)
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ID_TOK)
        return [varsblk, funcblk]

    def getStatement(self) -> Statement:
        tok = self.lex.getLookaheadToken()
        if (tok.getTokType() == TokenType.IF_TOK):
            stmt = self.getIfStatement()
        elif (tok.getTokType() == TokenType.WHILE_TOK):
            stmt = self.getWhileStatement()
        elif (tok.getTokType() == TokenType.PRINT_TOK):
            stmt = self.getPrintStatement()
        elif (tok.getTokType() == TokenType.SET_TOK):
            stmt = self.getAssignmentStatement()
        elif (tok.getTokType() == TokenType.FOR_TOK):
            stmt = self.getForStatement()
        elif (tok.getTokType() == TokenType.DEFINE_TOK):
            stmt = self.getDefineStatement()
        else:
            raise Exception(f'Invalid Statement type: {tok.getTokType()}')

        return stmt
    
    def getDefineStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.DEFINE_TOK)
        var = self.createId(TokenType.DEFINE_TOK)
        var.setId(value = None, )
        return DefineStatement(var.getId(), tok, self.memory)

    def getAssignmentStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.SET_TOK)
        tok = self.lex.getNextToken()
        #var = Id(ch = tok.getLexeme(), mem = self.memory) #change to self.createId()
        var_name = tok.getLexeme()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr = self.getArithmeticExpression()
        return AssignmentStatement(var_name, expr, self.memory)

    def getPrintStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.PRINT_TOK)
        expr = []
        while(self.lex.getLookaheadToken().getTokType() in (TokenType.ID_TOK, TokenType.STRING_TOK)):
            expr.append(self.getArithmeticExpression())
        
        return PrintStatement(expr)

    def getForStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.FOR_TOK)
        var = self.createId()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr1 = self.getArithmeticExpression()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.COL_TOK)
        expr2 = self.getArithmeticExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        it = Iter(expr1, expr2)
        
        return ForStatement(var, it, blk)

    def getWhileStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.getBooleanExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        
        return WhileStatement(expr, blk)

    def getIfStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.IF_TOK)
        expr = self.getBooleanExpression()
        blk1 = self.getBlock()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ELSE_TOK)
        blk2 = self.getBlock()
        tok = self.lex.getNextToken()
        
        return IfStatement(expr, blk1, blk2)

    def isValidIdentifier(self, ch) -> bool:
        return ch.isalpha()

    def isValidStartOfStatement(self, tok : Token) -> bool:
        if (tok == None):
            raise Exception(f'There is literally nothing here')
        
        return tok.getTokType() in (TokenType.SET_TOK, TokenType.IF_TOK, TokenType.WHILE_TOK, TokenType.FOR_TOK, TokenType.PRINT_TOK, TokenType.DEFINE_TOK)
    
    def getArithmeticExpression(self) -> Expression:
        tok = self.lex.getLookaheadToken()
        if (tok.getTokType() == TokenType.ID_TOK):
            expr = self.createId(TokenType.PRINT_TOK)
        elif (tok.getTokType() in (TokenType.CONST_TOK, TokenType.STRING_TOK)):
            expr = self.getConstant()
        else:
            expr = self.getBinaryExpression()
        
        return expr
    
    def getBinaryExpression(self) -> Expression:
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.ADD_TOK):
            self.match(tok, TokenType.ADD_TOK)
            op = Operator.ADD_OP
        elif (tok.getTokType() == TokenType.SUB_TOK):
            self.match(tok, TokenType.SUB_TOK)
            op = Operator.SUB_OP
        elif (tok.getTokType() == TokenType.MUL_TOK):
            self.match(tok, TokenType.MUL_TOK)
            op = Operator.MUL_OP
        elif (tok.getTokType() == TokenType.DIV_TOK):
            self.match(tok, TokenType.DIV_TOK)
            op = Operator.DIV_OP
        elif (tok.getTokType() == TokenType.REV_DIV_TOK):
            self.match(tok, TokenType.REV_DIV_TOK)
            op = Operator.REV_DIV_OP
        elif (tok.getTokType() == TokenType.EXP_TOK):
            self.match(tok, TokenType.EXP_TOK)
            op = Operator.EXP_OP
        elif (tok.getTokType() == TokenType.MOD_TOK):
            self.match(tok, TokenType.MOD_TOK)
            op = Operator.MOD_OP
        else:
            raise Exception(f'Invalid BinaryExpression: {tok.getTokType()}')
        
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        
        return BinaryExpression(op, expr1, expr2)
        

    def getBooleanExpression(self) -> BooleanExpression:
        op = Operator
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.EQ_TOK):
            op = RelativeOperator.EQ_OP
        elif (tok.getTokType() == TokenType.NE_TOK):
            op = RelativeOperator.NE_OP
        elif (tok.getTokType() == TokenType.GT_TOK):
            op = RelativeOperator.GT_OP
        elif (tok.getTokType() == TokenType.GE_TOK):
            op = RelativeOperator.GE_OP
        elif (tok.getTokType() == TokenType.LT_TOK):
            op = RelativeOperator.LT_OP
        elif (tok.getTokType() == TokenType.LE_TOK):
            op = RelativeOperator.LE_OP
        else:
            raise Exception(f'Invalid BooleanExpression: {tok.getTokType()}') #TODO
        
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        
        return BooleanExpression(op, expr1, expr2)
        
    def createId(self, tokenType) -> Id:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ID_TOK)
        if (tokenType == TokenType.FUNCTION_TOK):
            name = tok.getLexeme()
            tok = self.lex.getNextToken()
            if (tok.getTokType() == TokenType.RETURN_TOK):
                tok = self.lex.getNextToken()
                self.match(tok, TokenType.TYPE_TOK)
                tok = self.lex.getNextToken()
                return Id(ch = name, mem = self.memory, type = tok.getTokType())
            else:
                return Id(ch = name, mem = self.memory, type = TokenType.NONE_TOK)
        elif(tokenType == TokenType.DEFINE_TOK):
            name = tok.getLexeme()
            tok = self.lex.getNextToken()
            self.match(tok, TokenType.OF_TOK)
            tok = self.lex.getNextToken()
            self.match(tok, TokenType.TYPE_TOK)
            tok = self.lex.getNextToken()
            return Id(ch = name, mem = self.memory, type = tok.getTokType())
        # elif(tokenType == TokenType.SET_TOK):
        #     name = tok.getLexeme()
        #     tok = self.lex.getNextToken()
        #     self.match(tok, TokenType.ASSIGN_TOK)
            
        
        elif(tokenType == TokenType.PRINT_TOK):
            return Id(ch = tok.getLexeme(), mem = self.memory) 
            pass #TODO make id for print statements
        else:
            return Id(ch = tok.getLexeme(), mem = self.memory, type = tokenType)

    def getConstant(self) -> Expression:
        tok = self.lex.getNextToken()
        # self.match(tok, TokenType.CONST_TOK)
        if (tok.getTokType() not in (TokenType.CONST_TOK, TokenType.STRING_TOK)):
            raise Exception(f'Invalid token type: {tok.getTokType()}')
        value = tok.getLexeme()
        type = tok.getTokType()
        
        return Constant(value, type)
    
    def getVars(self):
        pass

    def match(self, tok : Token, tokenType : TokenType) -> None:
        if (tok == None or tokenType == None):
            raise Exception('Parser Exception')
        if (tok.getTokType() != tokenType):
            self.lex.printLex()
            raise Exception(f'{tok.getTokType()} is not {tokenType}; Token: {tok.getLexeme()}')