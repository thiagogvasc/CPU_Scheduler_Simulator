from process import State


class CPU():
    def __init__(self):
        self.currentProcess = None

        self.timeQuanta = None

    def dispach(self, process):
        self.currentProcess = process
        if process:
            self.currentProcess.setState(State.RUNNING)

    def preempt(self):
        if self.currentProcess:
            self.currentProcess.preempt()
            self.currentProcess.setState(State.READY)
            preemptedProcess = self.currentProcess
            self.currentProcess = None
            return preemptedProcess
        return None

    def timeout(self, timeQuanta):
        pass