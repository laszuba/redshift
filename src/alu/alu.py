from myhdl import *

def heartbeat(clock, reset, in1, in2, out, func):
    """ Main ALU

    clock - clock input
    reset - asyncronous reset
    in1 - input bus for operand 1
    in2 - input bus for operand 2
    out - result of operation output bus
    func - input to select operation

    """

    operations = enum('ADD','SUB','AND','OR','NOT','XOR','MOV')

    @always_comb
    def aluLogic():
        raise NotImplementedError

        if func == :
            # do stuff
        elif func == :

    return aluLogic
