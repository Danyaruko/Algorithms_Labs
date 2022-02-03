# Lab-6

## Task

Two participants play a lingustic game. At the start of the game the list of N words is given.
First player chooses any word w1 and crosses out any letter to form another word from the list w2. Then it is
turn of second player, who tries to do the same with the word w2.

The game finishes if remainig word has one letter, or if it is not possible to derive another word from the current one.

Define possible maximum word chain length in this game for a given word list.

---

## Input

The input file wchain.in consists of N + 1 lines.

- The first line contains N - number of words in the vocabulary, 1 ≤ N ≤ 10^5.
- Each of the next H lines contains a word with length in range from 1 to 50, which consists of lowercase Latin letters from a to z.

---

## Output

Output file wchain.out contains only one integer - the maximum word chain length.

---

## Algorithm

Since head-on formation of word chains is quite complex, we create a dictionary instead where each word from
vocabulary has an integer as a value that represents maximum length of a word chain that starts with this word(max len further), and then iterate through the vocabulary, deriving new words and seeing whether they are on the list. If they actually are, the max len of current word changes to max len of the new one plus one, if it is greater than the current max len. In the end, the highest max len would be the length of the longest word chain.

<b>Complexity = O(N \* L)</b>, where L - length of the longest word

---

## How to run

- `cd` into folder where you want to store this repository
- Download zip-archive of the repository and unpack it to your choosen folder
- Go into folder with files with command `cd Algorithms-Labs/Lab6`
- Insert input in a file `wchain.in`
- Run command `python3 wchain.py` on Mac/Linux or `py wchain.py` on Windows
- You will get output in `wchain.out`
