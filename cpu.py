from process import State


class CPU():
    def __init__(self):
        self.currentProcess = None

    def dispach(self, process):
        self.currentProcess = process
        if process:
            self.currentProcess.setState(State.RUNNING)

    def preempt(self):
        if self.currentProcess:
            self.currentProcess.preempt()
            self.currentProcess.setState(State.READY)
            #self.readyQueue.append(self.currentProcess)
            self.currentProcess = None