
class IF_ID:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )


class Control:

    def __init__(self):
        self.Inst = 0           # incoming instruction
        self.address = 0        # incoming address
        self.IncrPC = 0         # incremented PC
        self.hash = None        # dictionary from Arch

    def get(cls):
        return cls.__dict__

    def set(cls, hash_table):
        # hash is a dictionary
        if hash_table.get('func') == 'nop':
            for key, value in cls.get().items():
                value = 0
            for key, value in hash_table.items():
                value = 0
        cls.__dict__.update(dict(
            Inst=hash_table['ins'],
            Address=hash_table['addr'],
            IncrPC=hash_table['pc']
        ))
        cls.hash = hash_table

    def print_out(self, read=None, write=None):
        if write:
            print("*** IF/ID Write (written to by the IF Stage) ***")
        elif read:
            print("*** IF/ID Read (read by the ID Stage) ***")
        print("Inst = {}    [ {} ]  IncrPC = {}".format(
            self.Inst, self.address, self.IncrPC
        ))
        print()
        print()
