import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the barcode
data = np.random.randint(0, 2, 100)  # Generate random binary data (0 or 1)

# Plot the barcode
plt.figure(figsize=(15, 2))  # Set the figure size
plt.bar(range(len(data)), data, color='black')  # Create a bar plot with black bars
plt.axis('off')  # Turn off the axis
plt.title('Barcode')  # Add a title
plt.show()

""" 
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.randint(0, 2, size=100)

# Create barcode plot
plt.figure(figsize=(10, 2))
plt.eventplot(data, orientation='horizontal', colors='black')
plt.yticks([])
plt.show()
 """
