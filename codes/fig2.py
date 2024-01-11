import matplotlib.pyplot as plt

# Generate the sequences
ap1 = [101 + 5 * i for i in range(10)]  
ap2 = [1 + 5 * i for i in range(10)]    

# Plot both sequences on a single graph
plt.plot(ap1, label='101, 106, ...')
plt.plot(ap2, label='1, 6, ...')

# Add labels and legend
plt.plot(x, y, label='x(n) & y(n)')
plt.xlabel('n')
plt.ylabel('x(n) & y(n)')
plt.title('x(n) & y(n)')
plt.legend()

# Save the plot as a PNG
plt.savefig('fig2.png')

# Show the plot
plt.show()
