import matplotlib.pyplot as plt
from math import sqrt

# Helper: Plot a single complex number as a point.
def plot_complex_point(z, label=None, color='blue', marker='o'):
    plt.scatter(z.real, z.imag, color=color, marker=marker)
    if label is not None:
        # Annotate the point with its label slightly offset.
        plt.text(z.real, z.imag, ' ' + label, fontsize=9)

# (c) Define a function that takes three complex numbers and draws the triangle.
def draw_triangle(z1, z2, z3):
    # Get the real and imaginary parts for each vertex.
    xs = [z1.real, z2.real, z3.real, z1.real]  # Close the triangle
    ys = [z1.imag, z2.imag, z3.imag, z1.imag]
    
    # Create a new figure.
    plt.figure()
    
    # Plot the triangle (edges).
    plt.plot(xs, ys, 'b-', label="Triangle")
    
    # Plot the vertices.
    plot_complex_point(z1, label='z1', color='red')
    plot_complex_point(z2, label='z2', color='red')
    plot_complex_point(z3, label='z3', color='red')
    
    # Set up the plot details.
    plt.xlabel('Real part')
    plt.ylabel('Imaginary part')
    plt.title('Triangle in the Complex Plane')
    plt.grid(True)
    
    # Draw x and y axes.
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.legend()
    plt.show()

# --------------------------------------------------
# Optional extra: (b) Visualising various transformations of a complex number.
def plot_complex_transformations(z):
    # Compute the various transformations.
    transforms = {
        'z': z,
        '2z': 2 * z,
        '1/z': 1/z if z != 0 else None,
        'i*z': 1j * z,
        'conjugate(z)': z.conjugate(),
        'z^2/|z|': (z**2 / abs(z)) if z != 0 else None
    }
    
    plt.figure()
    for label, point in transforms.items():
        if point is not None:
            plot_complex_point(point, label=label, color='green')
            # Optionally, annotate the point.
            plt.text(point.real, point.imag, ' ' + label, fontsize=9)
    
    plt.xlabel('Real part')
    plt.ylabel('Imaginary part')
    plt.title('Complex Number Transformations')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

# --------------------------------------------------
# Demonstration of the triangle drawing function:
if __name__ == '__main__':
    # Example (c):
    draw_triangle(1 + 1j, 1.5 + 3j, 2 - 1j)
    
    # Example (d):
    # Let w = (-1 + sqrt(3)*i)/2 and z = 1+3j.
    w = (-1 + sqrt(3) * 1j) / 2
    z = 1 + 3j
    
    # Uncomment one of the following examples to test:
    # draw_triangle(z, 2*z, (1 + 2j)*z)
    # draw_triangle(z, z*w, z*w**2)
    
    # Optional: To see the various transformations of a complex number z, uncomment:
    # plot_complex_transformations(z)
