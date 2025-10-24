Assignment 2 — Left Recursion Elimination  

Student Information
Name: Juan Fernando Hernández Arenas  
Class number: 5730  


Development Environment
- Operating System: Windows 11 Pro  
- Programming Language: Python 3.13.1  
- Tools Used:
  - Visual Studio Code
  - Windows CMD

How to Run the Program

1. Save the main script
Save the following Python file as `recursion_elimination.py` in your directory.

2. Prepare your input file
Create a plain text file 'input.txt' with one or more grammar cases following the input format:

<number of cases>
<number of nonterminals>
<nonterminal> -> <alternatives separated by spaces>
<nonterminal> -> <alternatives separated by spaces>

Example:

3
1
S -> Sa b
2
S -> Aa b
A -> Ac Sd m
2
S -> Sa Ab
A -> Ac Sc c

3. Run from the command line
In the terminal or CMD, navigate to the folder containing the file and run:

python recursion_elimination.py < input.txt

4. Output format
Each case will print an equivalent grammar without left recursion, following the same input format.  
A blank line separates each grammar.

Example Output:

S -> bZ
Z -> aZ e

S -> Aa b
A -> bdZ mZ
Z -> cZ adZ e

S -> AbZ
A -> cY
Z -> aZ e
Y -> cY bZcY e

Algorithm Explanation

The program implements the Left Recursion Elimination algorithm described in  
Aho, Alfred V. et al. (2006). Compilers: Principles, Techniques, and Tools (2nd Edition). Section 4.3.3.


1. Input Parsing
   - The program reads the number of cases.
   - For each case, it reads all nonterminals and their production rules.
   - Alternatives are separated by spaces.

2. Processing Nonterminals
   - Nonterminals are processed in order: 'A₁, A₂, ..., Aₙ'.
   - For each 'Aᵢ', all indirect recursions from previous nonterminals 'Aⱼ (j < i)' are replaced by their expansions.

3. Direct Recursion Elimination
   - If 'Aᵢ' has rules of the form 'Aᵢ -> Aᵢα | β', it is rewritten as:
     Aᵢ -> βAᵢ
     Aᵢ' -> αAᵢ | ε
     where Aᵢ' (here named Z, Y) is a new nonterminal.

4. Output
   - The resulting grammar is printed in the same format as the input.
   - The symbol 'e' represents the empty string (ε).

Example of Transformation

Original:

S -> Sa b


Process:
- Recursive rule: 'S -> S a | b'
- Identify α = a, β = b
- Replace with:
 
  S -> bZ
  Z -> aZ e

