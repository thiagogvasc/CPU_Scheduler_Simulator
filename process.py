from enum import Enum

     
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

        self.state = State.READY # Assuming the process is ready once it's initiated
        self.previousState = State.NEW

        self.currentCycle = 0
        self.currentCycleType = 'Burst'
        self.cycleFinished = False
        self.discreteTimeUnit = 0


        self.totalWaitingTime = 0
        self.turnaroundTime = 0
        self.responseTime = 0

    def update(self):

        print('P' + str(self.pid) + ': ' + 'time: ' + str(self.discreteTimeUnit) + ' cycle: ' + str(self.currentCycle) + ' type: ' + self.currentCycleType + ' state: ', self.state.name)

        ### Changes process' state if they are done with burst times or I/O times 
        ### according to the provided simulation data
        if (self.state == State.WAITING or self.state == State.RUNNING):

            # check if current burst/io cycle is finished
            if self.discreteTimeUnit == self.simulationData[self.currentCycle]:

                self.previousState = self.state

                # Check if the finished cycle was a burst cycle
                if self.currentCycleType == 'Burst':
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
            else:
                self.discreteTimeUnit += 1

        if self.currentCycle % 2 == 0:
            self.currentCycleType = 'Burst'
        else:
            self.currentCycleType = 'I/O'


        ### Track response time
        if self.previousState == State.NEW and self.state == State.READY:
            self.responseTime += 1

        ### Track waiting time
        if self.state == State.READY:
            self.totalWaitingTime += 1

        ### Track turnaround time
        if self.state != State.TERMINATED:
            self.turnaroundTime += 1

    def setState(self, newState):
        self.previousState = self.state
        self.state = newState
        print(str(self.pid) + ' ' + self.previousState.name + ' TO ' + self.state.name)
