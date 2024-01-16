import matplotlib.pyplot as plt
import numpy as np

def constant_function(value):
    def function(x):
        return value
    return np.vectorize(function)

# Create data for a constant function with value 100
constant_two = constant_function(100)
x = np.arange(0, 11, 1)  # Adjust the range to include only whole numbers
y = constant_two(x)

# Plot
plt.plot(x, y, label='$x_1(n)$ (value = 100)')
plt.stem(x, y, linefmt=':', markerfmt='o', basefmt='', label='$x_2(n)$: Stem plot for constant function')
plt.xlabel('n')
plt.ylabel('$x(n) - y(n)$')
plt.title('Difference of $x(n)$ and $y(n)$')
plt.legend()

# Save the plot as a PNG
plt.savefig('fig1.png')

# Show the plot
plt.show()

