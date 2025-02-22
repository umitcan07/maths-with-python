import matplotlib.pyplot as plt

# Create a list of abscissas (x-values) from 0 to 10 in steps of 0.1
abscissas = [n * 0.1 for n in range(0, 101)]

# Compute the ordinates (y-values) as the square of each x-value
ordinates = [x**2 for x in abscissas]

# Plot the curve y = x^2 by drawing a line through the points
plt.plot(abscissas, ordinates, label='y = x^2')

# Draw scatter points with specified colors and sizes
plt.scatter(1, 2, color='red', s=30, label='Point (1,2)')
plt.scatter(2, 3, color='blue', s=70, label='Point (2,3)')

# Display grid lines on the plot
plt.grid(True)

# Set the axis scales to be equal so that one unit in x is the same length as one unit in y
plt.axis('equal')

# Optionally, you can set bounds for the x-axis and y-axis
plt.xlim(min(abscissas), max(abscissas))
plt.ylim(min(ordinates), max(ordinates))

# Draw horizontal and vertical reference lines (the x-axis and y-axis)
plt.axhline(y=0, color='r', linestyle='-')      # x-axis in red, solid line
plt.axvline(x=0, color='b', linestyle='dotted')   # y-axis in blue, dotted line

# Add a legend to explain the plot elements
plt.legend()

# Show the plot in a window
plt.show()

# Close the plot
plt.close()
