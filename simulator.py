#from scheduler import Scheduler
from process import Process
from process import State
from cpu import CPU

from scheduling.first_come_first_serve import FirstComeFirstServe
# from scheduling.shortest_job_first import ShortestJobFirst
# from scheduling.multilevel_feedback_queue import MultilevelFeedbackQueue
# from scheduling.round_robin import RoundRobin


class Simulator:
    def __init__(self, data):
        self.data = data
        self.scheduling = FirstComeFirstServe(CPU())

        self.processes = []

        for i, processSimulationData in enumerate(data):
            process = Process(i + 1, processSimulationData)
            self.scheduling.addProcess(process)
            self.processes.append(process)


    # Check if all processes terminated
    def allTerminated(self):
        for process in self.processes:
            if process.state != State.TERMINATED:
                return False
        return True

    ### Simulation Engine
    def run(self):

        # Stop only if all processes terminated
        while not self.allTerminated():
            print('-----------------------------------------')
            self.scheduling.update()     
            print('-----------------------------------------')



        ### Compute average times after simulation is finished

        print('Waiting time------------------------------------------------')
        waitingTimeSum = 0
        for process in self.processes:
            print('P' + str(process.pid) + ' ' + str(process.totalWaitingTime))
            waitingTimeSum += process.totalWaitingTime
        print('average: ' + str(waitingTimeSum / 8))

        print('Turnaround time----------------------------------------------')
        turnaroundTimeSum = 0
        for process in self.processes:
            print('P' + str(process.pid) + ' ' + str(process.turnaroundTime))
            turnaroundTimeSum += process.turnaroundTime
        print('average: ' + str(turnaroundTimeSum / 8))

        print('Response time------------------------------------------------')
        responseTimeSum = 0
        for process in self.processes:
            print('P' + str(process.pid) + ' ' + str(process.responseTime))
            responseTimeSum += process.responseTime
        print('average: ' + str(responseTimeSum / 8))