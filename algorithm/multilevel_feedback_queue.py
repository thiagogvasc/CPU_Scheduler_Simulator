from algorithm.abstract.scheduling_algorithm import SchedulingAlgorithm
from algorithm.round_robin import RoundRobin
from algorithm.first_come_first_serve import FirstComeFirstServe 


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