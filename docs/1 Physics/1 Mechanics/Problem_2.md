# Problem 2

# Investigating the Dynamics of a Forced Damped Pendulum

## Motivation

The forced damped pendulum is a fascinating example of a system where damping, restoring forces, and external periodic forcing interplay to create rich dynamic behavior. This system exhibits a variety of phenomena, including resonance, chaos, and quasiperiodicity, making it a valuable subject for studying complex real-world systems such as driven oscillators, climate models, and mechanical structures under periodic stress.

By adjusting parameters like damping, external force amplitude, and driving frequency, the system transitions through different behaviors, such as synchronized oscillations, chaotic motion, and resonance phenomena. Understanding these behaviors has significant implications for fields like energy harvesting, vibration isolation, and mechanical resonance.

## Theoretical Foundation

The motion of a forced damped pendulum is governed by the differential equation:

\[\frac{d^2\theta}{dt^2} + b \frac{d\theta}{dt} + \frac{g}{L} \sin(\theta) = A \cos(\omega t)\]

where:

- \( \theta(t) \) is the angular displacement,
- \( b \) is the damping coefficient,
- \( g \) is the gravitational acceleration,
- \( L \) is the length of the pendulum,
- \( A \) is the amplitude of the external force,
- \( \omega \) is the driving frequency.

### Small-Angle Approximation

For small angles, we approximate \( \sin\theta \approx \theta \), reducing the equation to:

\[\frac{d^2\theta}{dt^2} + b \frac{d\theta}{dt} + \frac{g}{L} \theta = A \cos(\omega t)\]

This equation describes a forced damped harmonic oscillator with the general solution:

\[\theta(t) = \theta_0 e^{-bt/2} \cos(\omega t - \delta)\]

where \( \theta_0 \) and \( \delta \) depend on the system parameters.

### Resonance Conditions

Resonance occurs when the driving frequency \( \omega \) matches the natural frequency:

\[ \omega_0 = \sqrt{\frac{g}{L}} \]

At resonance, the amplitude grows significantly unless limited by damping.

## Analysis of Dynamics

### Effects of Parameters

- **Damping coefficient (\( b \))**: Higher damping reduces oscillation amplitude and affects stability.
- **Driving amplitude (\( A \))**: Higher values increase oscillation response and can induce chaotic behavior.
- **Driving frequency (\( \omega \))**: Near resonance, large oscillations appear, leading to energy amplification.

### Transition to Chaos

Beyond simple oscillations, varying \( b \), \( A \), and \( \omega \) leads to quasiperiodic or chaotic motion. The transition to chaos can be observed using bifurcation diagrams and Poincaré sections. These chaotic behaviors arise from the system’s sensitivity to initial conditions, a hallmark of deterministic chaos.

## Practical Applications

- **Energy Harvesting**: Used in piezoelectric devices to convert oscillatory motion into electrical energy.
- **Suspension Bridges**: Models forced oscillations under periodic forces, such as wind or traffic-induced vibrations.
- **Oscillating Circuits**: Analogous to driven RLC circuits, where voltage replaces angular displacement and current replaces velocity.
- **Biological Rhythms**: Similar dynamics appear in human gait patterns and circadian rhythms under external influences.
- **Seismic Engineering**: Structures subjected to periodic seismic forcing can be analyzed using pendulum models.
- **Planetary Motion**: Certain planetary rotational dynamics exhibit nonlinear oscillatory behavior similar to forced pendulums.

## Graphical Representations

- **Time Series**: Plots of \( \theta(t) \) to observe periodicity or chaos. <a href="https://colab.research.google.com/drive/1bj51sHI9Xlik4Y6hWdOUKXCk4eS9XUBJ#scrollTo=4wrl1_4bTDLt" target="_blank">Learn more.</a>

![Time Series](time_series.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def forced_damped_pendulum(t, y, b, g, L, A, omega_d):
    """ODE system for a forced damped pendulum."""
    theta, omega = y  # omega represents angular velocity (dtheta/dt)
    dtheta_dt = omega
    domega_dt = -b * omega - (g/L) * np.sin(theta) + A * np.cos(omega_d * t)  # Corrected force term

    return [dtheta_dt, domega_dt]
# Parameters
g = 9.81  # Gravity (m/s^2)
L = 1.0   # Length of pendulum (m)
y0 = [np.pi / 4, 0]  # Initial angle = 45 degrees, initial velocity = 0

# Different parameter sets to compare
cases = [
    {"b": 0.2, "A": 1.0, "omega_d": 1.5, "label": "b=0.2, A=1.0, ω=1.5"},
    {"b": 0.5, "A": 1.2, "omega_d": 2.0, "label": "b=0.5, A=1.2, ω=2.0"},
    {"b": 0.8, "A": 1.5, "omega_d": 2.5, "label": "b=0.8, A=1.5, ω=2.5"},
]

# Time range
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

plt.figure(figsize=(12, 7.5))

# Solve and plot for different cases
for case in cases:
    sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval,
                     args=(case["b"], g, L, case["A"], case["omega_d"]))
    plt.plot(sol.t, sol.y[0], label=case["label"])

# Formatting the plot
plt.xlabel('Time (s)')
plt.ylabel('Angle (radians)')
plt.title('Forced Damped Pendulum Motion (Multiple Instances)')
plt.legend()
plt.grid(True)
plt.show()
```

- **Phase Portraits**: \( \theta \) vs. \( \frac{d\theta}{dt} \) to analyze system stability and attractors.

![Phase Portraits](phase_portrait.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def forced_damped_pendulum(t, y, b, g, L, A, omega):
    """ODE system for a forced damped pendulum."""
    theta, omega_dot = y
    dtheta_dt = omega_dot
    domega_dt = -b * omega_dot - (g/L) * np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Parameters
g = 9.81  # Gravity (m/s²)
L = 1.0   # Length of pendulum (m)
y0 = [np.pi / 4, 0]  # Initial angle = 45 degrees, initial velocity = 0

# Different parameter sets to compare
cases = [
    {"b": 0.2, "A": 1.0, "omega": 1.5, "color": "r", "label": "b=0.2, A=1.0, ω=1.5"},
    {"b": 0.5, "A": 1.2, "omega": 2.0, "color": "b", "label": "b=0.5, A=1.2, ω=2.0"},
    {"b": 0.8, "A": 1.5, "omega": 2.5, "color": "g", "label": "b=0.8, A=1.5, ω=2.5"},
]

# Time range
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

plt.figure(figsize=(12, 7.5))

# Solve and plot for different cases
for case in cases:
    sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval,
                     args=(case["b"], g, L, case["A"], case["omega"]))

    plt.plot(sol.y[0], sol.y[1], color=case["color"], label=case["label"])

# Formatting
plt.xlabel('Theta (angle)')
plt.ylabel('Angular Velocity')
plt.title('Phase Portrait of Forced Damped Pendulum')
plt.legend()
plt.grid(True)

plt.show()
```

- **Poincaré Sections**: Used to detect chaotic behavior by sampling system states at discrete time intervals.
  ![Poincaré Sections](poincare_section.png)
- **Bifurcation Diagrams**: Show transitions to complex motion as system parameters are varied, revealing period-doubling cascades leading to chaos.
  ![Bifurcation Diagrams](bifurcation_diagram.png)
- **Lyapunov Exponents**: Used to quantify chaos by measuring the rate of separation of nearby trajectories.
  ![Lyapunov Exponents](lyapunov_exponent.png)

## Conclusion

This study of the forced damped pendulum provides insight into nonlinear dynamics, resonance, and chaos, with applications in physics and engineering. By using numerical simulations, we can explore a range of behaviors from simple periodic motion to chaotic dynamics, offering deeper understanding and practical implications in various scientific domains. The forced damped pendulum serves as a fundamental model for diverse physical systems, reinforcing the significance of nonlinear dynamics in both theoretical and applied research.

```

```
