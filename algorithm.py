from process import Process
from abc import ABC, abstractmethod


class IAlgorithm(ABC):

    @abstractmethod
    def shouldContextSwitch(self) -> bool:
        pass
    
    @abstractmethod
    def getNextProcess(self) -> Process:  
        pass

### Non-Preemptive
class FirstComeFirstServe(IAlgorithm):
    def __init__(self):
        pass


    ### Issue: on preemtive algorithms it doenst work without an update method

    ### Update method will only check if the system needs to do a context switch
    def shouldContextSwitch(self):
        pass

    def getNextProcess(self, readyQueue):       #### maybe also pass the currentRunningProcess
        if readyQueue: # if not empty
            return readyQueue.pop(0)
        else:
            return None


### Non-Preemptive
class ShortestJobFirst(IAlgorithm):
    def __init__(self):
        pass

    def shouldContextSwitch(self):
        pass

    def getNextProcess(self, readyQueue):
        if readyQueue:
            lowestBurstTimeProcess = readyQueue[0]
            for i, process in enumerate(readyQueue):
                if process.simulationData[process.currentCycle] < lowestBurstTimeProcess.simulationData[lowestBurstTimeProcess.currentCycle]:
                    lowestBurstTimeProcess = process
                    return readyQueue.pop(i)
            return readyQueue.pop(0)
        else:
            return None


### Preemptive
class MultilevelFeedbackQueue(IAlgorithm):
    def __init__(self):
        self.priorityQueue1 = []
        self.timeQuantaQueue1 = 5

        self.priorityQueue2 = []
        self.timeQuantaQueue2 = 10

        ### Queue 3 uses FCFS 
        self.priorityQueue3 = []
        self.algorithmQueue3 = FirstComeFirstServe()

        ####All processes enter first queue 1. 
        # If time quantum (Tq) expires before CPU burst is complete,
        #  the process is downgraded to next lower priority queue. Processes are
        #  not downgraded when preempted by a higher queue level process.
        #  Once a process has been downgraded, it will not be upgraded.

    def shouldContextSwitch(self):
        pass


    def getNextProcess(self, readyQueue):

        pass