Bianca Martinez
CST560 Advanced Algorithm Design and Analysis
Activity 6.2 Integrated Algorithm System

==================================================
INTRODUCTION
==================================================

This project combines five algorithms developed
throughout the course into one integrated system.
The project is based on my Iris & Friends Care
Tracker concept and demonstrates how different
algorithmic approaches can work together to solve
a larger problem.

The system identifies cats requiring care,
assigns resources, selects high-priority care
tasks, schedules appointments, and finds the
shortest travel route between locations.

==================================================
SYSTEM OVERVIEW
==================================================

Algorithm 1: Recursion
Purpose:
Counts the number of cats requiring care.

Algorithm 2: Backtracking
Purpose:
Assigns tasks to available resources while
respecting workload constraints.

Algorithm 3: Dynamic Programming
Purpose:
Selects the highest-priority tasks while staying
within a limited amount of available time.

Algorithm 4: Greedy Algorithm
Purpose:
Schedules the maximum number of non-overlapping
appointments.

Algorithm 5: Graph Algorithm
Purpose:
Uses Dijkstra's Algorithm to find the shortest
travel route between locations.

==================================================
DATA FLOW DIAGRAM
==================================================

Recursion
    |
    V
Backtracking
    |
    V
Dynamic Programming
    |
    V
Greedy Scheduling
    |
    V
Graph Routing
    |
    V
Final Care Plan

==================================================
TEST SCENARIOS
==================================================

Scenario 1:
Normal system execution using all modules
with valid inputs.

Scenario 2:
Edge-case testing including:
- Empty lists
- Limited time
- Unknown locations
- Disconnected graphs

==================================================
RUNTIME ANALYSIS
==================================================

Recursion Module
Time Complexity: O(n)

Backtracking Module
Time Complexity: O(d^n)

Dynamic Programming Module
Time Complexity: O(n * W)

Greedy Module
Time Complexity: O(n log n)

Graph Module
Time Complexity: O((V + E) log V)

The Backtracking module is the most expensive
component because it may explore multiple
assignment combinations. The Dynamic Programming
module avoids recomputation through memoization
and tabulation, while the Greedy and Graph
algorithms provide efficient solutions for
scheduling and routing.

==================================================
DESIGN STATEMENT
==================================================

For this final project, I integrated the five
algorithms developed throughout the course into
a single system based on my Iris & Friends Care
Tracker project. I kept the modules separate to
make the program easier to read, test, and
maintain. Each algorithm performs a specific
task and passes information to the next stage of
the process.

The project begins by counting cats requiring
care, then assigns resources, selects important
tasks, schedules appointments, and finally finds
the shortest travel route. Throughout the
project I incorporated instructor feedback from
previous assignments, including additional test
cases, improvements to the MRV heuristic, and an
edge-relaxation example for Dijkstra's Algorithm.

I used Python and Visual Studio Code to develop,
test, and debug the system. This project helped
me better understand how different algorithmic
approaches can work together within a larger
software solution.