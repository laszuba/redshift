from myhdl import *

# Dummy test module

def test_():

    clock = [Signal(bool(0)) for i in range(1)]
    reset = ResetSignal(0, active=0, async=True)

    _inst =

    @always(delay(10))
    def clockgen():
        clock.next = not clock

    @instance
    def stimulus():

    return _inst, clockgen, stimulus

tb = traceSignals(test_)
sim = Simulation(tb)
sim.run(1000)
