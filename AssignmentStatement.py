from Memory import Memory

class AssignmentStatement():
    def __init__(self, var,  expr) -> None:
        if (var == None):
            raise Exception('null id argument')
        if(expr == None):
            raise Exception('null ArithmeticExpression argument')
        self.var = var
        self.expr = expr
    
    def execute(self):
        Memory.store(self.var, self.expr.evalute())