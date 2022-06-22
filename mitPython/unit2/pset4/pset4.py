

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    first_section = a*(x*x)
    second_section = b * x
    third_section = c
    resultado = first_section + second_section + third_section
    return resultado

print(evalQuadratic(2,3,4,5))
