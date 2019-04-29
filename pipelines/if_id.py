
class IF_ID:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )
        print('transfer successful')


class Control:

    def __init__(self):
        self.Inst = 0       # incoming instruction
        self.address = 0    # incoming address
        self.IncrPC = 0     # incremented PC
        self.hash = None        # dictionary from Arch

    def get(cls):
        return cls.__dict__

    def set(cls, hash_table):
        # hash is a dictionary
        cls.__dict__.update(dict(
            Inst=hash_table['ins'],
            Address=hash_table['addr'],
            IncrPC=hash_table['pc']
        ))
        cls.hash = hash_table
