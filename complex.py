from cmath import *

def addition(a, b, c, d):
    # Returns the sum of (a + b*i) and (c + d*i)
    return complex(a + c, b + d)

def multiplication(a, b, c, d):
    # Returns the product of (a + b*i) and (c + d*i)
    # (a + b*i) * (c + d*i) = (a*c - b*d) + (a*d + b*c)*i
    return complex(a * c - b * d, a * d + b * c)

def find_parts_of_conjugate(z):
    # Returns a tuple (real part, imaginary part) of the conjugate of z
    conj = z.conjugate()
    return (conj.real, conj.imag)

def reciprocal(z):
    # Returns 1/z if z is nonzero; prints a warning and returns None if z == 0
    if z == 0:
        print("Warning: division by zero!")
        return None
    return 1/z

def abs_value(z):
    # Returns the absolute value of z
    return abs(z)

# Test the find_parts_of_conjugate function:
print(find_parts_of_conjugate((1 + 2j) * (2 - 3j) * (4 + 5j)))
print(complex(1, 2) * complex(2, 3))
