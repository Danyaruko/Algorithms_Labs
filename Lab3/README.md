# Laboratory work №3

Create an algorithm to solve the following task

## Farm

John the Farmer has built a new long cattle barn, of N (2 <= N <= 100,000) stables. Stables are located along a straight line in positionsx1, ..., xN (0 <= x-i <= 1 000 000 000).

His C (2 <= C <= N) cows do not like the new building and become aggressive towards each other, when they are placed in adjacent stables. To avoid situation, when cows might harm each other, farmer wants to place aggressive cows in stables in such a way, so that minimal distance between any of them was as big as possible. What is the biggest minimal distance?

Input is contained in a file, where:
First line contains two integers, separated with a comma: N and C
Next lines 2..N + 1: line i + 1 contains integer, that indicates number of a free stable x-і

Input:
5,3
1
2
8
4
9

Output:
3

###### Explanation:

Farmer has 5 cows, of them 3 are aggressive. They can be placed in stables 1, 4 and 8 or 1,4, 9. Thus, minimal value of maximum distance is 3

###### Hint:

As we have at least two cows, the best we can donis to place them in the barn in the first free stable and in the last

#### How to run:

You have to download zip-archive of the repository and unpack it wherever it is convenient to you, modify input.txt to desired extent while keeping the structure mentioned above, and run the farm.py in IDE. The answer can be found in output.txt
