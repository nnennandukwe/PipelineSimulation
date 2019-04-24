
class ID_EX:

    def __init__(self):

        self.write = Control()
        self.read = Control()


class Control:

    self.RegDst = 0
    self.ALUSrc = 0
    self.ALUOp = "00"
    self.MemRead = 0
    self.MemWrite = 0
    self.Branch = 0
    self.MemToReg = 0
    self.RegWrite = 0
    self.Address_Func = ""      # e.g. "sw" or "lb"
    self.IncrPC = 0
    self.ReadReg1Value = 0
    self.ReadReg2Value = 0
    self.SEOffset = 0
    self.WriteReg_20_16 = 0
    self.WriteReg_15_11 = 0
    self.Function = ""          # e.g. "X"

    def get():
        return dict(
            RegDst=self.RegDst,
            ALUSrc=self.ALUSrc,
            ALUOp=self.ALUOp,
            MemRead=self.MemRead,
            MemWrite=self.MemWrite,
            Branch=self.Branch,
            MemToReg=self.MemToReg,
            RegWrite=self.RegWrite,
            Address_Func=self.Address_Func,
            IncrPC=self.IncrPC,
            ReadReg1Value=self.ReadReg1Value,
            ReadReg2Value=self.ReadReg2Value,
            SEOffset=self.SEOffset,
            WriteReg_20_16=self.WriteReg_20_16,
            WriteReg_15_11=self.WriteReg_15_11,
            Function=self.Function,
        )
