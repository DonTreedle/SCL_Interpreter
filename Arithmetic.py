from abc import ABC, abstractmethod
from enum import Enum
from LexicalAnalyzer import LexicalAnalyzer
from Memory import Memory

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

class Expression(ABC):

    @abstractmethod
    def evaluate(self) -> int:
        pass

class Constant(Expression):
    def __init__(self, value : int) -> None:
        super().__init__()
        self.value = value
    
    def evaluate(self) -> int:
        return self.value

class Id(Expression):
    def __init__(self, ch) -> None:
        super().__init__()
        if (not LexicalAnalyzer.isValidIdentifier(ch)):
            raise Exception()
        self.ch = ch
    
    def evaluate(self) -> int:
        return Memory.fetch(self.ch)
    
    def getChar(self):
        return self.ch

class BinaryExpression(Expression):
    def __init__(self, op : Operator, expr1 : Expression, expr2 : Expression) -> None:
        super().__init__()
        if (op == None):
            raise Exception() #TODO
        if (expr1 == None or expr2 == None):
            raise Exception() #TODO
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
    
    def __init__(self, op : Operator, expr1 : Expression, expr2 : Expression) -> None:
        super().__init__()
        if (op == None):
            raise Exception() #TODO
        if (expr1 == None or expr2 == None):
            raise Exception() #TODO
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