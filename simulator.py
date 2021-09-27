from scheduler import Scheduler
from process import Process
from process import State


class Simulator:
    def __init__(self, data):
        self.data = data
        self.processes = []


        ### Instantiate all processes with the corresponding simulation data
        i = 1 # Process id
        for processSimulationData in data:
            self.processes.append(Process(i, processSimulationData))
            i += 1

        self.scheduler = Scheduler(self.processes)

    def allTerminated(self):
        for process in self.processes:
            if process.state != State.TERMINATED:
                return False
        return True

    ### Simulation Engine
    def run(self):

        ### Main loop
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