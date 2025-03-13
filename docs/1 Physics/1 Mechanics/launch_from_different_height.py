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

def solve_projectile_height(v0, theta_deg, y0, Cd=0.47):
    """Solve projectile motion with different initial heights."""
    theta = np.radians(theta_deg)
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)

    # Initial conditions
    state0 = [0, y0, vx0, vy0]

    # Solve
    sol = solve_ivp(equations, (0, 10), state0, t_eval=np.linspace(0, 10, 500), args=(Cd, A, m, rho))
    
    return sol.t, sol.y[0], sol.y[1]

def plot_trajectory(v0, theta_deg, Cd, init_height):
    """Plots projectile motion with adjustable parameters."""
    t, x, y = solve_projectile_height(v0, theta_deg, init_height)

    plt.figure(figsize=(12, 7.5))
    plt.plot(x, y, label=f'v0={v0} m/s, θ={theta_deg}°, Cd={Cd}, y0={init_height}')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Motion with Air Resistance')
    plt.legend()
    plt.grid()
    plt.ylim(0)  # Ensure ground level is visible
    plt.show()

# Example: Launch from 13 meters
plot_trajectory(20, 45, 0.47, 13)