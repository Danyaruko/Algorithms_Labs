# Lab-5

## Task

    Impelement Kruskal's algortithm for finding the Minimum Spanning Tree

---

## Input

    Undirected and connected graph

---

## Output

    List of edges that comprise minimum spanning tree

---

## Algorithm

1.Sort the edges of the graph by weight
2.Choose the edge with the lowest weight and add it to the minimum spanning tree if it doesn't create a loop, in my implementation I maintain a set of vertices that are in the minimum spanning tree to check for it  
3.Repeat second step until all edges are checked

<b>Complexity = O(E\*logV)</b>

---

## How to run

- `cd` into folder where you want to store this repository
- Download zip-version of repository and unpack to your desired folder
- Go into folder with files with command `cd Algorithms_Labs/Lab_5`
- run command `python3 -m unittest test.py` on Mac/Linux _or_ `py -m unittest test.py` on Windows, there is also an example in `kruskals_algorithm.py`
