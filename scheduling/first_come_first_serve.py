from process import State

from scheduling.utils.functions import CPU_Idle
from scheduling.utils.functions import getFirstFromQueue
from scheduling.utils.functions import processWaiting
from scheduling.utils.functions import finishedIO

class FirstComeFirstServe():

    def __init__(self, cpu):
        self.cpu = cpu

        self.processes = []
        self.readyQueue = []
        self.doingIO = []

        self.time = 0

    def update(self):
        print('TIME: ' + str(self.time))
        for process in self.processes:
            process.update()

        if self.cpu.currentProcess:
            print(self.cpu.currentProcess.pid)
        else:
            print('NO PROCESS RUNNING')

        if self.cpu.currentProcess:
            if processWaiting(self.cpu.currentProcess):
                self.doingIO.append(self.cpu.currentProcess)

        if CPU_Idle(self.cpu.currentProcess):
            print('CPU IDLE')
            self.cpu.dispach(getFirstFromQueue(self.readyQueue))

        for i, process in enumerate(self.doingIO):
            if finishedIO(process):
                self.doingIO.pop(i)
                self.readyQueue.append(process)
    # before preemtping save state of cpu.curretnProcess

        self.time += 1

        for process in self.processes:
            if process.state == State.READY:
                process.totalWaitingTime += 1

    def addProcess(self, process):
        self.readyQueue.append(process)
        self.processes.append(process)