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
