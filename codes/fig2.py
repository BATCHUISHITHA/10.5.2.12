import matplotlib.pyplot as plt

# Generate the sequences
ap1 = [101 + 5 * i for i in range(10)]
ap2 = [1 + 5 * i for i in range(10)]

# Plot both sequences on a single graph
plt.plot(ap1, label='$x_1(n)$: 101, 106, ...')
plt.plot(ap2, label='$x_2(n)$: 1, 6, ...')

# Add stem plot
plt.stem(ap1, linefmt=':', markerfmt='o', basefmt=' ', label='Stem plot for $x_1(n)$')
plt.stem(ap2, linefmt=':', markerfmt='s', basefmt=' ', label='Stem plot for $x_2(n)$')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Values')
plt.title('Stem Plot for $x_1(n)$ and $x_2(n)$')
plt.legend(title='Sequences')

# Save the plot as a PNG
plt.savefig('fig2.png')

# Show the plot
plt.show()

