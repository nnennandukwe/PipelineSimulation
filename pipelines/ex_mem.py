
class EX_MEM:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )


class Control:

    def __init__(self):
        self.MemRead = 0
        self.MemWrite = 0
        self.Branch = 0
        self.MemToReg = 0
        self.RegWrite = 0
        self.Address_Func = 0      # e.g. "lw" or "add"
        self.CalcBTA = 0           # e.g. "X"
        self.Zero = 0              # e.g. "F"
        self.ALUResult = 0
        self.SWValue = 0
        self.WriteRegNum = 0

        self.hash = None

    def get(cls):
        return cls.__dict__

    def set(self, hash_table):
        if hash_table.get('Address_Func') == '[nop]':
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.MemToReg = 0
            self.RegWrite = 0
            self.Address_Func = 0
            self.CalcBTA = 0
            self.Zero = 0
            self.ALUResult = 0
            self.SWValue = 0
            self.WriteRegNum = 0

            self.hash = None

        for key, value in hash_table.items():
            if key in self.get().keys():
                self.get()[key] = value

        self.CalcBTA = "X"
        self.Zero = "F"
        self.SWValue = hash_table.get('ReadReg2Value')

        addr_func = hash_table.get('Address_Func')

        # handling R - type add function
        if addr_func is '[add]':
            self.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get(
                    'ReadReg2Value'
            )
            self.WriteRegNum = hash_table.get('WriteReg_15_11')

        # handling I - type "lw"
        elif addr_func == '[lw]' or addr_func == '[lb]':
            self.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get('SEOffset')
            self.WriteRegNum = hash_table.get('WriteReg_20_16')

        # handling "sw"
        elif addr_func == '[sw]' or addr_func == '[sb]':
            self.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get('SEOffset')
            self.WriteRegNum = "X"

        # handling "sub"
        elif addr_func == '[sub]':
            self.ALUResult = hash_table.get(
                'ReadReg1Value') - hash_table.get('ReadReg2Value')
            self.WriteRegNum = hash_table.get('WriteReg_15_11')

    def print_out(self, write=None, read=None):

        if write:
            print("*** EX/MEM Write (written to by the EX Stage) ***")
        elif read:
            print("*** EX/MEM Read (read by the MEM Stage) ***")
        print("Control: MemRead = {}, MemWrite = {}, Branch = {}, MemToReg = {}, RegWrite = {},         {}".format(
            self.MemRead, self.MemWrite, self.Branch, self.MemToReg, self.RegWrite, self.Address_Func
        ))
        print("CalcBTA = {}         Zero = {}       ALUResult = {}".format(
            self.CalcBTA, self.Zero, self.ALUResult
        ))
        print("SWValue = {}     WriteRegNum = {}".format(
            self.SWValue, self.WriteRegNum
        ))
        print()
        print()
