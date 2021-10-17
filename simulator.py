#from scheduler import Scheduler
from process import Process
from process import State
from cpu import CPU

from scheduling.first_come_first_serve import FirstComeFirstServe
from scheduling.shortest_job_first import ShortestJobFirst
from scheduling.round_robin import RoundRobin
from scheduling.multilevel_feedback_queue import MultilevelFeedbackQueue


class Simulator:
    def __init__(self, data):
        self.data = data
        self.scheduling = MultilevelFeedbackQueue(CPU())

        self.processes = []

        for i, processSimulationData in enumerate(data):
            process = Process(i + 1, processSimulationData)
            self.scheduling.addProcess(process)
            self.processes.append(process)

        self.time = 0


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
            print('Time: ' + str(self.time))

            # Update process state
            for process in self.processes:
                process.update()

            # Update algorithm and process state
            self.scheduling.update()     


            # Track simulation result
            for process in self.processes:
                ### Track waiting time
                if process.state == State.READY:
                    process.totalWaitingTime += 1

                ### Track turnaround time
                if process.state != State.TERMINATED:
                    process.turnaroundTime += 1

                ### Track response time
                if process.previousState == State.NEW and process.state == State.READY:
                    process.responseTime += 1
            print('-----------------------------------------')
            self.time += 1


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