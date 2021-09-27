COP 4610 - Programming Assignment

Comparison of CPU Schedulers

 Project objective: To learn more about OS scheduling through a hands-on simulation programming experience

Implement the following 3 CPU scheduling algorithms

Simulate and evaluate each with the set of eight processes below.
Use any programming language. The program listing should be submitted with the report.
FCFS non-preemptive (partial results provided)
SJF non-preemptive
MLFQ
Multilevel Feedback Queue (absolute priority in higher queues)

            Queue 1 uses RR scheduling with Tq = 5

            Queue 2 uses RR scheduling with Tq = 10

            Queue 3 uses FCFS

All processes enter first queue 1. If time quantum (Tq) expires before CPU burst is complete, the process is downgraded to next lower priority queue. Processes are not downgraded when preempted by a higher queue level process. Once a process has been downgraded, it will not be upgraded.

Assumptions:

All processes are activated at time 0
Assume that no process waits on I/O devices.
After completing an I/O event, a process is transferred to the ready queue.
Waiting time is accumulated while a process waits in the ready queue.
Turnaround time is a total of (Waiting time) + (CPU burst time) + (I/O time)
Response time is the first measure of waiting time from arrival at time 0 until the first time on the CPU.
 

Process Data: process goes {CPU burst, I/O time, CPU burst, I/O time, CPU burst, I/O time,…….., last CPU burst}

P1 {5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 5}

P2 {4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8}

P3 {8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6}

P4 {3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3}

P5 {16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4}

P6 {11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8}

P7 {14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10}

P8 {4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6}

Simulation completed for FCFS (see results in table below).

Presentation of results:

Write the simulation program in a programming language (such as C, C++, C#, Java, Python, or any other language).

 

Submit REPORT: Write a well-organized report, which will include:

Table of Content
Introduction
General flow chart (logic) of the simulation program
Well-presented final results including tables and discussion
Discussion and Tables (see below) for
U (CPU utilization),
Tw (waiting times)
Ttr (turnaround times),
Tr (response times)
 for all processes and averages for each algorithm (see FCFS below)

Compare results SJF, FCFS, MLFQ
Sample of dynamic execution (program output)  
---This information should be displayed for each context switch

Current Execution time
Running process
The Ready queue, with the CPU burst time for each process
The Processes in I/O with the remaining time for every process for its I/O burst completion
Indicate when a process has completed its total execution.
Results printed at the end of each simulation
This information should be displayed at the end of each simulation

Total time needed to complete all 8 processes.
CPU utilization - [%] (U).
Waiting times for each process and the average waiting time for all processes (Tw)
Turnaround time for each process and the average turnaround time.(Ttr)
Response time for each process and the average response time (Tr).
Well commented source code
The grading will be based on the following

(1) Program structure and organization

(2) Overall report

(3) Final results and discussion

 

Table of results comparison (SJF, FCFS, MLFQ)


                            SJF         FCFS            MLFQ\
CPU utilization                         85.34%
Avg Waiting time (Tw)                   185.25
Avg Turnaround time (Ttr)               521.37
Avg Response time (Tr)                  24.37


 |              SJF              |       FCFS           |             MLFQ	|
|-------------------------------|---------------------|-----------------------|
 | Process ID |      Tw   |   Ttr  |   Tr    |   Tw  |   Ttr  |   Tr     |     Tw    |  Ttr    | Tr   | 
|------------|--------|----------|-------|--------|-----------|---------|----------|-------|--------|
|P1 | | | |                       170|     395|     0| | | | 
P2                              164     591     5
P3                              165     557     9
P4                              164     648     17
P5                              221     530     20
P6                              230     445     36
P7                              184     512     47
P8                              184     493     61

Avg                             185.25  521.37  24.37