import heapq
import random
from Simulation import WorkingMachinesSimulation

def main():
    total_machine=40
    spares=10
    
    def repair_function(mu=1/2.0):
        return random.expovariate(mu)
    
    def working_function(alpha=10, mean=30):
        beta = mean / alpha
        return random.gammavariate(alpha, beta)
        #return random.expovariate(lambda_op)
    
    time_break_heap=[]
    repair_factor=1.0
    alpha=10
    mean=30
    for i in range(total_machine-spares):
        heapq.heappush(time_break_heap,working_function())
    sim=WorkingMachinesSimulation(total_machine,spares,time_break_heap,repair_function,repair_factor,working_function,alpha,mean)
    time=sim.run()
    
    print(time)
    
    
if __name__=="__main__":
    main()
    