Here's an expanded version of the document with more mathematical examples and computations to further illustrate different trajectories:

---

# Problem 3

# Trajectories of a Freely Released Payload Near Earth

## Introduction

When a payload is released from a moving rocket near Earth, its trajectory depends on various factors such as its initial velocity, position, and the gravitational forces it experiences. Depending on these initial conditions, the payload can follow different types of trajectories such as elliptical, parabolic, or hyperbolic. These trajectories are critical for space missions, including satellite deployment, payload recovery, and even interplanetary travel.

Understanding the different trajectories that a payload can follow, based on its velocity and position relative to Earth, is essential for mission planning. This document discusses the underlying physics of gravitational forces, derives the equations of motion, explains the types of possible trajectories, and provides a simulation of a payload's trajectory near Earth.

## Gravitational Force and Equations of Motion

The motion of a payload near Earth is governed by Newton’s law of gravitation. The gravitational force acting on an object of mass \(m\) at a distance \(r\) from the center of Earth is given by:

\[
F = \frac{G M m}{r^2}
\]

Where:

- \(F\) is the gravitational force (in newtons),
- \(G\) is the gravitational constant, \(6.67430 \times 10^{-11} \) m³/kg⋅s²,
- \(M\) is the mass of Earth (\(5.972 \times 10^{24}\) kg),
- \(m\) is the mass of the payload,
- \(r\) is the distance from the center of Earth to the payload (in meters).

The force is responsible for the acceleration of the payload towards Earth. The acceleration \(a\) is given by:

\[
a = \frac{F}{m} = \frac{GM}{r^2}
\]

This is also referred to as **gravitational acceleration**. The second-order differential equations describing the motion of an object under Earth's gravity are:

\[
\frac{d^2 x}{dt^2} = -\frac{GM x}{(x^2 + y^2)^{3/2}}, \quad \frac{d^2 y}{dt^2} = -\frac{GM y}{(x^2 + y^2)^{3/2}}
\]

These equations form the foundation for calculating the trajectory of the payload.

### Additional Mathematical Computations

Let's now expand on the motion using a specific example to compute the initial velocities and energy in different scenarios:

1. **Escape Velocity Computation**

The escape velocity at a given distance \(r\) from the center of Earth is given by:

\[
v\_{\text{esc}} = \sqrt{\frac{2GM}{r}}
\]

At Earth's surface, \(r = R\_{\text{Earth}} = 6.371 \times 10^6 \, \text{m}\):

\[
v\_{\text{esc}} = \sqrt{\frac{2 \times 6.67430 \times 10^{-11} \times 5.972 \times 10^{24}}{6.371 \times 10^6}} \approx 11200 \, \text{m/s}
\]

2. **Energy Conservation in Gravitational Motion**

For a payload, the total mechanical energy is conserved in the absence of other forces. The total energy \(E\) is the sum of the kinetic and potential energies:

\[
E = \frac{1}{2} m v^2 - \frac{GMm}{r}
\]

Where:

- \(v\) is the velocity of the payload,
- \(r\) is the distance from the center of Earth.

For different initial velocities, we compute the total energy:

- For a payload at \(r = 2 \times R\_{\text{Earth}}\) with an initial velocity of \(v_0 = 9000 \, \text{m/s}\):

\[
E = \frac{1}{2} m (9000)^2 - \frac{GMm}{2R\_{\text{Earth}}}
\]

This can be expanded for different scenarios as part of a trajectory analysis.

## Types of Trajectories

The trajectory of a payload released near Earth depends on its initial velocity. Based on the velocity, the trajectory could be one of the following:

### 1. **Elliptical Trajectory**

When the initial velocity is less than the escape velocity, the payload follows an elliptical trajectory. The payload will eventually return to Earth after completing its elliptical orbit. This type of trajectory is typical for satellites in low Earth orbit (LEO).

The general equation for an elliptical orbit is derived from Kepler's Laws:

\[
r(t) = \frac{a(1 - e^2)}{1 + e \cos(\theta)}
\]

Where:

- \(a\) is the semi-major axis,
- \(e\) is the orbital eccentricity,
- \(\theta\) is the true anomaly (the angle between the payload and the periapsis).

### 2. **Parabolic Trajectory**

When the payload's initial velocity is equal to the **escape velocity** at a given distance from Earth, its trajectory will be parabolic. A parabolic trajectory is the boundary between bound and unbound motion, and it represents the exact condition for escaping Earth's gravity.

### 3. **Hyperbolic Trajectory**

If the payload's initial velocity exceeds the escape velocity, the trajectory will be hyperbolic. In this case, the payload escapes Earth's gravitational influence completely, traveling on a path that takes it far beyond Earth.

## Numerical Simulation of Trajectories

To simulate the trajectory of a payload under the influence of Earth’s gravity, we use numerical methods, particularly **Runge-Kutta** and **adaptive solvers** to solve the equations of motion.

Below is an extended version of the code with multiple scenarios and further mathematical computations. <a href="https://colab.research.google.com/drive/1Ednr7-CPkA0YtiMMcqQB_HHBQg6yCsmH#scrollTo=EL_sji7HhYQI" target="_blank">Learn more.</a>

![Payload Trajectory](payload_trajectory.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
G = 6.67430e-11  # m³/kg/s²
M_earth = 5.972e24  # kg
R_earth = 6.371e6  # m

def equations(t, state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -G * M_earth * x / r**3
    ay = -G * M_earth * y / r**3
    return [vx, vy, ax, ay]

def simulate_trajectory(y0, t_max, solver='RK45'):
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 2000)
    sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method=solver, rtol=1e-8)
    return sol

# Different scenarios for simulation
scenarios = {
    "LEO (Circular Orbit)": [R_earth + 300e3, 0, 0, 7800], # LEO example
    "Suborbital": [R_earth + 100e3, 0, 0, 5000], # Suborbital trajectory
    "Escape Trajectory": [R_earth + 300e3, 0, 0, 11200], # Escape velocity
    "Hyperbolic Escape": [R_earth + 300e3, 0, 0, 12000] # Hyperbolic trajectory
}

# Visualize the trajectories
plt.figure(figsize=(12, 12))
for label, initial_conditions in scenarios.items():
    sol = simulate_trajectory(initial_conditions, 5000)
    plt.plot(sol.y[0], sol.y[1], label=label)

plt.scatter(0, 0, color='red', label='Earth Center')
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid()
plt.title("Different Trajectories of a Released Payload")
plt.show()
```

### Additional Example: Calculation of Energy

To further illustrate the differences in energy at various positions, consider the following energy calculation for a payload with initial velocity \(v*0 = 9000 \, \text{m/s}\) at \(r = 2 \times R*{\text{Earth}}\):

- Compute the total mechanical energy:

\[
E = \frac{1}{2} m v_0^2 - \frac{GMm}{r}
\]

For \(v*0 = 9000 \, \text{m/s}\) and \(r = 2R*{\text{Earth}}\):

\[
E = \frac{1}{2} m (9000)^2 - \frac{G M m}{2R\_{\text{Earth}}}
\]

### Conclusion

This study explored payload trajectories mathematically and computationally, deriving governing equations, implementing numerical solutions with improved accuracy, and providing multiple examples. These additional mathematical calculations, including energy considerations and velocity computations, provide further insight into how different initial conditions affect the trajectory.
