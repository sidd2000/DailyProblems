"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i. Solve it without using 
division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""

"""Solution 1, basic solution and takes O(n^2 time)"""
def problem02(numbers):
  numbers_product = []
  for i in range(0, len(numbers)):
    product = 1
    for j in range(0, len(numbers)):
      if not i is j:
        product *= numbers[j]
    numbers_product.append(product)
  return numbers_product

"""solution 2, slightly more complicated solution and takes O(n) time
The idea here is to create a multiple of all elements of the array,
Then replacing the values of the original array by dividing them with elements of original array"""

def problem02_solution2(numbers):
  product = 1
  for i in numbers:
    product *= i
  #Now we need index as well so need to use range
  for i in range(0,len(numbers)):
  #We use floor division instead of division. Floor division returns an integer value only
    numbers[i] = product // numbers[i]
  return numbers

def test_problem02a():
  input = [1, 2, 3, 4, 5]
  output = [120, 60, 40, 30, 24]
  assert problem02(input) == output
#We need to call the appropriate function as required

def test_problem02b():
  input = [3, 2, 1]
  output = [2, 3, 6]
  assert problem02(input) == output