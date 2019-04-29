
import sys

from arch import Arch
from pipelines.if_id import IF_ID
from formats.r_format import RFormat
from formats.i_format import IFormat


def main():

    # initialize architecture class
    a = Arch()
    a.develop_memory()
    a.develop_registers()

    # initialize all stages
    ifid = IF_ID()
    print(ifid.write.get())

    count = 0
    incremented_pc = 0x7A000
    with open('ins', 'r') as f:
        for line in f:
            count = count + 1
            incremented_pc += 4
            sep = list(line)  # separate each hex digit into list element
            s = int(line, 16)  # convert str to short int

            if int(sep[2], 16) == 0:  # opcode check for r-format

                r = RFormat()  # initialize new r-format object

                r.ins = s  # set instruction
                r.opcode = (s & r.R_MASKS["opcode"]) >> (32-6)
                r.src1 = (s & r.R_MASKS["s1"]) >> 21
                r.src2 = (s & r.R_MASKS["s2"]) >> 16
                r.dest = (s & r.R_MASKS["dest"]) >> 11
                r.shamt = (s & r.R_MASKS["shamt"]) >> 6

                func = (s & r.R_MASKS["func"])  # preliminary func

                # find correct matching function
                for option in r.func_options.keys():
                    if func == option:
                        # set function in instruction object
                        r.func = r.func_options[func]

                # format and print out full instruction
                print(r.full_ins())

                # add to Architecture dictionary
                a.hash[count] = dict(
                    pc=hex(incremented_pc),
                    addr=r.format(),
                    ins=r.as_hex(),
                    opcode=r.opcode,
                    src1=r.src1,
                    src2=r.src2,
                    dest=r.dest,
                    shamt=r.shamt,
                    func=r.func,
                    raw_func=hex(func)[2:],
                )
                a.example.append(r.full_ins())

            else:

                i = IFormat()  # initialize new i-format object

                i.ins = s  # set instruction
                i.opcode = (s & i.I_MASKS["opcode"]) >> (32-6)
                i.src1 = (s & i.I_MASKS["s1"]) >> 21
                i.dest_src = (s & i.I_MASKS["ds"]) >> 16
                i.offset = (s & i.I_MASKS["off"])

                # find correct matching operation
                for op in i.ops.keys():
                    if i.opcode == op:
                        # set string equivalent instruction (e.g. "lw", "sw")
                        i.op = i.ops[i.opcode]

                if (i.op == i.ops[0x20]) or (i.op == i.ops[0x28]) or (i.op == i.ops[0x23]) or (i.op == i.ops[0x2b]):
                    i.offset = i.signed_offset()
                    # format and print out full instruction
                    print(i.full_ins())

                # add to Architecture dictionary
                a.hash[count] = dict(
                    pc=hex(incremented_pc),
                    addr=i.format(),
                    ins=i.as_hex(i.ins),
                    opcode=i.opcode,
                    src1=i.src1,
                    dest_src=i.dest_src,
                    offset=i.offset,
                    func=i.op,
                )
                a.example.append(i.full_ins())

    a.print_hash()
    a.pipeline()


if __name__ == '__main__':
    main()
