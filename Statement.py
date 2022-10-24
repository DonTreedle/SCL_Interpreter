from abc import ABC, abstractmethod
from Arithmetic import Expression, Id, BooleanExpression
#from Block import Block
from Memory import Memory

class Statement(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class Iter():
    def __init__(self, expr1 : Expression, expr2 : Expression) -> None:
        if (expr1 == None or expr2 == None):
            raise Exception('Invalid Expression')
        self.expr1 = expr1
        self.expr2 = expr2
        self.it = []
    
    def evaluate(self):
        self.it.append(self.expr1.evaluate())

class Block():
    def __init__(self) -> None:
        self.stmts = []
    
    def add(self, stmt : Statement):
        if (stmt == None):
            raise Exception('Invalid Statement') #TODO
        self.stmts.append(stmt)
    
    def execute(self):
        for i in self.stmts:
            i.execute()

class ForStatement(Statement):
    def __init__(self, var : Id, it : Iter, blk : Block) -> None:
        super().__init__()
        if (var == None):
            raise Exception('Invalid Variable')
        if (it == None):
            raise Exception('Invalid Iterator')
        if (blk == None):
            raise Exception('Invalid Block')

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
            raise Exception('Invalid Expression')
        if (blk1 == None or blk2 == None):
            raise Exception('Invalid Block. There are 2 to check')
        
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
            raise Exception('Invalid Expression')
        
        self.expr = expr
    
    def execute(self) -> None:
        print(self.expr.evaluate())

class WhileStatement(Statement):
    def __init__(self, expr : BooleanExpression, blk : Block) -> None:
        super().__init__()
        if (expr == None):
            raise Exception('Invalid Expression')
        if (blk == None):
            raise Exception('Invalid Block')
        
        self.expr = expr
        self.blk = blk
    
    def execute(self) -> None:
        while(self.expr.evaluate()):
            self.blk.execute()

class AssignmentStatement(Statement):
    def __init__(self, var : Id,  expr : Expression, mem : Memory) -> None:
        if (var == None):
            raise Exception('null Id argument')
        if(expr == None):
            raise Exception('null ArithmeticExpression argument')
        if  (mem == None):
            raise Exception('null Memory argument') 
        self.var = var
        self.expr = expr
        self.mem = mem
    
    def execute(self) -> None:
        self.mem.store(self.var.getId(), self.expr.evaluate())

class FunctionStatement(Statement):
    def __init__(self, vars : Block, ) -> None:
        super().__init__()


class DefineStatement(Statement):
    def __init__(self, var, type, mem : Memory) -> None:
        super().__init__()
        if (var == None):
            raise Exception('Invalid Variable')
        if (type == None):
            raise Exception('Invalid Type')
        if (mem == None):
            raise Exception('Invalid Memory')
        self.var = var
        self.type = type
        self.mem = mem
    
    def execute(self) -> None:
        self.mem.store(self.var, None, type=self.type)