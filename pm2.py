import matplotlib.pyplot as plt
import numpy as np

# Given value
v0 = 10  # m/s

# Heights to consider
h_values =  np.arange(0, 3.1, 0.1)

# Compute α using Newton's method for each height
alpha_values = [newton_method(v0, h) for h in h_values]

# Plot the angles α
plt.plot(h_values, alpha_values)
plt.xlabel("Height (h)")
plt.ylabel("Angle (α)")
plt.title("Angle α vs. Height h")
plt.grid(True)
plt.show()