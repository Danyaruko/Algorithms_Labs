# Lab-4

## Task

Build directed and weighted graph from input and implement Dijkstra algorithm to find average distance from vertice **S**
to all available vertices

---

## Input

- First row contain two numbers **N**, **S**: **N** - amount of edges, 0 < N <= 10000; **S** - start vertice
- The next N rows contain 3 numbers - start of edge, end of edge and weight of edge, weight >= 0

---

## Output

Output contains only one number - average distance from vertice **S** to all available vertices

---

## Algorithm

1. Add start vertice to min priority queue, prioritized by distance
2. For every `cur_vertice` in queue do the following:
   - For every vertice with edge from `cur_vertice` to it:
     - Add to queue if not visited
     - Update distance with min value
   - Remove from queue

<b>Complexity = O(V + E\*logV),</b>
where V - number of vertices and E - number of edges

---

## How to run

- Download zip-archive of repository and unpack it wherever it is convenient to you
- Open command line and `cd` into folder with files, e.g. `cd C:\FolderWhereIPutLabs\Algorithms-Labs`
- Run command `python3 dijkstra.py` on Mac/Linux _or_ `py dijkstra.py` on Windows, _or_ use an IDE instead
