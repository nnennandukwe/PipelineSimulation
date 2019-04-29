
class EX_MEM:

    def __init__(self):

        self.write = Control()
        self.read = Control()

    def transfer(self):
        self.read.__dict__.update(
            self.write.get()
        )
        print('transfer from exmem write to read SUCCESS')


class Control:

    def __init__(self):
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

    def get(cls):
        return cls.__dict__

    def set(cls, hash_table):
        # print("EX MEMMMMM ----- ", hash_table)

        for key, value in hash_table.items():
            if key in cls.get().keys():
                cls.get()[key] = value

        cls.CalcBTA = "X"
        cls.Zero = "F"
        cls.SWValue = hash_table.get('ReadReg2Value')

        addr_func = hash_table.get('Address_Func')

        # handling R - type add function
        if addr_func is '[add]':
            cls.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get(
                    'ReadReg2Value'
            )
            cls.WriteRegNum = hash_table.get('WriteReg_15_11')

        # handling I - type "lw"
        elif addr_func == '[lw]' or addr_func == '[lb]':
            cls.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get('SEOffset')
            cls.WriteRegNum = hash_table.get('WriteReg_20_16')

        # handling "sw"
        elif addr_func == '[sw]' or addr_func == '[sw]':
            cls.ALUResult = hash_table.get(
                'ReadReg1Value') + hash_table.get('SEOffset')
            cls.WriteRegNum = "X"

        # handling "sub"
        elif addr_func == '[sub]':
            cls.ALUResult = hash_table.get(
                'ReadReg1Value') - hash_table.get('ReadReg2Value')
            cls.WriteRegNum = hash_table.get('WriteReg_15_11')
