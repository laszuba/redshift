from myhdl import *
from heartbeat import heartbeat

def test_heartbeat():

    clock, beat = [Signal(bool(0)) for i in range(2)]
    reset = ResetSignal(0, active=0, async=True)

    heatbeat_inst = heartbeat(clock, reset, beat, 10)

    @always(delay(10))
    def clockgen():
        clock.next = not clock

    @instance
    def stimulus():
        reset.next = bool(0)
        yield delay(40)
        reset.next = bool(1)

    return heatbeat_inst, clockgen, stimulus

tb = traceSignals(test_heartbeat)
sim = Simulation(tb)
sim.run(1000)
