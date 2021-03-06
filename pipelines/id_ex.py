
class ID_EX:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )


class Control:

    def __init__(self):
        self.RegDst = 0
        self.ALUSrc = 0
        self.ALUOp = ""
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

        self.hash = None

    def get(cls):
        return cls.__dict__

    def set(self, hash_table):
        # R - type
        if hash_table is None:
            self.RegDst = 0
            self.ALUSrc = 0
            self.ALUOp = ""
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.MemToReg = 0
            self.RegWrite = 0
            self.Address_Func = ""
            self.IncrPC = 0
            self.ReadReg1Value = 0
            self.ReadReg2Value = 0
            self.SEOffset = 0
            self.WriteReg_20_16 = 0
            self.WriteReg_15_11 = 0
            self.Function = ""

            self.hash = None

        if hash_table and hash_table.get('func') == 'nop':
            self.RegDst = 0
            self.ALUSrc = 0
            self.ALUOp = ""
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.MemToReg = 0
            self.RegWrite = 0
            self.Address_Func = ""
            self.IncrPC = 0
            self.ReadReg1Value = 0
            self.ReadReg2Value = 0
            self.SEOffset = 0
            self.WriteReg_20_16 = 0
            self.WriteReg_15_11 = 0
            self.Function = ""

            self.hash = None

        if hash_table and hash_table.get('dest'):
            self.RegDst = 1
            self.ALUSrc = 0
            self.ALUOp = "10"
            self.MemRead = 0
            self.MemWrite = 0
            self.MemToReg = 0
            self.RegWrite = 1
            self.SEOffset = "X"
            self.WriteReg_20_16 = hash_table['src2']
            self.WriteReg_15_11 = hash_table['dest']
            self.Function = hash_table['raw_func']

        else:
            # handling I - type LW
            if hash_table:
                if hash_table.get('func') is "lw" or hash_table.get('func') == 'lb':
                    self.MemRead = 1
                    self.MemToReg = 1
                    self.RegWrite = 1
                    self.RegDst = 0
                    self.WriteReg_15_11 = 0

                    # both SW and LW / SB and LB
                    self.SEOffset = hash_table.get('offset')
                    self.Function = "X"
                    self.ALUSrc = 1
                    self.ALUOp = "00"
                    self.WriteReg_20_16 = hash_table.get('dest_src')

                # handling I - type SW
                elif hash_table and hash_table.get('func') is "sw" or hash_table.get('func') == 'sb':
                    self.RegDst = "X"
                    self.WriteReg_15_11 = 31
                    self.MemRead = 0
                    self.MemWrite = 1

                    # both SW and LW / SB and LB
                    self.SEOffset = hash_table.get('offset')
                    self.ALUSrc = 1
                    self.ALUOp = "00"
                    self.WriteReg_20_16 = hash_table.get('dest_src')

                # both SW and LW / SB and LB
                    self.Function = "X"
                # self.SEOffset = hash_table.get('offset')
                # self.Function = "X"
                # self.ALUSrc = 1
                # self.ALUOp = "00"
                # self.WriteReg_20_16 = hash_table.get('dest_src')

        if hash_table:
            # all functions and types
            self.IncrPC = hash_table['pc']
            self.Address_Func = "[" + hash_table.get('func') + "]"
            self.ReadReg1Value = hash_table['src1']
            self.ReadReg2Value = (hash_table.get(
                'src2') or hash_table.get('dest_src'))
            self.Branch = 0

            self.hash = hash_table

    def print_out(self, write=None, read=None):

        if write:
            print("*** ID/EX Write (written to by the ID Stage) ***")
        elif read:
            print("*** ID/EX Read (read by the EX Stage) ***")
        print("Control: RegDst = {}, ALUSrc = {}, ALUOp = {}, MemRead = {}, MemWrite = {}, Branch = {}, MemToReg = {}, RegWrite = {},      {}".format(
            self.RegDst, self.ALUSrc, self.ALUOp, self.MemRead, self.MemWrite, self.Branch, self.MemToReg, self.RegWrite, self.Address_Func
        ))
        print("IncrPC = {}      ReadReg1Value = {}      ReadReg2Value = {}".format(
            self.IncrPC, self.ReadReg1Value, self.ReadReg2Value
        ))
        print("SEOffset = {}    WriteReg_20_16 = {}     WriteReg_15_11 = {}     Function = {}".format(
            self.SEOffset, self.WriteReg_20_16, self.WriteReg_15_11, self.Function
        ))
        print()
        print()
