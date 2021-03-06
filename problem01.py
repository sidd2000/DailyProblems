"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed 
using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is 
[1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwords from the end state.

"""

def problem01(stack):
  #initializing an empty queue at start of test case
  queue = []
  while len(stack) > 0:
    #Popping an element from the start of the stack, FIFO model
    queue.append(stack.pop(0))
    if len(stack) > 0:
      #Popping an element from the end of the stack, LIFO model
      queue.append(stack.pop())
  print(queue)
  return queue


def test_problem01a():
  input = [1, 2, 3, 4, 5]
  output = [1, 5, 2, 4, 3]
  assert problem01(input) == output


def test_problem01b():
  input = [1, 2, 3, 4]
  output = [1, 4, 2, 3]
  assert problem01(input) == output
  
"""Need to call the test functions to run the code"""