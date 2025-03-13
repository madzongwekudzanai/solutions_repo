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