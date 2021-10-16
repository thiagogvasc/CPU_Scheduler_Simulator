from enum import Enum

import time

     
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

        self.priority = 1 # default

        self.state = State.READY # Assuming the process is ready once it's initiated
        self.previousState = State.NEW

        self.currentCycle = 0
        self.currentCycleType = Burst.CPU
        self.cycleFinished = False
        self.cycleStarted = False
        self.discreteTimeUnit = 0


        self.totalWaitingTime = 0
        self.turnaroundTime = 0
        self.responseTime = 0


        self.timeRunning = 0


        ### Control delta time
        self.initialTime = 0
        self.elapsedTime = 0

    def update(self):
        ### Control delta time
        if self.initialTime == 0:
            self.initialTime = time.time()
        else:
            self.elapsedTime = time.time() - self.initialTime


        if self.state == State.RUNNING:
            self.timeRunning += 1 
        else:
            self.timeRunning = 0

        #print('P' + str(self.pid) + ': ' + 'time: ' + str(self.discreteTimeUnit) + ' cycle: ' + str(self.currentCycle) + ' type: ' + str(self.currentCycleType) + ' state: ', self.state.name + ' tw: ' + str(self.totalWaitingTime))

        ### Changes process' state if they are done with burst times or I/O times 
        ### according to the provided simulation data
        if (self.state == State.WAITING or self.state == State.RUNNING):

            self.discreteTimeUnit += 1
        
            # check if current burst/io cycle is finished
            if self.discreteTimeUnit >= self.simulationData[self.currentCycle]:

                self.previousState = self.state
                
                self.timeRunning = 0

                # Check if the finished cycle was a burst cycle
                if self.currentCycleType == Burst.CPU:
                    print('P' + str(self.pid) + ' done with cpu burst time')
                    if self.currentCycle >= len(self.simulationData) - 1:
                        self.setState(State.TERMINATED)
                        print('DODODODODONNNNNNNNEEEEEE')
                    else:
                        self.setState(State.WAITING)
                else: # Done with IO Cycle
                    print('P' + str(self.pid) + ' done with IO burst time')
                    self.setState(State.READY)
                
                self.currentCycle += 1
                self.cycleFinished = True

            if self.cycleFinished:
                self.discreteTimeUnit = 0
                self.cycleFinished = False

        if self.currentCycle % 2 == 0:
            self.currentCycleType = Burst.CPU
        else:
            self.currentCycleType = Burst.IO


        ### Track response time
        if self.previousState == State.NEW and self.state == State.READY:
            self.responseTime += 1

        ### Track waiting time
        if self.state == State.READY:
            pass
            #self.totalWaitingTime += 1

        ### Track turnaround time
        if self.state != State.TERMINATED:
            self.turnaroundTime += 1


        print('P' + str(self.pid) + ': ' + 'time: ' + str(self.discreteTimeUnit) + ' cycle: ' + str(self.currentCycle) + ' type: ' + str(self.currentCycleType) + ' state: ', self.state.name + ' tw: ' + str(self.totalWaitingTime))

    def setState(self, newState):
        self.previousState = self.state
        self.state = newState
        print(str(self.pid) + ' ' + self.previousState.name + ' TO ' + self.state.name)


    def preempt(self):
        pass
