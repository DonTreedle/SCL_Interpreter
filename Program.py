from Block import Block

class Program():
    def __init__(self, blk : Block) -> None:
        if (blk == None):
            raise Exception()
        
        self.blk = blk

    def execute(self):
        self.blk.execute()