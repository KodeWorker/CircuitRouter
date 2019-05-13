# Circuit Router v0.0.1
## The Project Goal

**(2019/05/10)**

This project is a test ground for a general circuit router.
Back in 2018, I started working on path finding problems to aid the PCB circit designers in my company.
PCB circuit line can walk diagonally rather than horizonally/vertically in VLSI design.
The first thing came to my mind was a very simple A* path finding algorithm as a circuit router (ref. 1).
And there are many difficulties to come.
 
Tie-breaking technique can help accelerating the A* routing process (ref 2). 
Octagon-shaped obstacles, diagonal distance as heuristic and pre-defined midpoints can achieve more likable routes.
The computation of A* is quite intuitive and fast but memory comsumption is the pain in the ass.
I tried many workarounds, for an example, the graph only records few recently compolished routes.
However, the problems remained.

Recently I've read many papers about circuit routing.
Global and detailed routing (ref. 3) hints two phase routing mechanism with different scales can be a possible solution.
Multithreaded Collision-Aware Global Routing with Bounded-Length Maze Routing (ref. 4) and Negotiation-Based Maze Routing tried to solve the resource sharing (route blockage) problems.
Some articles also said that planning can help accelerating whole routing process.

This time, I'll build the circuit router from scratch and see how it ends.

## Dev Log
- 2019/05/09 initialtion
- 2019/05/10 add lincese, basic A* algorithm, 4-direction grid, 8-direction graph, and their unit tests
- 2019/05/10 add shapes for graph obstacles
- 2019/05/13 unit tests for shapes

## Reference
1. https://www.redblobgames.com/pathfinding/a-star/implementation.html
2. http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
3. http://cc.ee.ntu.edu.tw/~ywchang/Courses/PD_Source/EDA_routing.pdf
4. https://ir.nctu.edu.tw/bitstream/11536/21646/1/000318163800005.pdf

## Clarification
- This project is only the implementation of academic concepts and all the technological details are not confidential.