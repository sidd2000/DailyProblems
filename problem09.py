"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.

"""

def problem09(arr): 
    incl = 0
    excl = 0
    #incl and excl are variables to consider sum including or excluding current number
     
    for i in arr:    
        #Current max excluding i (No ternary in  Python)         
        new_excl = max(incl, excl) 
         
        #Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return max(incl, excl) 

def test_problem09a():
    input = [2, 4, 6, 8]
    output = 12
    assert problem09(input) == output
    
def test_problem09b():
    input = [5, 1, 1, 5]
    output = 10
    assert problem09(input) == output

