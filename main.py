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
    
    c=1
    while(c<200):
    
        time_break_heap=[]
        repair_factor=1.0
        alpha=10
        mean=30
        for i in range(total_machine-spares):
            heapq.heappush(time_break_heap,working_function())
        sim=WorkingMachinesSimulation(total_machine,spares,time_break_heap,repair_function,repair_factor,working_function,alpha,mean)
        
        
    
            
        time=sim.run()
        print(time)
        c+=1
    
if __name__=="__main__":
    main()
    