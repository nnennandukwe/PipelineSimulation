
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
        return self.Regs

    def Print_out_everything(self):
        self.ifid.write.print_out()
        self.ifid.read.print_out()
        self.idex.write.print_out()
        self.idex.read.print_out()
        self.exmem.write.print_out()
        self.exmem.read.print_out()
        self.memwb.write.print_out()
        self.memwb.read.print_out()

    def WB_stage(self):
        memwb_dict = self.memwb.read.get()
        wrn = memwb_dict.get('WriteRegNum')
        if memwb_dict.get('Address_Func') == '[lb]' and not memwb_dict.get('ALUResult', None).isalpha():
            # print(memwb_dict['ALUResult'])
            self.Regs[memwb_dict['WriteRegNum']
                      ] = memwb_dict['ALUResult']
            print("${} is set to a new value of {} at memory address {}".format(
                wrn, hex(memwb_dict['LWDataValue']),
            ))

    def MEM_stage(self):
        self.memwb.write.set(self.exmem.read.get())
        if self.memwb.write.get().get('Address_Func') == '[lb]' and not self.memwb.write.get().get('ALUResult').isalpha():
            ALUResult = self.memwb.write.get().get('ALUResult')
            FoundAddr = self.Main_Mem[ALUResult]
            self.memwb.write.FoundAddr = FoundAddr

    def EX_stage(self):
        self.exmem.write.set(self.idex.read.get())

    def ID_stage(self):
        self.idex.write.set(self.ifid.read.get()['hash'])

    def IF_stage(self, hash_table):
        self.ifid.write.set(hash_table)

    def Copy_write_to_read(self):
        self.ifid.transfer()
        self.idex.transfer()
        self.exmem.transfer()
        self.memwb.transfer()

    def pipeline(self):
        for key, value in self.hash.items():
            self.IF_stage(value)
            self.ID_stage()
            self.EX_stage()
            self.MEM_stage()
            self.WB_stage()

            self.Copy_write_to_read()
            self.Print_out_everything()
