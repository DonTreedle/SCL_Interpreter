from Arithmetic import BinaryExpression, BooleanExpression, Constant, Expression, Id, Operator, RelativeOperator
from AssignmentStatement import AssignmentStatement
from Statement import ForStatement, IfStatement, PrintStatement, Statement, WhileStatement, Iter
from Token import Token
from TokenType import TokenType
from LexicalAnalyzer import LexicalAnalyzer
from Block import Block

class Parser:
    def __init__(self, filename):
        self.lex = LexicalAnalyzer(filename)
    
    def parse(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.FUNCTION_TOK)
        
    
    def getBlock(self) -> Block:
        blk = Block()
        tok = self.lex.getLookaheadToken()
        while (self.isValidStartOfStatement(tok)):
            stmt = self.getStatement()
            blk.add(stmt)
            tok = self.lex.getLookaheadToken()
        
        return blk
    
    def getStatement(self) -> Statement:
        stmt = Statement()
        tok = self.lex.getLookaheadToken()
        if (tok.getTokType() == TokenType.IF_TOK):
            stmt = self.getIfStatement()
        elif (tok.getTokType() == TokenType.WHILE_TOK):
            stmt = self.getWhileStatement()
        elif (tok.getTokType() == TokenType.PRINT_TOK):
            stmt = self.getPrintStatement()
        elif (tok.getTokType() == TokenType.ID_TOK):
            stmt = self.getAssignmentStatement()
        elif (tok.getTokType() == TokenType.FOR_TOK):
            stmt = self.getForStatement()
        else:
            raise Exception()

        return stmt
    
    def getAssignmentStatement(self) -> Statement:
        var = self.getId()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr = self.getArithmeticExpression()
        return AssignmentStatement(var, expr)

    def getPrintStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.PRINT_TOK)
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getArithmeticExpression()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        
        return PrintStatement(expr)

    def getForStatement(self) -> Statement:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.FOR_TOK)
        var = self.getId()
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

    def isValidStartOfStatement(self, tok : Token) -> bool:
        if (tok == None):
            raise Exception()
        
        return tok.getTokType() == TokenType.ID_TOK or tok.getTokType() == TokenType.IF_TOK or tok.getTokType() == TokenType.WHILE_TOK or tok.getTokType() == TokenType.FOR_TOK or tok.getTokType() == TokenType.PRINT_TOK
    
    def getArithmeticExpression(self) -> Expression:
        expr = Expression()
        tok = self.lex.getLookaheadToken()
        if (tok.getTokType() == TokenType.ID_TOK):
            expr = self.getId()
        elif (tok.getTokType() == TokenType.CONST_TOK):
            expr = self.getConstant()
        else:
            expr = self.getBinaryExpression()
        
        return expr
    
    def getBinaryExpression(self) -> Expression:
        op = Operator()
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
            raise Exception()
        
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
            raise Exception() #TODO
        
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        
        return BooleanExpression(op, expr1, expr2)
        
    def getId(self) -> Id:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ID_TOK)
        
        return Id(tok.getLexeme()[0])

    def getConstant(self) -> Expression:
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.CONST_TOK)
        value = (int)(tok.getLexeme())
        
        return Constant(value)

    def match(self, tok : Token, tokenType : TokenType) -> None:
        if (tok == None or tokenType == None):
            raise Exception('Parser Exception')
        if (tok.getTokType() != tokenType):
            raise Exception(f'')