from Statement import Statement
from typing import List

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