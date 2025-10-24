Student: Juan Fernando Hernández Arenas
Class number: 5730
Operating system: Windows 11 Pro
Programming language: Python 3.13.3
Tools used: Visual Studio Code, Python interpreter, Windows Terminal


Description

This project implements the DFA minimization algorithm described by Dexter Kozen in Automata and Computability at Lecture 14.
Given a deterministic finite automaton with no inaccessible states, the program identifies equivalent states and produces the list of pairs that can be collapsed to obtain a minimized automaton.


Input and Output Format

The program reads the DFA description and prints the equivalent state pairs, as required by the assignment.

Input format

c
n
alphabet
final_states
transition_table

c: number of cases
n: number of states (0 is always the initial state)
alphabet: space-separated symbols
final_states: space-separated list of final state numbers

Output format

For each case, the program prints all equivalent pairs of states in lexicographical order, in one line separated by spaces.

Example:

(1, 2) (3, 4)

How to Use:

Option 1

- Save the file as 'minimization.py'

- Navigate to the directory using 'cd name_of_directory'

- Prepare a file 'input.txt' with the DFA cases and run:

- python minimization.py < input.txt > output.txt

- This will save the output to 'output.txt'.

Option 2

- You can also type the input manually:

- python minimization.py

- Then enter the DFA description following the required format.

- This will display the output on the screen


Algorithm Explanation

The minimization algorithm follows the table-filling method described by Kozen:

1. Initialization:
   Create a table for all pairs of states '(p, q)' with 'p < q'.
   Mark a pair as 'distinguishable' if one is final and the other is not.

2. Refinement:
   Iteratively scan all unmarked pairs.
   For each pair '(p, q)' and each input symbol 'a':

   Let 'p' = δ(p, a)' and 'q' = δ(q, a)' be their next states.
   If '(p', q')' is already marked as distinguishable, mark '(p, q)' as distinguishable too.

   Repeat until no new pairs are marked in a full pass.

3. Equivalence Extraction:
   All unmarked pairs are equivalent states and can be merged.

4. Result:
   The program prints all equivalent pairs '(p, q)' in lexicographical order.