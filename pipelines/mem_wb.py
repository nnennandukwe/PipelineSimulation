

class MEM_WB:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )
        print('transfer in MEM / WB read SUCCESS')


class Control:

    def __init__(self):
        self.MemToReg = 0
        self.RegWrite = 0
        self.Address_Func = ""
        self.LWDataValue = ""           # e.g. "X"
        self.ALUResult = 0
        self.WriteRegNum = 0

    def get(cls):
        return cls.__dict__

    def set(self, hash_table):
        print(hash_table)

        self.MemToReg = hash_table.get('MemToReg')
        self.RegWrite = hash_table.get('RegWrite')
        self.Address_Func = hash_table.get('Address_Func')
        self.ALUResult = hash_table.get('ALUResult')
        self.WriteRegNum = hash_table.get('WriteRegNum')

        if self.Address_Func != "[lb]":
            self.LWDataValue = "X"
        else:
            self.LWDataValue = self.ALUResult
