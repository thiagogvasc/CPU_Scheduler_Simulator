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

        self.doingIO = []

        self.timeQuanta = 5

    def update(self):
        if self.cpu.currentProcess:
            print(self.cpu.currentProcess.pid)
        else:
            print('NO PROCESS RUNNING')

        for process in self.readyQueue_1:
            print(str(process.pid) + ', ', end="")
        print()
        for process in self.readyQueue_2:
            print(str(process.pid) + ', ', end="")
        print()
        for process in self.readyQueue_3:
            print(str(process.pid) + ', ', end="")
        print()
        print('doing io: ')
        for process in self.doingIO:
            print(str(process.pid) + ', ', end="")
        print()

        # Keep track of processes doing I/O
        if hasToDoIO(self.cpu.currentProcess):
            if self.cpu.currentProcess not in self.doingIO:
                self.doingIO.append(self.cpu.currentProcess)

        # If CPU is idle, then select next process from the ready queue 1
        if CPU_Idle(self.cpu.currentProcess):
            print('CPU IDLE')
          
            if self.readyQueue_1:
                self.cpu.dispach(getFirstFromQueue(self.readyQueue_1))
            else:
                if self.readyQueue_2:
                    self.cpu.dispach(getFirstFromQueue(self.readyQueue_2))   
                else:
                    if self.readyQueue_3:
                        self.cpu.dispach(getFirstFromQueue(self.readyQueue_3))
        else:
            if self.cpu.currentProcess.priority < 3:

                if self.cpu.currentProcess.priority == 1:
                    if self.cpu.currentProcess.timeRunning >= self.timeQuanta_1:
                        preemptedProcess = self.cpu.preempt()
                        if preemptedProcess.priority < 3:
                            preemptedProcess.priority += 1
                            print('Reduced priority')

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
        for i, process in enumerate(self.doingIO):
            if finishedIO(process):
                self.doingIO.pop(i)

                if process.priority == 1:
                    self.readyQueue_1.append(process)
                elif process.priority == 2:
                    self.readyQueue_2.append(process)
                elif process.priority == 3:
                    self.readyQueue_3.append(process)
            

    def addProcess(self, process):
        self.readyQueue_1.append(process)