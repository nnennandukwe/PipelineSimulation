
class EX_MEM:

    def __init__(self):

        self.write = Control()
        self.read = Control()


class Control:

    self.MemRead = 0
    self.MemWrite = 0
    self.Branch = 0
    self.MemToReg = 0
    self.RegWrite = 0
    self.Address_Func = ""      # e.g. "lw" or "add"
    self.CalcBTA = ""           # e.g. "X"
    self.Zero = ""              # e.g. "F"
    self.ALUResult = 0
    self.SWValue = 0
    self.WriteRegNum = 0

    def get():
        return dict(
            MemRead=self.MemRead,
            MemWrite=self.MemWrite,
            Branch=self.Branch,
            MemToReg=self.MemToReg,
            RegWrite=self.RegWrite,
            Address_Func=self.Address_Func,
            CalcBTA=self.CalcBTA,
            Zero=self.Zero,
            ALUResult=self.ALUResult,
            SWValue=self.SWValue,
            WriteRegNum=self.WriteRegNum,
        )
