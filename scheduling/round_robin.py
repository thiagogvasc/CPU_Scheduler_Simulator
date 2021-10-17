from scheduling.utils.functions import CPU_Idle
from scheduling.utils.functions import getFirstFromQueue
from scheduling.utils.functions import finishedIO
from scheduling.utils.functions import hasToDoIO


class RoundRobin():
    def __init__(self, cpu):
        self.cpu = cpu

        self.readyQueue = []
        self.doingIO = []

        self.timeQuanta = 5

    def update(self):
        if self.cpu.currentProcess:
            print(self.cpu.currentProcess.pid)
        else:
            print('NO PROCESS RUNNING')

        # Keep track of processes doing I/O
        if hasToDoIO(self.cpu.currentProcess):
            self.doingIO.append(self.cpu.currentProcess)

        # If CPU is idle, then select next process from the ready queue
        if CPU_Idle(self.cpu.currentProcess):
            print('CPU IDLE')
            self.cpu.dispach(getFirstFromQueue(self.readyQueue))
        else:
            if self.cpu.currentProcess.timeRunning >= self.timeQuanta:
                preemptedProcess = self.cpu.preempt()
                self.readyQueue.append(preemptedProcess)
                self.cpu.dispach(getFirstFromQueue(self.readyQueue))

        # If process finished doing I/O, then move it to the ready queue
        for i, process in enumerate(self.doingIO):
            if finishedIO(process):
                self.doingIO.pop(i)
                self.readyQueue.append(process)
        

    def addProcess(self, process):
        self.readyQueue.append(process)