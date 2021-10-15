from scheduler import Scheduler
from process import Process
from process import State

from algorithm.first_come_first_serve import FirstComeFirstServe
from algorithm.shortest_job_first import ShortestJobFirst
from algorithm.multilevel_feedback_queue import MultilevelFeedbackQueue


class Simulator:
    def __init__(self, data):
        self.data = data

        ### Instantiate all processes with the corresponding simulation data
        self.scheduler = Scheduler()
        self.scheduler.algorithm = ShortestJobFirst(self.scheduler)

        for i, processSimulationData in enumerate(data):
            self.scheduler.addProcess(Process(i + 1, processSimulationData))


    # Check if all processes terminated
    def allTerminated(self):
        for process in self.scheduler.processes:
            if process.state != State.TERMINATED:
                return False
        return True

    ### Simulation Engine
    def run(self):

        # Stop only if all processes terminated
        while not self.allTerminated():
            self.scheduler.update() 


        ### Compute average times after simulation is finished

        print('Waiting time------------------------------------------------')
        waitingTimeSum = 0
        for process in self.scheduler.processes:
            print('P' + str(process.pid) + ' ' + str(process.totalWaitingTime))
            waitingTimeSum += process.totalWaitingTime
        print('average: ' + str(waitingTimeSum / 8))

        print('Turnaround time----------------------------------------------')
        turnaroundTimeSum = 0
        for process in self.scheduler.processes:
            print('P' + str(process.pid) + ' ' + str(process.turnaroundTime))
            turnaroundTimeSum += process.turnaroundTime
        print('average: ' + str(turnaroundTimeSum / 8))

        print('Response time------------------------------------------------')
        responseTimeSum = 0
        for process in self.scheduler.processes:
            print('P' + str(process.pid) + ' ' + str(process.responseTime))
            responseTimeSum += process.responseTime
        print('average: ' + str(responseTimeSum / 8))