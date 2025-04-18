

import heapq
import math


class WorkingMachinesSimulation():
    def __init__(self,total_machine,spares,Q,repair_cost,time_break_heap,repair_distribution_function,repair_factor,working_distribution_function,alpha,mean):
        
        self.total_machine=total_machine
        self.spares=spares
        self.repair_factor=repair_factor
        self.alpha=alpha
        self.mean=mean
        
        
        self.Q=Q
        self.profit=0
        
        self.repair_cost=repair_cost
        #Time Variables:
        self.time=0
        self.repair_time=math.inf
    
        self.time_break_heap=time_break_heap
    
        self.working_distribution_function=working_distribution_function
        self.repair_distribution_function=repair_distribution_function
        # State Variable
        self.machines_down=0
        
    def BreakDown(self):
        
        next_event_time=heapq.heappop(self.time_break_heap)
        dt=next_event_time-self.time
        self.profit+=self.Q * (self.total_machine-self.spares)*dt
        
        self.time=next_event_time
        self.machines_down+=1
        
        if self.machines_down==1:
            t=self.repair_distribution_function()
            self.repair_time=self.time+t
            
            t1= self.working_distribution_function(self.alpha,self.mean)
            heapq.heappush(self.time_break_heap,self.time+t1)
           # self.spares-=1
            
            return False
            
            
        elif self.machines_down< self.spares+1:
            t= self.working_distribution_function(self.alpha,self.mean)
            heapq.heappush(self.time_break_heap,self.time+t)
            #self.spares-=1
            return False
        
        elif  self.machines_down==self.spares+1:
            return True
        
            
    def Reapair(self):
        
        self.time=self.repair_time
        self.profit-=self.repair_cost
        self.machines_down-=1
       # self.spares+=1
        
        if self.machines_down>0:
            t=self.repair_distribution_function()
            self.repair_time=self.time+t
            
        else:
            self.repair_time=math.inf
    
    def run(self):
        
        while(True):
            t1=self.time_break_heap[0]
            if t1<self.repair_time:
                end=self.BreakDown()
                if end:break
            else: self.Reapair()

        return self.time,self.profit

    def reset(self):
        self.time=0
        self.repair_time=math.inf
        self.machines_down=0
        self.profit=0
        
        
        
    #  trabajando [] n-1
    #  repuesto  =0
    #  reparacion  r=s+1
    #   n + s 
        
    
    
        
        
        