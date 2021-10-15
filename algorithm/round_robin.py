from algorithm.abstract.scheduling_algorithm import SchedulingAlgorithm
from process import State


class RoundRobin(SchedulingAlgorithm):
    def __init__(self, scheduler):
        super().__init__(scheduler)

        self.readyQueue = []

        self.timeQuanta = 5

    # This method will be called whenever there is no process currently running
    def noProcessRunning(self) -> None:
        if self.readyQueue:
            newProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(newProcess)

    # This method will be called whenever a new process is activated
    def processActivated(self, process) -> None:
        self.readyQueue.append(process)

    # This method will be called at every iteration to handle the time quanta
    def handleTimeQuanta(self, process) -> None:
        if process:
            if process.timeRunning >= 5:
                print('QUANTA EXPIRED')
                self.scheduler.preempt()
                self.readyQueue.append(process)
                if self.readyQueue:
                    newProcess = self.readyQueue.pop(0)
                    self.scheduler.dispach(newProcess)
                    print('dispatched ' + str(newProcess.pid) + ' to cpu')
                else:
                    self.scheduler.currentProcess = None

     # This method will be called when a process has to wait for I/O
    def processWaiting(self, process) -> None:
        if self.readyQueue:
            newProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(newProcess)
        ### REFACTOR LATER
        else:
            self.scheduler.currentProcess = None
    
    # This method will be called when a process has finished waiting for I/O
    def processFinishedIO(self, process) -> None:
        ### DONT NEED IF STATEMENT
        ### REFACTOR LATER
        if process not in self.readyQueue:
            self.readyQueue.append(process)
            print('P' + str(process.pid) + ' appended in ready queue')


    # This method will be called when a process terminates execution
    def processTerminated(self, process) -> None:
        if self.readyQueue: ### if not empty
            nextProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(nextProcess)
        else:
            self.scheduler.currentProcess = None
