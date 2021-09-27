# CPU_Scheduler_Simulator (In Progress...)
A CPU scheduling simulator for comparing different scheduling algorithms




This is an assignment for the Operating Systems (COP4610) class at Florida Atlantic University (FAU)
The assignment consists in buildling a simulator, in which three cpu scheduling algorithm will be run.
After the simulation, the average time, turnaround time, and response time of all processes will be comprared between the three algorithms

# How to test

1. Clone the repository at https://github.com/thiagogvasc/CPU_Scheduler_Simulator.git
2. Make sure Python is installed and added to the path environment variable
3. Run 'python main.py' on the command line

# Tentative Architecture (Draft)
-
 - Simulator
    - functions
        - main loop of application
        - calculate final results

    - data
        - reference to processes in the system
        - reference to the type of scheduler used


- Scheduler
    - functions
        - use the corresponding scheduling algorithm
        - update processes states
        - assign processes to cpu
        - manages the ready queue

    - data
        - reference to processes in the system
        - reference to the currently executing process
        - reference to the ready queue


- Process
    - functions
        - update state according to provided simulation data
        - track waiting time, reponse time and turnaround time

    - data
        - proccess id
        - simulation data
        - current state and previous state
        - waiting time, response time and turnaround time
--------------------------------------------------------------
