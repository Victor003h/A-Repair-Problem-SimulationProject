import heapq
import random
from Simulation import WorkingMachinesSimulation

def main():
    total_machine=40
    spares=10
    
    def repair_function(alpha=1, mean=3):
        beta = mean / alpha
        return random.gammavariate(alpha, beta)
    
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
        
        
    
  
    time_break_heap=[]
    Q=1.0
    repair_cost=10.0
    for i in range(total_machine-spares):
        heapq.heappush(time_break_heap,working_function())
    
    
    sim=WorkingMachinesSimulation(total_machine,spares,Q,repair_cost,time_break_heap,repair_function,repair_factor,working_function,alpha,mean)
    t=sim.run()
    print(t)
    
if __name__=="__main__":
    main()
    