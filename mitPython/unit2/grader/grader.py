"""
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area 
and square of the perimter of the regular polygon. The function returns the sum, rounded to 4 decimal places
"""
import math

# We first have to define the main function
def main():
# in the following line we are printing the result of the function polysum
    print(polysum(72,60))


# Here we are defining our functions that calculates the sum of area plus perimeter of a poligon
def polysum(n, s):
#The first section calculates the area of the polygon
    #We are using the math library to define the constant of pi
    pi = math.pi
    # We define 0.25 constant indicated in the formula for the area of the regular polygon
    CONST = 0.25
    # we multiply the number of sides by itself to get the sides squared
    s_squared = s * s
    # With the previous calculations we get the numerator of the formula       
    numerator = CONST * n * s_squared
    # We calculate the denominator
    denominator = math.tan(pi/n)
    # Area calculation
    area = numerator / denominator
    # Next we calculate the perimeter
    perimeter = (n * s) * (n * s)

    # Finally we add the area plus the perimeter to have the desired result
    result = area + perimeter
    
    #We return the result
    return round(result, 4)
# We make sure to run the main function
if __name__ == "__main__":
    main()