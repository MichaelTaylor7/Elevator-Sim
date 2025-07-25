# The Elevator Coding Challenge

Provide code that simulates an elevator.

### Elevator Capacity

Assuming infinite capacity unless told otherwise

### Elevator/Building Floors

Defaulting to 10 floors (floor 0 through 9)
**weekend goal -- floors are dynamic, accept any # of floors

### Request Handling

Simulating floor queue as list of integers
##weekend goal -- allow live input using CLI

### Elevator Movement

Elevator moves one floor per unit time, elevator cannot teleport

### No GUI

Simulation runs in CLI, actions printed

### Prioritization of direction

Currently handling as FIFO
###Logic Notes
Don't SSTF, leads to starvation
LOOK is more efficient than SCAN, ends at last step of direction instead of at the end of that direction

###Remaining Tasks
**weekend goal -- update to LOOK
**weekend goal -- multiple elevators/elevator systemt
**weekend goal -- modularize code
**weekend goal -- containerize w/ Docker
