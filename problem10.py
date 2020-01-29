"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n 
milliseconds.

"""

import time

def problem10(f,n):
    time.sleep(0.001*n)
    f()
    



