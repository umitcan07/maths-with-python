import matplotlib.pyplot as plt
import math
import numpy as np
from cmath import phase  # for obtaining the principal argument

# ----------------------------------------
# Exercise 3: Cartesian to Polar Conversions
# ----------------------------------------

def cartesian_to_polar(z):
    """
    Converts a complex number z in Cartesian form (a + bi)
    to polar coordinates (r, theta) using math.atan2.
    Here, r = |z| and theta is the principal argument in (-pi, pi].
    """
    r = abs(z)
    theta = math.atan2(z.imag, z.real)
    return (r, theta)

def cartesian_to_polar2(z):
    """
    Alternative implementation using cmath.phase.
    Returns a tuple (|z|, phase(z)).
    """
    return (abs(z), phase(z))

# A third version (already provided) using math.atan2:
def cartesian_to_polar3(z):
    r = abs(z)
    x = z.real
    y = z.imag
    theta = math.atan2(y, x)
    return (r, theta)

# ----------------------------------------
# Converting from Polar to Cartesian
# ----------------------------------------

def polar_to_cartesian(r, theta):
    """
    Given an absolute value r and an angle theta (in radians),
    returns the complex number r*(cos(theta) + i*sin(theta)).
    """
    return r * (math.cos(theta) + 1j * math.sin(theta))

# ----------------------------------------
# Tracing a Line Segment in the Complex Plane
# ----------------------------------------

def trace_segment(z0, z1, c='red'):
    """
    Traces (plots) the line segment between complex numbers z0 and z1.
    The segment is parameterized as:
       z(t) = (1-t)*z0 + t*z1,   for t in [0, 1].
    """
    # Create 100 values of t between 0 and 1.
    ts = np.linspace(0, 1, 100)
    # Compute the corresponding points along the segment.
    points = [(1 - t) * z0 + t * z1 for t in ts]
    xs = [pt.real for pt in points]
    ys = [pt.imag for pt in points]
    
    # Plot the segment.
    plt.plot(xs, ys, color=c, label='Segment')
    # Optionally, mark the endpoints.
    plt.scatter([z0.real, z1.real], [z0.imag, z1.imag], color='blue', zorder=5)
    
    # Draw the axes and grid.
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel('Real part')
    plt.ylabel('Imaginary part')
    plt.title('Line Segment in the Complex Plane')
    plt.legend()
    plt.show()

# ----------------------------------------
# Testing the Functions
# ----------------------------------------

if __name__ == '__main__':
    # Test cartesian_to_polar and cartesian_to_polar2 with an example complex number.
    z = 1 + 1j
    print("Cartesian to polar (using math.atan2):", cartesian_to_polar(z))
    print("Cartesian to polar (using cmath.phase):", cartesian_to_polar2(z))
    
    # Test polar_to_cartesian: Convert back using the polar coordinates.
    r, theta = cartesian_to_polar(z)
    z_back = polar_to_cartesian(r, theta)
    print("Polar to cartesian:", z_back)
    
    # Trace a line segment between two complex numbers.
    z0 = 1 + 1j
    z1 = 4 + 4j
    trace_segment(z0, z1)
