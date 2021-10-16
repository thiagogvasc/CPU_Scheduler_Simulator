from process import Process
from process import State


def processWaiting(process: Process) -> bool:
    return process.state == State.WAITING

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
    pass

