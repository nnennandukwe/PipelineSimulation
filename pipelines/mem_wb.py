

class MEM_WB:

    def __init__(self):

        self.write = Control()
        self.read = Control()


class Control:

    self.MemToReg = 0
    self.RegWrite = 0
    self.Address_Func = ""
    self.LWDataValue = ""           # e.g. "X"
    self.ALUResult = 0
    self.WriteRegNum = 0

    def get():
        return dict(
            MemToReg=self.MemToReg,
            RegWrite=self.RegWrite,
            Address_Func=self.Address_Func,
            LWDataValue=self.LWDataValue,
            ALUResult=self.ALUResult,
            WriteReg=self.WriteReg,
        )
