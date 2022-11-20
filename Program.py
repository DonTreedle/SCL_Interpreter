from Statement import Block

class Program():
    def __init__(self, blks : Block) -> None:
        if (blks == None):
            raise Exception()
        
        self.blks = blks

    def execute(self):
        for i in self.blks:
            for j in i:
                for k in j:
                    k.execute()