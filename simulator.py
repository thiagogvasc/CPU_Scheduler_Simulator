from cpu import CPU
from simulation import Simulation

from scheduling.first_come_first_serve import FirstComeFirstServe
from scheduling.shortest_job_first import ShortestJobFirst
from scheduling.multilevel_feedback_queue import MultilevelFeedbackQueue


class Simulator:
    def __init__(self, data):
        self.cpu = CPU()

        self.FCFS_Simulation = Simulation(data, self.cpu, FirstComeFirstServe(self.cpu))
        self.SJF_Simulation = Simulation(data, self.cpu, ShortestJobFirst(self.cpu))
        self.MLFQ_Simulation = Simulation(data, self.cpu, MultilevelFeedbackQueue(self.cpu))

    ### Simulation Engine
    def runSimulations(self):
        self.FCFS_Simulation.run()
        self.SJF_Simulation.run()
        self.MLFQ_Simulation.run()