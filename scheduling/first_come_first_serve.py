from scheduling.utils.functions import CPU_Idle
from scheduling.utils.functions import getFirstFromQueue
from scheduling.utils.functions import finishedIO
from scheduling.utils.functions import hasToDoIO

class FirstComeFirstServe():

    def __init__(self, cpu):
        self.cpu = cpu

        self.readyQueue = []
        self.processesDoingIO = []
 
    def update(self):
       # self.cpu.printCurrentProcess()

        # Keep track of processes doing I/O
        if hasToDoIO(self.cpu.currentProcess):
            if self.cpu.currentProcess not in self.processesDoingIO:
                self.processesDoingIO.append(self.cpu.currentProcess) 

        # If CPU is idle, then select next process from the ready queue
        if CPU_Idle(self.cpu.currentProcess):
            self.cpu.dispach(getFirstFromQueue(self.readyQueue))

        # If process finished doing I/O, then move it to the ready queue
        # Dispach to the CPU if ready queue was empty
        for i, process in enumerate(self.processesDoingIO):
            if finishedIO(process):
                self.processesDoingIO.pop(i)
                self.readyQueue.append(process)
                if len(self.readyQueue) == 1 and CPU_Idle(self.cpu.currentProcess):
                    self.cpu.dispach(getFirstFromQueue(self.readyQueue))
    
    def addProcess(self, process):
        self.readyQueue.append(process)

    def printQueues(self):
        print('Ready Queue: ', end='')
        for process in self.readyQueue:
            print('P' + str(process.pid) + '  ', end='')
        print()

        print('Doing I/O: ', end='')
        for process in self.processesDoingIO:
            print('P' + str(process.pid) + '  ', end='')
        print()
