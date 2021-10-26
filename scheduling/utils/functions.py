from process import Process
from process import State

##### Helper Functions #####

def processWaiting(process: Process) -> bool:
    return process.state == State.WAITING

def hasToDoIO(process: Process) -> bool:
    if process:
        if processWaiting(process):
            return True
        else:
            return False
    else:
        return False


def finishedIO(process: Process) -> bool:
    return process.state == State.READY

def CPU_Idle(currentProcess: Process) -> bool:
    if currentProcess: # if not none
        if currentProcess.state == State.WAITING or currentProcess.state == State.TERMINATED:
            return True
        else: 
            return False
    else:
        return True

def getFirstFromQueue(readyQueue: list) -> Process:
    if readyQueue:
        newProcess = readyQueue.pop(0)
        return newProcess
    else:
        return None

def getShortesBurstFromQueue(readyQueue: list) -> Process:
    if readyQueue:
        lowestBurstTimeProcess = readyQueue[0]
        index = 0
        for i, process in enumerate(readyQueue):
            if process.simulationData[process.currentBurst] < lowestBurstTimeProcess.simulationData[lowestBurstTimeProcess.currentBurst]:
                lowestBurstTimeProcess = process
                index = i
                #return self.readyQueue.pop(i)
        return readyQueue.pop(index)
    else:
        return None