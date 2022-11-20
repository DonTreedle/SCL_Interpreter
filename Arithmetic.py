from abc import ABC, abstractmethod
from enum import Enum
from LexicalAnalyzer import LexicalAnalyzer
from Memory import Memory
from TokenType import TokenType, ValueType

class Operator(Enum):
    ADD_OP = 1          #+
    MUL_OP = 2          #*
    SUB_OP = 3          #-
    DIV_OP = 4          #/
    REV_DIV_OP = 5      #\\
    EXP_OP = 6          #^
    MOD_OP = 7          #%

class RelativeOperator(Enum):
    LE_OP = 1           #<=    
    LT_OP = 2           #<
    GE_OP = 3           #>=
    GT_OP = 4           #>
    EQ_OP = 5           #==
    NE_OP = 6           #!=

class BitwiseOperator(Enum):
    BNOT_OP = 1         #negate
    BAND_OP = 2         #band
    BOR_OP = 3          #bor
    BXOR_OP = 4         #bxor
    L_SHIFT_OP = 5      #lshift
    R_SHIFT_OP = 6      #rshift

class Expression(ABC):

    @abstractmethod
    def evaluate(self):
        pass

class Constant(Expression):
    def __init__(self, value, type) -> None:
        super().__init__()
        self.value = value
        self.type = type
    
    def getType(self):
        return self.type
    
    def evaluate(self):
        if self.type == ValueType.STRING_TOK:
            return self.value[1:-1]
        return float(self.value)

class Id(Expression):
    def __init__(self, ch, mem : Memory, type = None) -> None:
        super().__init__()
        if type:
            if (not self.isValidIdentifier(ch = ch)):
                raise Exception('Invalid Identifier')
            if (not self.isValidType(type = type)):
                raise Exception(f'Invalid Type {type}')
            self.mem = mem
            self.ch = ch
            self.type = type
        else:
            if (not self.isValidIdentifier(ch = ch)):
                raise Exception(f'Invalid Identifier: {ch}')
            self.mem = mem
            self.ch = ch
    
    def evaluate(self):
        # if (self.type == TokenType.SET_TOK):
        #     return Memory.fetch(self.ch)
        # return self.mem.store(self.ch)
        return self.mem.fetch(self.ch)[1]
    
    def setId(self, value): #create a place in memory for id
        self.mem.store(self.ch, value, type=self.type)
    
    def getId(self):
        return self.ch
    
    def isValidIdentifier(self, ch) -> bool:
        return ch[0].isalpha()
    
    def isValidType(self, type) -> bool:
        return type in ValueType


class BinaryExpression(Expression):
    def __init__(self, op : Operator, expr1 : Expression, expr2 : Expression) -> None:
        super().__init__()
        if (op == None):
            raise Exception('Invalid Operation') #TODO
        if (expr1 == None or expr2 == None):
            raise Exception('Invalid Expression(s)') #TODO
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
    
    def evaluate(self) -> int:
        value = 0
        if (self.op == Operator.ADD_OP):
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif (self.op == Operator.SUB_OP):
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif (self.op == Operator.MUL_OP):
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif (self.op == Operator.DIV_OP):
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif (self.op == Operator.MOD_OP):
            value = self.expr1.evaluate() % self.expr2.evaluate()
        elif (self.op == Operator.EXP_OP):
            value = self.expr1.evaluate() ^ self.expr2.evaluate()
        elif (self.op == Operator.REV_DIV_OP):
            value = self.expr1.evaluate() / self.expr2.evaluate()
        return value

class BooleanExpression(Expression):
    
    def __init__(self, op : RelativeOperator, expr1 : Expression, expr2 : Expression) -> None:
        super().__init__()
        if (op == None):
            raise Exception(f'Invalid Operator: {op}') #TODO
        if (expr1 == None or expr2 == None):
            raise Exception('Invalid Expression. You forgot one.') #TODO
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
    
    def evaluate(self) -> bool:
        value = False
        
        if (self.op == RelativeOperator.LE_OP):
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        elif (self.op == RelativeOperator.LT_OP):
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif (self.op == RelativeOperator.GE_OP):
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif (self.op == RelativeOperator.GT_OP):
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif (self.op == RelativeOperator.EQ_OP):
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif (self.op == RelativeOperator.NE_OP):
            value = self.expr1.evaluate() != self.expr2.evaluate()
        
        return value
    
class BitwiseExpression(Expression):
    def __init__(self, op : BitwiseOperator, expr1 : Expression, expr2 : Expression) -> None:
        super().__init__()
        if (op == None):
            raise Exception(f'Invalid Operator: {op}')
        if (op == BitwiseOperator.BNOT_OP and expr1 == None and expr2 != None):
            self.expr = expr2
            self.op = op
        if (expr1 == None or expr2 == None):
            raise Exception('Invalid Expression')
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
    
    def evaluate(self):
        value = bin(0)

        if (self.op == BitwiseOperator.BNOT_OP):
            value = ~self.expr.evaluate()
        elif (self.op == BitwiseOperator.BAND_OP):
            value = self.expr1.evaluate() & self.expr2.evaluate()
        elif (self.op == BitwiseOperator.BOR_OP):
            value = self.expr1.evaluate() | self.expr2.evaluate()
        elif (self.op == BitwiseOperator.BXOR_OP):
            value = self.expr1.evaluate() ^ self.expr2.evaluate()
        elif (self.op == BitwiseOperator.L_SHIFT_OP):
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif (self.op == BitwiseOperator.R_SHIFT_OP):
            value = self.expr1.evaluate() - self.expr2.evaluate()
        return value