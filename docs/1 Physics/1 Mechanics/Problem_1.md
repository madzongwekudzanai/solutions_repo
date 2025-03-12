# Problem 1

# **Projectile Motion Analysis and Simulation**

### **Investigating the Range as a Function of the Angle of Projection**

---

## **1. Theoretical Foundation**

Projectile motion follows Newton’s laws of motion. We analyze the motion by separating it into horizontal and vertical components.

### **1.1 Equations of Motion**

The motion of a projectile launched with initial velocity \( v_0 \) at an angle \( \theta \) is governed by:

- **Horizontal motion (constant velocity)**  
  &nbsp;x=v₀cos(θ)t
- **Vertical motion (accelerated due to gravity)**  
  &nbsp;y=v₀sin(θ)t−1/2gt²
- **Time of flight (when \( y = 0 \))**  
  &nbsp;tբ=(2v₀sin(θ))/g
- **Range of projectile**  
  &nbsp;R=(v₀²sin(2θ))/g
- **Maximum height**  
  &nbsp;H=(v₀²sin²(θ))/2g

### **1.2 Effects of Air Resistance**

Without air resistance, projectiles follow a **parabolic trajectory**. However, with air resistance, the motion is more complex because drag opposes velocity. The drag force is given by:

\[
F_d = \frac{1}{2} C_d \rho A v^2
\]

where:

- \( C_d \) = drag coefficient (depends on object shape)
- \( \rho \) = air density (kg/m³)
- \( A \) = cross-sectional area (m²)
- \( v \) = velocity (m/s)

The equations of motion then become **nonlinear differential equations**, which we solve numerically.

---

## **2. Analytical Analysis of Range**

This section plots **range vs. launch angle** without air resistance.

```python
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
```
