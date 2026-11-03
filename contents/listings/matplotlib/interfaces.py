import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x ** 2

# --- Stateful (pyplot) Interface ---
plt.figure(figsize=(5, 3))
plt.plot(x, y)          # Draws on the "current" figure
plt.ylabel('Y axis')
plt.show()              # Displays the figure

# --- Stateless (Object-Oriented) Interface ---
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)           # Draws explicitly on 'ax'
ax.set_ylabel('Y axis')
plt.show()