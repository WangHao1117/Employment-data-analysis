import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(10)
y = np.sqrt(x)
yerr = 0.1 + 0.2*np.sqrt(x)  # Simulated error bars (constant value for simplicity)

# Create error bar plot
plt.errorbar(x, y, yerr=yerr, fmt='o', color='b', ecolor='r', capsize=5, capthick=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Error Bar Plot')
plt.show()
