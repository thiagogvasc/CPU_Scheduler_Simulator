from process import State


class Scheduler:
    def __init__(self):
        self.processes = []
        self.currentProcess = None

        self.algorithm = None

        #self.currentProcessRunningTime = 0    move this to process class

    def update(self):

        self.algorithm.handleTimeQuanta(self.currentProcess)


        # If there is no process currently running
        if self.currentProcess is None:
            self.algorithm.noProcessRunning()

        # If there is a process running
        else:

            # If current process has to do I/O
            if self.currentProcess.previousState == State.RUNNING and self.currentProcess.state == State.WAITING:
                self.algorithm.processWaiting(self.currentProcess)


        # Iterate through all processes
        for process in self.processes:

            # If process finished with I/O
            if process.previousState == State.WAITING and process.state == State.READY:
                self.algorithm.processFinishedIO(process)

            # If process terminated
            if process.previousState == State.RUNNING and process.state == State.TERMINATED:
                self.algorithm.processTerminated(process)

        # Update the state of all processes
        for process in self.processes:
            process.update() # add more boolean variables to make sure results are calculated properly


    # Dispach a process to the cpu / change process state to RUNNING
    def dispach(self, process):
        self.currentProcess = process
        self.currentProcess.setState(State.RUNNING)

    # Activate a process
    def addProcess(self, process):
        self.processes.append(process)
        self.algorithm.processActivated(process)