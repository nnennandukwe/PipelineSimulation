

class MEM_WB:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )


class Control:

    def __init__(self):
        self.MemToReg = 0
        self.RegWrite = 0
        self.Address_Func = ""
        self.LWDataValue = ""           # e.g. "X"
        self.ALUResult = 0
        self.WriteRegNum = 0

        self.FoundAddr = 0              # from Main_Mem index
        self.SWValue = 0

        self.hash = None

    def get(cls):
        return cls.__dict__

    def set(self, hash_table):

        if hash_table.get('Address_Func') is '[nop]':
            for key, value in self.get().items():
                value = 0

        self.MemToReg = hash_table.get('MemToReg')
        self.RegWrite = hash_table.get('RegWrite')
        self.Address_Func = hash_table.get('Address_Func')
        self.ALUResult = hash_table.get('ALUResult')
        self.WriteRegNum = hash_table.get('WriteRegNum')
        self.SWValue = hash_table.get('SWValue')

        if self.Address_Func != "[lb]":
            self.LWDataValue = "X"
        else:
            self.LWDataValue = self.ALUResult
            self.ALUResult = "X"

    def print_out(self):
        print("Control: MemToReg = {}, RegWrite = {},       {}".format(
            self.MemToReg, self.RegWrite, self.Address_Func
        ))

        if self.LWDataValue == "X" or self.LWDataValue == "":
            print("LWDataValue = {}     ALUResult = {}      WriteRegNum = {}".format(
                self.LWDataValue, self.ALUResult, self.WriteRegNum
            ))
        else:
            print("LWDataValue = mem contents @ {}      ALUResult = {}            WriteRegNum = {}".format(
                self.LWDataValue, self.ALUResult, self.WriteRegNum
            ))

        if self.SWValue:
            print("(value {} written to memory address {})".format(
                hex(self.SWValue), self.ALUResult
            ))
