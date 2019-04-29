

class IFormat():

    I_MASKS = {
        "opcode": 0b11111100000000000000000000000000,
        "s1": 0b00000011111000000000000000000000,
        "ds": 0b00000000000111110000000000000000,
        "off"	: 0b00000000000000001111111111111111,
    }

    def __init__(
        self,
        opcode=None,
        offset=None,
        src1=None,
        dest_src=None,
        op=None,
        ins=None,
    ):

        self.opcode = opcode
        self.offset = offset
        self.src1 = src1
        self.dest_src = dest_src
        self.ins = ins  # pure first instructions
        self.op = op  # e.g. "beq", "bne"
        # self.branch = branch # instruction from offset

        # operation options
        self.ops = {
            0x20: "lb",
            0x28: "sb",
            0x23: "lw",
            0x2b: "sw",
        }

    def as_hex(self, instruction):
        return hex(instruction)

    def format(self):
        return f'{self.op} ${self.dest_src}, {self.offset}(${self.src1})'

    # convert offset value to signed int

    def signed_offset(self):
        if self.offset >= 2**15:
            self.offset -= 2**16
        return self.offset

    # full written out instructions as string

    def full_ins(self):
        return (
            f"{self.as_hex(self.ins)}  {self.op} "
            f"{self.format()}"
        )
