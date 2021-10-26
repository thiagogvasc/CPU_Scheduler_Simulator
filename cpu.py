from process import State


class CPU():
    def __init__(self):
        self.currentProcess = None

        self.contextSwitch = True

    def dispach(self, process):
        self.currentProcess = process
        if process:
            self.currentProcess.setState(State.RUNNING)
            self.contextSwitch = True

    def preempt(self):
        if self.currentProcess:
            self.currentProcess.setState(State.READY)
            preemptedProcess = self.currentProcess
            self.currentProcess = None
            return preemptedProcess
        return None

    def printCurrentProcess(self):
        if self.currentProcess:
            print(self.currentProcess.pid)
        else:
            print('NO PROCESS RUNNING')