from process import State
from process import Process
from abc import ABC
from abc import abstractmethod


class SchedulingAlgorithm(ABC):
    def __init__(self, scheduler): 
        self.scheduler = scheduler

    # This method will be called whenever there is no process currently running
    @abstractmethod
    def noProcessRunning(self) -> None:
        pass

    # This method will be called whenever a new process is activated
    @abstractmethod
    def processActivated(self, process) -> None:
        pass

    # This method will be called at every iteration to handle the time quanta
    @abstractmethod
    def handleTimeQuanta(self, process) -> None:
        pass

    # This method will be called when a process has to wait for I/O
    @abstractmethod
    def processWaiting(self, process) -> None:
        pass
    
    # This method will be called when a process has finished waiting for I/O
    @abstractmethod
    def processFinishedIO(self, process) -> None:
        pass

    # This method will be called when a process terminates execution
    @abstractmethod
    def processTerminated(self, process) -> None:
        pass


class FirstComeFirstServe(SchedulingAlgorithm):
    def __init__(self, scheduler):
        super().__init__(scheduler)

        self.readyQueue = []

    # This method will be called whenever there is no process currently running
    def noProcessRunning(self) -> None:
        if self.readyQueue: # if not empty
            nextProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(nextProcess)

    # This method will be called whenever a new process is activated
    def processActivated(self, process) -> None:
        self.readyQueue.append(process)

    # This method will be called at every iteration to handle the time quanta   
    def handleTimeQuanta(self, process) -> None:
        pass

     # This method will be called when a process has to wait for I/O
    def processWaiting(self, process) -> None:
        if self.readyQueue: # if not empty
            nextProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(nextProcess)
            print('P' + str(self.scheduler.currentProcess.pid) + ' removed from ready queue and dispached to cpu')
        else:
            self.scheduler.currentProcess = None
    
    # This method will be called when a process has finished waiting for I/O
    def processFinishedIO(self, process) -> None:
        if process not in self.readyQueue:
            self.readyQueue.append(process)
            print('P' + str(process.pid) + ' appended in ready queue')


    # This method will be called when a process terminates execution
    def processTerminated(self, process) -> None:
        #print('P' + str(process.pid) + ' TERMINATED')
        if self.readyQueue: ### if not empty
            nextProcess = self.readyQueue.pop(0)
            self.scheduler.dispach(nextProcess)
        else:
            self.scheduler.currentProcess = None


class ShortestJobFirst(SchedulingAlgorithm):
    def __init__(self, scheduler):
        super().__init__(scheduler)

        self.readyQueue = []

    # This method will be called whenever there is no process currently running
    def noProcessRunning(self) -> None:
        if self.readyQueue: # if not empty
            nextProcess = self.__chooseLowestBurstTime()
            if nextProcess:
                self.scheduler.dispach(nextProcess)

    # This method will be called whenever a new process is activated
    def processActivated(self, process) -> None:
        self.readyQueue.append(process)

    # This method will be called at every iteration to handle the time quanta
    def handleTimeQuanta(self, process) -> None:
        pass

     # This method will be called when a process has to wait for I/O
    def processWaiting(self, process) -> None:
        if self.readyQueue: # if not empty
            nextProcess = self.__chooseLowestBurstTime()
            if nextProcess:
                self.scheduler.dispach(nextProcess)
                print('P' + str(self.scheduler.currentProcess.pid) + ' removed from ready queue and dispached to cpu')
        else:
            self.scheduler.currentProcess = None
    
    # This method will be called when a process has finished waiting for I/O
    def processFinishedIO(self, process) -> None:
        if process not in self.readyQueue:
            self.readyQueue.append(process)
            print('P' + str(process.pid) + ' appended in ready queue')


    # This method will be called when a process terminates execution
    def processTerminated(self, process) -> None:
        #print('P' + str(process.pid) + ' TERMINATED')
        if self.readyQueue: ### if not empty
            nextProcess = self.__chooseLowestBurstTime()
            if nextProcess:
                self.scheduler.dispach(nextProcess)
        else:
            self.scheduler.currentProcess = None

    def __chooseLowestBurstTime(self) -> Process:
        if self.readyQueue:
            lowestBurstTimeProcess = self.readyQueue[0]
            index = 0
            for i, process in enumerate(self.readyQueue):
                if process.simulationData[process.currentCycle] < lowestBurstTimeProcess.simulationData[lowestBurstTimeProcess.currentCycle]:
                    lowestBurstTimeProcess = process
                    index = i
                    #return self.readyQueue.pop(i)
            return self.readyQueue.pop(index)
        else:
            return None

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
                self.readyQueue.append(process)
                if self.readyQueue:
                    newProcess = self.readyQueue.pop(0)
                    self.scheduler.dispach(newProcess)

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



class MultilevelFeedbackQueue(SchedulingAlgorithm):
    def __init__(self, scheduler):
        super().__init__(scheduler)

        self.readyQueue_1 = []
        self.algorithm_1 = RoundRobin()
        self.algorithm_1.timeQuanta = 5


        self.readyQueue_2 = []
        self.algorithm_2 = RoundRobin()
        self.algorithm_2.timeQuanta = 10


        self.readyQueue_3 = []
        self.algorithm_3 = FirstComeFirstServe()


    # This method will be called whenever there is no process currently running
    def noProcessRunning(self) -> None:
        if self.readyQueue_1: # if not empty
            self.algorithm_1.noProcessRunning()
        else:
            if self.readyQueue_2:
                self.algorithm_2.noProcessRunning()
            else:
                if self.readyQueue_3:
                    self.algorithm_3.noProcessRunning()

    # This method will be called whenever a new process is activated
    def processActivated(self, process) -> None:
        pass

    # This method will be called at every iteration to handle the time quanta
    def handleTimeQuanta(self, process) -> None:
        self.algorithm_1.handleTimeQuanta()
        self.algorithm_2.handleTimeQuanta()

     # This method will be called when a process has to wait for I/O
    def processWaiting(self, process) -> None:
        pass
    
    # This method will be called when a process has finished waiting for I/O
    def processFinishedIO(self, process) -> None:
        pass


    # This method will be called when a process terminates execution
    def processTerminated(self, process) -> None:
        pass