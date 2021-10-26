from process import Process
from process import State

class Simulation:
    def __init__(self, data, cpu, scheduling):
        self.data = data
        self.cpu = cpu
        self.scheduling = scheduling

        self.processes = []

        ### Initiate all processes at the same time since they all arrive at t = 0
        for i, processSimulationData in enumerate(data):
            process = Process(i + 1, processSimulationData)
            self.scheduling.addProcess(process)
            self.processes.append(process)

        self.time = 0
        self.totalRunningTime = 0


    # Check if all processes terminated
    def terminated(self):
        for process in self.processes:
            if process.state != State.TERMINATED:
                return False
        return True

    ### Simulation Loop
    def run(self):

        # Stop only if all processes terminated
        while not self.terminated():

            # Update process state
            for process in self.processes:
                process.update()

            # Update scheduling state
            self.scheduling.update()     

            ### Print formatted data
            if (self.cpu.contextSwitch or self.terminated()):
                print('Time: ' + str(self.time))
                print('{:20}'.format('Process ID'), end='')
                print('{:20}'.format('Burst Type'), end='')
                print('{:20}'.format('Burst TIme'), end='')
                print('{:20}'.format('Remaining Time'), end='')
                print('{:20}'.format('State'), end='')
                print()
                for process in self.processes:
                    process.print()
                self.cpu.contextSwitch = False
                self.scheduling.printQueues()
                print('----------------------------------------------------------------------------------------------')

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
            # print('-----------------------------------------')

            ### Track total running time
            if self.cpu.currentProcess:
                if self.cpu.currentProcess.state == State.RUNNING:
                    self.totalRunningTime += 1

            self.time += 1


        ### Compute results after simulation is finished

        print('Results:')
        waitingTimeSum = 0
        turnaroundTimeSum = 0
        responseTimeSum = 0

        ### Print formatted data

        print('{:20}'.format('Process ID'), end='')
        print('{:20}'.format('Tw (Waiting)'), end='')
        print('{:20}'.format('Ttr (Turnaround)'), end='')
        print('{:20}'.format('Tr (Response)'), end='')
        print()

        for process in self.processes:
            print('{:20}'.format('P' + str(process.pid)), end='')
            print('{:20}'.format(str(process.totalWaitingTime)), end='')
            print('{:20}'.format(str(process.turnaroundTime)), end='')
            print('{:20}'.format(str(process.responseTime)), end='')
            print()

            waitingTimeSum += process.totalWaitingTime
            turnaroundTimeSum += process.turnaroundTime
            responseTimeSum += process.responseTime
            
        print('{:20}'.format('Average'), end='')
        print('{:20}'.format(str(waitingTimeSum / 8)), end='')
        print('{:20}'.format(str(turnaroundTimeSum / 8)), end='')
        print('{:20}'.format(str(responseTimeSum / 8)), end='')

        print()
        print()

        print('CPU Utilization: ', end='')
        print(self.totalRunningTime/(self.time - 1) * 100)

        print('Total time to finish all processes: ', end='')
        print(self.time - 1 )