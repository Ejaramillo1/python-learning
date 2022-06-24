"""
Write an iterative function, gdcIter(a,b), that implements this idea. One easy way to do this is to
begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this
test value by 1 until you either reach a case where the test divides both a and b without remainder, or you 
reach 1.
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # Find the Maximum value and the Minimum value
    if a > b:
        minVal = b
        maxVal = a        
    else:
        minVal = a
        maxVal = b
    divisor = minVal
    
    # create a for loop that iterates in a range from 1 to maxValue + 1
    for i in range(1, maxVal + 1):
        while True:
            # the result of taking the modulo from both numbers has to be zero
            if maxVal % divisor != 0 or minVal % divisor != 0:
            # if the result of the modulo is not zero for both take 1 from the divisor
                divisor -= 1
            else:
                return divisor

print(gcdIter(6,12))