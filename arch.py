
class Arch:
    """
    1. set up main memory (Main_Mem)
    2. setup and store registers array here (Regs)

    3. here is where you will develop the seven methods that allow the four pipeline registers
        IF_stage()
        ID_stage()
        EX_stage()
        MEM_stage()
        WB_stage()
        Print_out_everything()
        Copy_write_to_read()

    4. all instructions and address translations should be brought into a dictionary so as to begin the procedural stages in the pipeline
    """

    def __init__(self):
        self.Main_Mem = []  # list of short ints w/ 1024 max
        self.MEMORY_MAX = 0x400  # max amount of main memory available (1024)
        self.Regs = []  # all registers

    def develop_memory(self):
        for i in range(0x0, self.MEMORY_MAX+1):
            for j in range(0x0, 0x100):
                if len(self.Main_Mem) == self.MEMORY_MAX:
                    break
                else:
                    self.Main_Mem.append(j)
            if len(self.Main_Mem) == self.MEMORY_MAX:
                break
        # print(self.Main_Mem)
        return self.Main_Mem

    def develop_registers(self):
        for i in range(0x0, 32):
            self.Regs.append(0x100 + i)

        self.Regs[0x0] = 0
        # print(self.Regs)
        return self.Regs

    def collect():
        pass

    def IF_stage():
        pass

    def ID_stage():
        pass

    def EX_stage():
        pass

    def MEM_stage():
        pass

    def WB_stage():
        pass

    def Print_out_everything():
        pass

    def Copy_write_to_read():
        pass
