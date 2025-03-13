import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s²)
v0 = 20   # initial velocity (m/s)

# Angle range (0° to 90°)
theta = np.linspace(0, 90, 100)
theta_rad = np.radians(theta)  # Convert to radians

# Compute range
R = (v0**2 * np.sin(2 * theta_rad)) / g

# Plot range vs. angle
plt.figure(figsize=(8, 5))
plt.plot(theta, R, label=f'Initial velocity = {v0} m/s')
plt.xlabel('Launch Angle (°)')
plt.ylabel('Range (m)')
plt.title('Projectile Range vs. Launch Angle')
plt.legend()
plt.grid()
plt.show()