# Problem 1

# **Projectile Motion Analysis and Simulation**

### **Investigating the Range as a Function of the Angle of Projection**

---

## **1. Theoretical Foundation**

Projectile motion follows Newton’s laws of motion. We analyze the motion by separating it into horizontal and vertical components.

### **1.1 Equations of Motion**

The motion of a projectile launched with initial velocity \( v_0 \) at an angle \( \theta \) is governed by:

- **Horizontal motion (constant velocity)**  
  \[
  x = v_0 \cos(\theta) t
  \]
- **Vertical motion (accelerated due to gravity)**  
  \[
  y = v_0 \sin(\theta) t - \frac{1}{2} g t^2
  \]
- **Time of flight (when \( y = 0 \))**  
  \[
  t_f = \frac{2 v_0 \sin(\theta)}{g}
  \]
- **Range of projectile**  
  \[
  R = \frac{v_0^2 \sin(2\theta)}{g}
  \]
- **Maximum height**  
  \[
  H = \frac{v_0^2 \sin^2(\theta)}{2g}
  \]

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

---

## **3. Numerical Simulation with Air Resistance**

Here, we use **ODE solvers** to simulate projectile motion with drag.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravity (m/s²)
rho = 1.225  # Air density (kg/m³)
Cd = 0.47  # Drag coefficient (sphere)
A = 0.01  # Cross-sectional area (m²)
m = 0.145  # Mass of projectile (kg) (e.g., baseball)

def equations(t, state, Cd, A, m, rho):
    """Differential equations for projectile motion with air resistance."""
    x, y, vx, vy = state
    v = np.sqrt(vx**2 + vy**2)  # Speed
    drag = (0.5 * Cd * rho * A * v**2) / m  # Drag acceleration

    ax = -drag * (vx / v)  # Drag in x-direction
    ay = -g - drag * (vy / v)  # Drag in y-direction

    return [vx, vy, ax, ay]

def solve_projectile(v0, theta_deg, Cd=0.47):
    """Solve projectile motion with air resistance using numerical integration."""
    theta = np.radians(theta_deg)
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)

    # Initial conditions
    state0 = [0, 0, vx0, vy0]

    # Solve using solve_ivp
    t_span = (0, 5)  # Time range
    t_eval = np.linspace(0, 5, 300)  # Time points for solution
    sol = solve_ivp(equations, t_span, state0, t_eval=t_eval, args=(Cd, A, m, rho))

    return sol.t, sol.y[0], sol.y[1]  # Time, x, y

def plot_trajectory(v0, theta_deg, Cd):
    """Plots projectile motion with adjustable parameters."""
    t, x, y = solve_projectile(v0, theta_deg, Cd)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f'v0={v0} m/s, θ={theta_deg}°, Cd={Cd}')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Motion with Air Resistance')
    plt.legend()
    plt.grid()
    plt.ylim(0)  # Ensure ground level is visible
    plt.show()

# Example Plot
plot_trajectory(20, 45, 0.47)
```
