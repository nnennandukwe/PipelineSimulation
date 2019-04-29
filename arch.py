
import pipelines

from pipelines.if_id import IF_ID as ifid
from pipelines.id_ex import ID_EX as idex
from pipelines.ex_mem import EX_MEM as exmem
from pipelines.mem_wb import MEM_WB as memwb


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
        self.Main_Mem = []          # list of short ints w/ 1024 max
        # max amount of main memory available (1024)
        self.MEMORY_MAX = 0x400
        self.Regs = []              # all registers
        self.hash = {}              # mips instructions & their addresses
        self.example = []           # eventually I'll delete this

        # CREATE / INITIALIZE ALL PIPELINE STAGES

        self.ifid = ifid()
        self.idex = idex()
        self.exmem = exmem()
        self.memwb = memwb()

    def develop_memory(self):
        for i in range(0x0, self.MEMORY_MAX+1):
            for j in range(0x0, 0x100):
                if len(self.Main_Mem) == self.MEMORY_MAX:
                    break
                else:
                    self.Main_Mem.append(j)
            if len(self.Main_Mem) == self.MEMORY_MAX:
                break
        return self.Main_Mem

    def develop_registers(self):
        for i in range(0x0, 32):
            self.Regs.append(0x100 + i)

        self.Regs[0x0] = 0
        # print(self.Regs)
        return self.Regs

    def Print_out_everything():
        pass

    def WB_stage(self):
        print('made it to the WB stage...')
        print(self.memwb.write.get())

    def MEM_stage(self):
        print('made it to the mem stage')
        self.memwb.write.set(self.exmem.read.get())
        print("IN MEM/WEB STAGE ------ ", self.memwb.write.get())
        # self.memwb.transfer()
        print(self.memwb.read.get())
        # self.WB_stage()

    def EX_stage(self):
        self.exmem.write.set(self.idex.read.get())
        print('You have made it to the EX stage')
        # self.exmem.transfer()
        print("IN EX/MEM", self.exmem.read.get())
        # self.MEM_stage()

    def ID_stage(self):
        # print("IN IFID ----", self.ifid.read.get())
        print('you are now in the id stage')
        print("IFID ----", self.ifid.read.get())
        self.idex.write.set(self.ifid.read.get()['hash'])
        # self.idex.transfer()
        print("IN IDEX ----", self.idex.read.get())
        # self.EX_stage()

    def IF_stage(self, hash_table):
        print('in the IF METHODDDD')
        self.ifid.write.set(hash_table)
        # self.ifid.transfer()
        # self.ID_stage()

    def print_hash(self):
        print(self.hash)

    def Copy_write_to_read(self):
        self.ifid.transfer()
        self.idex.transfer()
        self.exmem.transfer()
        self.memwb.transfer()

    def pipeline(self):
        # for cycle in range(len(self.hash)):
        for key, value in self.hash.items():
            self.IF_stage(value)
            self.ID_stage()
            self.EX_stage()
            self.MEM_stage()
            self.WB_stage()

            print('called {} TIMES'.format(key))
            self.Copy_write_to_read()
