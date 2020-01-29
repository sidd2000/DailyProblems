"""
This problem was asked by Apple.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
write a function that returns the number of unique ways you can climb the staircase. The order of 
the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a 
set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a 
time.

"""

# Recurssive program to find n'th fibonacci number 
def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2) 
  
# returns no. of ways to reach s'th stair 
def countWays(s): 
    return fib(s + 1) 


def test_problem12a():
    steps = 4
    assert countWays(steps) == 5

def test_problem12b():
    steps = 3
    assert countWays(steps) == 3
