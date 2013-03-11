from myhdl import *
import heartbeat

def test_heartbeat():

    clk, rst, beat = [Signal(bool(0)) for i in range(3)]

    heatbeat_inst = heartbeat(clk, rst, beat)

    @always(delay(10)) 
    def clkgen(): 
        clk.next = not clk
    
    @instance
    def stimulus():
        rst.next = False
        yield delay(100)
        rst.next = True
        
        raise StopSimulation

    return heatbeat_inst, clkgen, stimulus


def simulate(timesteps):
    tb = traceSignals(test_heartbeat)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(1000)