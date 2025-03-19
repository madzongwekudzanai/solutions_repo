# Problem 1

# **Projectile Motion Analysis and Simulation**

### **Investigating the Range as a Function of the Angle of Projection**

---

## **1. Theoretical Foundation**

Projectile motion is a fundamental topic in classical mechanics, describing the motion of an object launched into the air under the influence of gravity. It plays a crucial role in various real-world applications, such as ballistics, sports, and space exploration. Understanding projectile motion requires analyzing both horizontal and vertical components independently, assuming no external forces except gravity (neglecting air resistance initially). By exploring its equations, derivations, and computational approaches, we can gain deeper insights into the factors influencing projectile trajectory.

### **1.1 Equations of Motion**

The motion of a projectile launched with an initial velocity \( v_0 \) at an angle \( \theta \) is governed by the fundamental kinematic equations.

#### **1.1.1 Horizontal Motion**

Since there is no horizontal acceleration (neglecting air resistance), the horizontal displacement is given by:

\[ x = v_0 \cos(\theta) t \]

where:

- \( x \) = horizontal displacement
- \( v_0 \) = initial velocity
- \( \theta \) = launch angle
- \( t \) = time

#### **1.1.2 Vertical Motion**

The vertical motion is influenced by gravity \( g \), leading to the equation:

\[ y = v_0 \sin(\theta) t - \frac{1}{2} g t^2 \]

where:

- \( y \) = vertical displacement
- \( g \) = acceleration due to gravity (9.81 m/s²)

### **1.2 Derivation of Key Equations**

#### **1.2.1 Time of Flight**

The total time of flight occurs when the projectile returns to the ground (i.e., \( y = 0 \)). Setting the vertical displacement equation to zero:

\[ 0 = v_0 \sin(\theta) t - \frac{1}{2} g t^2 \]

Factoring out \( t \):

\[ t (v_0 \sin(\theta) - \frac{1}{2} g t) = 0 \]

Solving for \( t \):

\[ t_f = \frac{2 v_0 \sin(\theta)}{g} \]

#### **1.2.2 Range of the Projectile**

The range \( R \) is the horizontal distance traveled before the projectile lands:

\[ R = v_0 \cos(\theta) t_f \]

Substituting \( t_f \) from above:

\[ R = v_0 \cos(\theta) \times \frac{2 v_0 \sin(\theta)}{g} \]

Using the trigonometric identity \( 2 \sin(\theta) \cos(\theta) = \sin(2\theta) \), we get:

\[ R = \frac{v_0^2 \sin(2\theta)}{g} \]

#### **1.2.3 Maximum Height**

At the peak, the vertical velocity is zero \( (v_y = 0) \). Using the kinematic equation:

\[ v_y^2 = v_0^2 \sin^2(\theta) - 2 g H \]

Setting \( v_y = 0 \):

\[ 0 = v_0^2 \sin^2(\theta) - 2 g H \]

Solving for \( H \):

\[ H = \frac{v_0^2 \sin^2(\theta)}{2g} \]

### **1.3 Effects of Air Resistance**

Without air resistance, projectiles follow a **parabolic trajectory**. However, with air resistance, the motion becomes more complex due to a drag force \( F_d \), given by:

\[ F_d = \frac{1}{2} C_d \rho A v^2 \]

where:

- \( C_d \) = drag coefficient (depends on object shape)
- \( \rho \) = air density (kg/m³)
- \( A \) = cross-sectional area (m²)
- \( v \) = velocity (m/s)

### **1.4 Numerical Computation with Air Resistance**

With air resistance, the equations of motion become nonlinear differential equations:

#### **1.4.1 Horizontal Motion with Drag**

\[ m \frac{dv_x}{dt} = -\frac{1}{2} C_d \rho A v v_x \]

#### **1.4.2 Vertical Motion with Drag**

\[ m \frac{dv_y}{dt} = -mg - \frac{1}{2} C_d \rho A v v_y \]

where \( v_x \) and \( v_y \) are the horizontal and vertical velocity components. These equations require numerical methods (such as Euler’s method or Runge-Kutta) for solving.

### **1.5 Summary of Important Equations**

| Quantity            | Equation                                         |
| ------------------- | ------------------------------------------------ |
| Horizontal Position | \( x = v_0 \cos(\theta) t \)                     |
| Vertical Position   | \( y = v_0 \sin(\theta) t - \frac{1}{2} g t^2 \) |
| Time of Flight      | \( t_f = \frac{2 v_0 \sin(\theta)}{g} \)         |
| Range               | \( R = \frac{v_0^2 \sin(2\theta)}{g} \)          |
| Maximum Height      | \( H = \frac{v_0^2 \sin^2(\theta)}{2g} \)        |
| Drag Force          | \( F_d = \frac{1}{2} C_d \rho A v^2 \)           |

---

## **2. Analytical Analysis of Range**

This section plots **range vs. launch angle** without air resistance. <a href="https://colab.research.google.com/drive/1sxZ0hmVo9KCmVdGBfbu7JuImuAKgUyYd#scrollTo=70QY0plaFcA-" target="_blank">Learn more.</a>

![range vs. launch angle](analytical_analysis_of_range.png)

---

## **3. Numerical Simulation with Air Resistance**

Here, we use **ODE solvers** to simulate projectile motion with drag. <a href="https://colab.research.google.com/drive/1mVflU6NC26PCAmQeVa732XKLAykqwTBU#scrollTo=Z3YGY0DjGQv-" target="_blank">Learn more.</a>

![ODE solvers](numerical_sumulation_with_air_resistance.png)

---

## **4. Interactive Simulation**

This section adds **sliders** for interactive tuning of launch parameters. <a href="https://colab.research.google.com/drive/1GlJbqtlKH8E3AgUMlgDzl-D4lrUWxCb5" target="_blank">Learn more.</a>

---

## **5. Launch from Different Heights**

We modify our simulation to allow for launch at y₀≠0. This affects the time of flight calculation. <a href="https://colab.research.google.com/drive/1puFf49HH7PUNkO4eD5cUrila92r7QgWX#scrollTo=ZBnL01S3HUhj" target="_blank">Learn more.</a>

![different heights](launch_from_different_height.png)
