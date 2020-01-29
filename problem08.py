"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes have the same value.

Given the root to a Binary tree, count the number of unival subtrees.

"""

"""
Hint: Singly leaf node is always a possible unival tree
"""

# Node Structure  
class Node: 
    # Utility function to create a new node 
    def __init__(self ,data): 
        self.data = data 
        self.left = None 
        self.right = None
  
  
""" This function increments count by number of single  
    valued subtrees under root. It returns true if subtree  
     under root is Singly, else false. 
"""
def countSingleRec(root , count): 
    # Return False to indicate None 
    if root is None : 
        return True
  
    # Recursively count in left and right subtress also 
    left = countSingleRec(root.left , count) 
    right = countSingleRec(root.right , count) 
      
    # If any of the subtress is not singly, then this 
    # cannot be singly 
    if left == False or right  == False : 
        return False 
      
    # If left subtree is singly and non-empty , but data 
    # doesn't match 
    if root.left and root.data != root.left.data: 
        return False
  
    # same for right subtree 
    if root.right and root.data != root.right.data: 
        return False
  
    # If none of the above conditions is True, then  
    # tree rooted under root is single valued,increment 
    # count and return true 
    count[0] += 1
    return True 
  
  
# This function mainly calls countSingleRec() 
# after initializing count as 0 
def problem08(root): 
    # initialize result 
    count = [0] 
  
    # Recursive function to count 
    countSingleRec(root , count) 
  
    return count[0] 



def test_problem08a():
    """Let us construct the below tree  
            5 
          /   \ 
        4       5 
       /  \      \ 
      4    4      5 
    """
    root = Node(5) 
    root.left = Node(4) 
    root.right = Node(5) 
    root.left.left = Node(4) 
    root.left.right = Node(4) 
    root.right.right = Node(5) 
    output = 5
    assert problem08(root) == output

def test_problem08b():
    """Let us construct the below tree  
            5 
          /   \ 
         1      5 
       /  \      \ 
      5    5      5 
    """
    root = Node(5) 
    root.left = Node(1) 
    root.right = Node(5) 
    root.left.left = Node(5) 
    root.left.right = Node(5) 
    root.right.right = Node(5) 
    output = 4
    assert countSingle(root) == output