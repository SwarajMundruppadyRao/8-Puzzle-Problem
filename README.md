# 8-Puzzle-Problem
Solving the 8 puzzle problem using Node exploration strategy (BFS Algorithm)

## Description

The repository contains two pyton files to solve and animate the 8 puzzle problem. The project is a part of ENPM661 - Planning for Autonomous Robots Project 1 

## Libraries Used in the Code
- queue.PriorityQueue
- numpy
- sortedcollections.OrderedSet
- matplotlib.pyplot
- matplotlib.patches.Polygon
- time
- pygame
- vidmaker
- math

## Running the Code
- Open the 8_puzzle_problem.py file and enter the desired combination to be achieved
*  Run the 8_puzzle_problem.py file using the following command
  ```bash
 python 3 8_puzzle_problem.py
```
* Enter the Puzzle configuration into the terminal row wise ( Enter the first element of row 1, press Enter. Next enter the second element of the first row.....And so on...)
*  Wait for the file to run. Once the process has ended the following will be printed in your terminal " Run Animate.py file using: python3 Animate.py command in the terminal to watch how the puzzle was solved".
*  Run this command in the terminal to visualize how the puzzle was solved using BFS algorithm.
 ```bash
python3 Animate.py
   ```

## Note 
1. For the entered configuration the code will convey whether the puzzle combination entered is solvable or not. If the puzzle is not solvable then a prompt will be displayed in the terminal. Run the program again, follow steps 3 - 6.
2. The code for solvability checker has been borrowed from GeeksForGeeks Website (https://www.geeksforgeeks.org/check-instance-8-puzzlesolvable/).
