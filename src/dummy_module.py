from myhdl import *

# Empty file

def example(clock, reset):
    """ Example

    clock - clock input
    reset - asyncronous reset

    """

    @always_seq(clock.posedge, reset=reset)
    def exampleLogic():


    @always_comb
    def exampleComb():

    return exampleLogic
