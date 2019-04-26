# Title

N queens problem using constraint satisfication Problem (CSP) forwarding and backtracking approch in Python

### Prerequisites

Python 3.0+

## Running the tests

Any python ide or anaconda tools like (VScode, pycharm, spyder, jupyter notebook and any such tool which can support python 3.0+)

### Run

On ide just click run.
On command line get address to your file(where you saved the code).
and type command " Python Nqueens.py"

### Problem Statement

N-Queens problem: There is a n x n grid where the value of n is 8. Your task is to place 8 queens on this board. As per the rules of chess, a queen should have no other queen in its respective column, neither it should have any other queen in its row nor it should have any within its diagonal cells. You can consider this case as placing each queen individually per column such that it does not violate any of the constraints mentioned. It’s quite easy to find solution manually but your task is now to code it and find the correct positions for the queens. 
This problem has to be solved through the concept of CSP. So initially you will place the first queen randomly at any location within column 1. With respect to its location, now next 7 queens’ domain might shrink up. This is where the concept of consistency will get applied. Further up, when we will move forward, there might be a point where domain gets empty for any particular queen, at that instance apply backtrack concept, which means that location of previous queen will have to get changed.


## Note

Placement of first queen is randomly generated as defined in problem statment.

## Authors

* **Sooraj Kumar** 
