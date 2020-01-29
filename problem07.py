"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can 
be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.

"""

def problem07(digits): 
    #Extract the digits string as a list
    digits = [int(x) for x in digits]
    n = len(digits)
          
    # A table to store results of subproblems 
    count = [0] * (n+1)  #Initializes (n+1) indices in the list as 0
    count[0] = 1
    count[1] = 1
    
    for i in range(2, n+1): 
      
        count[i] = 0
  
        # If the last digit is not 0, 
        # then last digit must add to 
        # the number of words 
        if (digits[i-1] > '0'): 
            count[i] = count[i-1] 
  
        # If second last digit is smaller 
        # than 2 and last digit is 
        # smaller than 7, then last two 
        # digits form a valid character 
        if (digits[i-2] == '1' or (digits[i-2] == '2' and digits[i-1] < '7') ): 
            count[i] += count[i-2]
      
    return count[n] 

def test_problem07a():
    input = "111"
    output = 3
    assert problem07(input) == output
    
def test_problem07b():
    input = "1234"
    output = 3
    assert problem07(input) == output
    
    