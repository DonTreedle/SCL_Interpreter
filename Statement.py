from abc import ABC, abstractmethod
from Arithmetic import Expression, Id, BooleanExpression
from Block import Block
from Memory import Memory

class Statement(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class Iter():
    def __init__(self, expr1 : Expression, expr2 : Exception) -> None:
        if (expr1 == None or expr2 == None):
            raise Exception()
        self.expr1 = expr1
        self.expr2 = expr2
        self.it = []
    
    def evaluate(self):
        self.it.append(self.expr1.evaluate())

class ForStatement(Statement):
    def __init__(self, var : Id, it : Iter, blk : Block) -> None:
        super().__init__()
        if (var == None):
            raise Exception()
        if (it == None):
            raise Exception()
        if (blk == None):
            raise Exception()

        self.var = var
        self.it = it
        self.blk = blk
    
    def execute(self) -> None:
        if (self.it.evaluate()[0] < self.it.evaluate()[1]):
            Memory.store(self.var.getChar(), self.it.evaluate()[0])
            while(Memory.fetch(self.var.getChar()) <= self.it.evaluate()[1]):
                self.blk.execute()
                i = Memory.fetch(self.var.getChar())
                i += 1
                Memory.store(self.var.getChar(), i)
        else:
            Memory.store(self.var.getChar(), self.it.evaluate()[0])
            while(Memory.fetch(self.var.getChar()) >= self.it.evaluate()[1]):
                self.blk.execute()
                i = Memory.fetch(self.var.getChar())
                i -= 1
                Memory.store(self.var.getChar(), i)

class IfStatement(Statement):
    def __init__(self, expr : BooleanExpression, blk1 : Block, blk2 : Block) -> None:
        super().__init__()
        if (expr == None):
            raise Exception()
        if (blk1 == None or blk2 == None):
            raise Exception()
        
        self.expr = expr
        self.blk1 = blk1
        self.blk2 = blk2
    
    def execute(self) -> None:
        if (self.expr.evaluate()):
            self.blk1.execute()
        else:
            self.blk2.execute()

class PrintStatement(Statement):
    def __init__(self, expr : Expression) -> None:
        super().__init__()
        if (expr == None):
            raise Exception()
        
        self.expr = expr
    
    def execute(self) -> None:
        print(self.expr.evaluate())

class WhileStatement(Statement):
    def __init__(self, expr : BooleanExpression, blk : Block) -> None:
        super().__init__()
        if (expr == None):
            raise Exception()
        if (blk == None):
            raise Exception()
        
        self.expr = expr
        self.blk = blk
    
    def execute(self) -> None:
        while(self.expr.evaluate()):
            self.blk.execute()