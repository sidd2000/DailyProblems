"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant 
space. In other words, find the lowest positive integer that does not exist in the array. The array 
can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

def problem04(numbers):
    #In-place sorting of array
    #Use sorted(list) when in-place is not allowed
	numbers.sort()
	next_number = 1
    #Defining start value for checking and incrementing till search in array is successful
	for n in numbers:
        #Neglecting negative numbers and 0 from computation, so it starts from 1
		if n > 0:
            #As soon as the number in array gets bigger than next_number, loop breaks and returns the missing number
			if n > next_number:
				break
			else:
				next_number = n + 1
	return next_number


def test_problem04a():
	input = [3, 4, -1, 1]
	output = 2
	assert problem04(input) == output


def test_problem04b():
	input = [1, 2, 0]
	output = 3
	assert problem04(input) == output
	