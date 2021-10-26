from enum import Enum
     
class Burst(Enum):
    CPU = 1
    IO = 2

class State(Enum):
    NEW = 1
    READY = 2
    WAITING = 3
    RUNNING = 4
    TERMINATED = 5

class Process:
    def __init__(self, pid, simulationData):
        self.pid = pid
        self.simulationData = simulationData

        self.priority = 1 # default priority

        self.state = State.READY # Assuming the process is ready once it's initiated
        self.previousState = State.NEW

        ### Iterate through the simulation data and track the position
        self.currentBurst = 0
        self.currentBurstType = Burst.CPU
        self.burstFinished = False
        self.burstStarted = False
        self.discreteTimeUnit = 0


        self.totalWaitingTime = 0
        self.turnaroundTime = 0
        self.responseTime = 0


        self.timeRunning = 0
        self.totalTimeRunning = 0

    def update(self):
        #### Track time running
        if self.state == State.RUNNING:
            self.timeRunning += 1 
        else:
            self.timeRunning = 0

        ### Changes process' state if they are done with burst times or I/O times 
        ### according to the provided simulation data
        if (self.state == State.WAITING or self.state == State.RUNNING):

            self.discreteTimeUnit += 1
        
            # check if current cpu/io Burst is finished
            if self.discreteTimeUnit >= self.simulationData[self.currentBurst]:

                self.previousState = self.state
                
                self.timeRunning = 0

                # Check if the finished Burst was a CPU Burst
                if self.currentBurstType == Burst.CPU:
                    if self.currentBurst >= len(self.simulationData) - 1:
                        self.setState(State.TERMINATED)
                        print('P' + str(self.pid) + ' terminated execution')
                    else:
                        self.setState(State.WAITING)
                else: # Done with IO Burst
                    self.setState(State.READY)
                
                self.currentBurst += 1
                self.burstFinished = True

            if self.burstFinished:
                self.discreteTimeUnit = 0
                self.burstFinished = False

        if self.currentBurst % 2 == 0:
            self.currentBurstType = Burst.CPU
        else:
            self.currentBurstType = Burst.IO

    def setState(self, newState):
        self.previousState = self.state
        self.state = newState

    ### Print formatted process data
    def print(self):
        print('{:20}'.format('P' + str(self.pid)), end='')
        if self.state == State.TERMINATED:
            print('{:20}'.format('None'), end='')
            print('{:20}'.format('None'), end='')  
            print('{:20}'.format('None'), end='') 
        else:
            print('{:20}'.format(self.currentBurstType.name), end='')
            print('{:20}'.format(str(self.simulationData[self.currentBurst])), end='')  
            print('{:20}'.format(str(self.simulationData[self.currentBurst] - self.discreteTimeUnit)), end='') 
        print('{:20}'.format(self.state.name), end='')
        print()