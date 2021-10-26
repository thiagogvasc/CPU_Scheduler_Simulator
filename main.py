from simulator import Simulator


p1SimulationData = [5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 5]
p2SimulationData = [4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8]
p3SimulationData = [8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6]
p4SimulationData = [3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3]
p5SimulationData = [16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4]
p6SimulationData = [11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8]
p7SimulationData = [14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10]
p8SimulationData = [4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6]

simulationData = [p1SimulationData, p2SimulationData,
                  p3SimulationData, p4SimulationData, 
                  p5SimulationData, p6SimulationData, 
                  p7SimulationData, p8SimulationData]


simulator = Simulator(simulationData)
simulator.runSimulations()
