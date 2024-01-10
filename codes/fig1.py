import matplotlib.pyplot as plt
import numpy as np

def constant_function(value):
    def function(x):
        return value
    return np.vectorize(function)

# Create data for a constant function with value 100
constant_two = constant_function(100)
x = np.linspace(0,101,100)
y = constant_two(x)

# Plot
plt.plot(x, y, label='Constant Function (value = 100)')
plt.xlabel('n')
plt.ylabel('x(n)-y(n)')
plt.title('Difference of nth terms of X and Y')
plt.legend()

# Save the plot as a PNG
plt.savefig('fig1.png')

# Show the plot
plt.show()

