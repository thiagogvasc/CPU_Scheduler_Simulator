from process import State


class Scheduler:
    def __init__(self, processes):
        self.processes = processes 
        self.readyQueue = list(processes)
        self.currentProcess = None

        self.algorithm = None

        #self.currentProcessRunningTime = 0    move this to process class

    def update(self):
        print('---------------------------------------------------------------------------------------------------')



        ### if shouldContextSwitch(self.readyQueue....)
        ###     self.currentPRocess = self.algorithm.getNextProcess(self.readyQueue)



        # Dispach a process in the ready queue if there is none running
        if self.currentProcess is None: 
            if self.readyQueue: # if not empty
                #self.currentProcess = self.readyQueue.pop(0)
                self.currentProcess = self.algorithm.getNextProcess(self.readyQueue)
                self.currentProcess.setState(State.RUNNING)


        # If there is already a process running, check if the process needs to do I/O
        # If the process needs to do I/O, remove from the cpu and dispach another process 
        #   from the ready queue if it is not emtpy
        else:
            if self.currentProcess.state == State.WAITING and self.currentProcess.previousState == State.RUNNING:
                if self.readyQueue: # if not empty
                    #self.currentProcess = self.readyQueue.pop(0)
                    self.currentProcess = self.algorithm.getNextProcess(self.readyQueue)
                    print('P' + str(self.currentProcess.pid) + ' removed from ready queue and dispached to cpu')
                    self.currentProcess.setState(State.RUNNING)
                else:
                    self.currentProcess = None


        #### Check all processes if they are done with I/O, or if they were terminated
        for process in self.processes:
            if process.state == State.READY and process.previousState == State.WAITING:
                if process not in self.readyQueue:
                    self.readyQueue.append(process)
                    print('P' + str(process.pid) + ' appended in ready queue')
            

            #### ((FIX)) Move this section to the else statement above
            if process.state == State.TERMINATED and process.previousState == State.RUNNING:
                #print('P' + str(process.pid) + ' TERMINATED')
                if self.readyQueue: ### if not empty
                    #self.currentProcess = self.readyQueue.pop(0)
                    self.currentProcess = self.algorithm.getNextProcess(self.readyQueue)
                    self.currentProcess.setState(State.RUNNING)

        ### Print current running process
        if (self.currentProcess):
            print('Current running process: ' + 'P' + str(self.currentProcess.pid))
        else:
            print('Current running process: None')

        ### Print Ready Queue
        print('Ready Queue: ', end = '')
        for process in self.readyQueue:
            print(process.pid, end = ' ')
        if not self.readyQueue:
            print('Empty', end= '')

        print('') # new line
        

        for process in self.processes:
            process.update()  

        print('---------------------------------------------------------------------------------------------------')