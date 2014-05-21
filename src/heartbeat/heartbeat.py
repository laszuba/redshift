from myhdl import *

def heartbeat(clock, reset, beat, n):
    """ Heartbeat generator

    clock - clock input
    reset - asyncronous reset
    beat - heartbeat output
    n - maximum count

    """
    counter = Signal(intbv(0))

    @always_seq(clock.posedge, reset=reset)
    def heartbeatLogic():
        counter.next = (counter + 1) % n

        if (counter == 0) and (clock == 1):
            beat.next = bool(1)
        else:
            beat.next = bool(0)

    return heartbeatLogic
