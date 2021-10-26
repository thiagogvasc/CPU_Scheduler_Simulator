from scheduling.utils.functions import CPU_Idle
from scheduling.utils.functions import getFirstFromQueue
from scheduling.utils.functions import finishedIO
from scheduling.utils.functions import hasToDoIO


class MultilevelFeedbackQueue():
    def __init__(self, cpu):
        self.cpu = cpu

        self.readyQueue_1 = []
        self.timeQuanta_1 = 5

        self.readyQueue_2 = []
        self.timeQuanta_2 = 10

        self.readyQueue_3 = []

        self.processesDoingIO = []

        self.timeQuanta = 5

    def update(self):

        # Keep track of processes doing I/O
        if hasToDoIO(self.cpu.currentProcess):
            if self.cpu.currentProcess not in self.processesDoingIO:
                self.processesDoingIO.append(self.cpu.currentProcess)

        # If CPU is idle, then select next process from the ready queue 1
        if CPU_Idle(self.cpu.currentProcess):        
            if self.readyQueue_1:
                self.cpu.dispach(getFirstFromQueue(self.readyQueue_1))
            else:
                if self.readyQueue_2:
                    self.cpu.dispach(getFirstFromQueue(self.readyQueue_2))   
                else:
                    if self.readyQueue_3:
                        self.cpu.dispach(getFirstFromQueue(self.readyQueue_3))
        else: ### Not Idle

            #### Check if time quata expired for priorities 1 and 2
            if self.cpu.currentProcess.priority < 3:

                ### If priority = 1, then check if the time quanta (5) is expired
                ### Dispach next process to the cpu if time quanta expired
                if self.cpu.currentProcess.priority == 1:
                    if self.cpu.currentProcess.timeRunning >= self.timeQuanta_1:
                        preemptedProcess = self.cpu.preempt()
                        if preemptedProcess.priority < 3:
                            preemptedProcess.priority += 1
                           
                        if preemptedProcess.priority == 2:
                            self.readyQueue_2.append(preemptedProcess)
                        elif preemptedProcess.priority == 3:
                            self.readyQueue_3.append(preemptedProcess)

                    
                        if self.readyQueue_1:
                            self.cpu.dispach(getFirstFromQueue(self.readyQueue_1))
                        else:
                            if self.readyQueue_2:
                                self.cpu.dispach(getFirstFromQueue(self.readyQueue_2))   
                            else:
                                if self.readyQueue_3:
                                    self.cpu.dispach(getFirstFromQueue(self.readyQueue_3))

                ### If priority = 2, then check if the time quanta (10) is expired
                ### Dispach next process to the cpu if time quanta expired
                elif self.cpu.currentProcess.priority == 2:
                    if self.cpu.currentProcess.timeRunning >= self.timeQuanta_1:
                        preemptedProcess = self.cpu.preempt()
                        if preemptedProcess.priority < 3:
                            preemptedProcess.priority += 1

                        if preemptedProcess.priority == 2:
                            self.readyQueue_2.append(preemptedProcess)
                        elif preemptedProcess.priority == 3:
                            self.readyQueue_3.append(preemptedProcess)

                    
                        if self.readyQueue_1:
                            self.cpu.dispach(getFirstFromQueue(self.readyQueue_1))
                        else:
                            if self.readyQueue_2:
                                self.cpu.dispach(getFirstFromQueue(self.readyQueue_2))   
                            else:
                                if self.readyQueue_3:
                                    self.cpu.dispach(getFirstFromQueue(self.readyQueue_3))

        # If process finished doing I/O, then move it to the ready queue
        # Dispach to the CPU if ready queue was empty
        for i, process in enumerate(self.processesDoingIO):
            if finishedIO(process):
                self.processesDoingIO.pop(i)

                if process.priority == 1:
                    self.readyQueue_1.append(process)
                elif process.priority == 2:
                    self.readyQueue_2.append(process)
                elif process.priority == 3:
                    self.readyQueue_3.append(process)

                if len(self.readyQueue_1) == 1 and CPU_Idle(self.cpu.currentProcess):
                    self.cpu.dispach(getFirstFromQueue(self.readyQueue_1))
                else:
                    if len(self.readyQueue_2) == 1 and CPU_Idle(self.cpu.currentProcess):
                        self.cpu.dispach(getFirstFromQueue(self.readyQueue_2))   
                    else:
                        if len(self.readyQueue_3) == 1 and CPU_Idle(self.cpu.currentProcess):
                            self.cpu.dispach(getFirstFromQueue(self.readyQueue_3))
            

    def addProcess(self, process):
        self.readyQueue_1.append(process)

    def printQueues(self):
        print('Ready Queue 1: ', end='')
        for process in self.readyQueue_1:
            print('P' + str(process.pid) + '  ', end='')
        print()

        print('Ready Queue 2: ', end='')
        for process in self.readyQueue_2:
            print('P' + str(process.pid) + '  ', end='')
        print()

        print('Ready Queue 3: ', end='')
        for process in self.readyQueue_3:
            print('P' + str(process.pid) + '  ', end='')
        print()

        print('Doing I/O: ', end='')
        for process in self.processesDoingIO:
            print('P' + str(process.pid) + '  ', end='')
        print()