import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.randn(1000)

# Create histogram
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(axis='y', alpha=0.75)
plt.show()
