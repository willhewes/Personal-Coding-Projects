import matplotlib.pyplot as plt
import numpy as np

# Some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the first subplot (left)
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(x, y1, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('First Subplot')
plt.legend()

# Create the second subplot (right)
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.plot(x, y2, label='cos(x)', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Second Subplot')
plt.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()