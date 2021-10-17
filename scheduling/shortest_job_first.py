from scheduling.abstract.scheduling_algorithm import SchedulingAlgorithm
from process import Process


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