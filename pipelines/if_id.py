
class IF_ID:

    def __init__(self):

        self.write = Control()
        self.read = Control()


class Control:

    # def __init__(self):

    self.Inst = 0       # incoming instruction
    self.address = 0    # incoming address
    self.IncrPC = 0     # incremented PC

    def get():
        return dict(
            Inst=self.Inst,
            Address=self.address,
            IncrPC=self.IncrPC
        )
