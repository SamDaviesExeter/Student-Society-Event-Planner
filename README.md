# Student Society Event Planner

## Overview

The project implements an optimisation system for the student society event planner scenario. The goal is to select the subset of activities that will maximise the total enjoyment while staying within both the constraints of:
- A maximum budget
- A maximum time

Two algorithmic approaches are implemented here:
- A Brute-Force algorithm
- A Dynamic Programming algorithm (which employs bottom-up tabulation)

The project demonstrates the difference between the exponential and polynomial-time optimisation techniques

## How to Run the Program

Ensure that the plain text files are inside the folder named assets, in the same directory as the script and then execute the main script - from the project root directory:
```
python source/main.py
```
The program will:
- Automatically read all the input files inside the ```assets/``` folder
- Apply both algorithms
- Display selected activities
- Display total enjoyment, cost and time taken
- Ask if you want to skip the brute-force approach if the input size exceeds 22 activities (to avoid an excessive runtime)
- input 1000 will cause dynamic prossessing to take atleast 2 minuets, the program has not crashed 
- input 100, 200, 1000 are not recommended to run with brute force input_large.txt takes about 3 minuets 

## Input File Format

Each input file inside ```assets/``` contains:
- A list of activities (name, enjoyment, cost, time)
- A maximum budget constraint
- A maximum time constraint

Example activity line format:
```
activity_name enjoyment cost time
```

## Project Structure

```
assets/
    input_10.txt
    input_100.txt
    input_1000.txt
    input_200.txt
    input_small.txt
    input_medium.txt
    input_large.txt
    constraint_budget.txt
    constraint_time.txt
    constraint_gracefull.txt

source/
    main.py
    brute_force.py
    dynamic.py
    utility.py
    tests.py
    data_strucs/
        stack_struc.py
        queue_struc.py
```

## File Descriptions

- ```main.py``` - Entry point of the program. It will load the input files and execute both algorithms
- ```brute_force.py``` - Implements the subset generation using bit manipulation to explore all possible combinations
- ```dynamic.py``` - Implements a 3D dynamic programming solution: ```dp[i][t][b]``` representing a maximum enjoyment using first ```i``` activities within time ```t``` and budget ```b```
- ```utility.py``` - Contains file-reading and helper functions
- ```stack_struc.py``` / ```queue_struc.py``` - Custom data structure implementations used for solution reconstruction and ordering
- ```tests.py``` - Used for basic validation and debugging during development

## Algorithm Summary

Brute-Force
- Generates all possible subsets (2^n combinations)
- Uses bit manipulation
- Checks each subset against budget and time constraints
- Guarantees an optimal solution
- Exponential time complexity: O(2^n)

Brute-force approach takes more computation time for larger input sizes

Dynamic Programming
- Uses bottom-up tabulation
- 3D DP table: ```dp[i][t][b]```
- Avoids recalculating overlapping subproblems
- Time complexity: O(n x T x B)
- Space complexity: O(n x T x B)

Produces the same optimal result but significantly faster for larger input sizes

Greedy Heuristic
- Sorts activities with a scoring system
- Selects activities in descending order
- Does not explore all combinations
- Does not guarantee optimal solution
- Time complexity: O(nlogn)
- Space complexity: O(n)

Runs significantly faster than both but may produce a suboptimal solution

## Dependencies 

This project:
- Requires Python 3.x to run
- Uses only standard Python libraries

No additional external libraries or packages are required

## Purpose

This project demonstrates:
- Combinatorial optimisation
- Bit manipulation
- Multi-constraint knapsack problems
- Time and Space complexity comparison
- Trade-offs between algorithmic approaches
