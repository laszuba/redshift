from myhdl import *

def heartbeat(clk, rst, beat):
    """ Heartbeat generator

    clk - clock input
    rst - asyncronous reset
    beat - heartbeat output

    """
    width = 12
    counter = Signal(modbv(0)[width:]) 

    @always_seq(clock.posedge, rst.negedge)
    def div1():
        if reset = 0:
            counter.next = 0
        else:
            counter.next = counter + 1
            beat.next = counter[width-1]
    return div1
