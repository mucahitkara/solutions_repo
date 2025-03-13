# Problem 3
# Trajectories of a Freely Released Payload Near Earth

## Introduction
When an object is released from a moving rocket near Earth, its trajectory depends on initial conditions and gravitational forces. This scenario presents a rich problem, blending principles of orbital mechanics and numerical methods. Understanding the potential trajectories is vital for space missions, such as deploying payloads or returning objects to Earth.

## Orbital Mechanics and Possible Trajectories
An object released near Earth can follow different types of trajectories based on its velocity and altitude:
- **Elliptical Orbit:** If the velocity is below escape velocity but high enough, the object remains in orbit.
- **Parabolic Trajectory:** If the velocity is exactly the escape velocity, the object follows a parabolic path and escapes Earth's gravity.
- **Hyperbolic Trajectory:** If the velocity exceeds escape velocity, the object follows a hyperbolic trajectory and moves away from Earth indefinitely.
- **Suborbital (Ballistic) Trajectory:** If the velocity is low, the object will re-enter Earth's atmosphere and eventually impact the surface.

## Mathematical Model
Newton’s Law of Gravitation governs the motion of the payload:
\[
F = \frac{G M m}{r^2}
\]
where:
- \( G \) is the gravitational constant (6.67430 × 10⁻¹¹ m³/kg/s²)
- \( M \) is the mass of Earth (5.972 × 10²⁴ kg)
- \( m \) is the mass of the payload
- \( r \) is the distance from the center of the Earth

Using Newton’s second law, we derive the equations of motion for numerical simulation.

## Python Simulation
The following Python script numerically simulates the trajectory of a payload released near Earth, considering different initial velocities.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M_earth = 5.972e24  # Mass of Earth (kg)
R_earth = 6.371e6  # Radius of Earth (m)

# Equations of Motion
def equations(t, y):
    x, vx, y, vy = y
    r = np.sqrt(x**2 + y**2)
    ax = -G * M_earth * x / r**3
    ay = -G * M_earth * y / r**3
    return [vx, ax, vy, ay]

# Initial Conditions
altitude = 400000  # 400 km above Earth's surface
initial_speed = 7500  # m/s (adjust to simulate different trajectories)
angle = np.radians(45)  # Launch angle
x0, y0 = R_earth + altitude, 0
vx0, vy0 = initial_speed * np.cos(angle), initial_speed * np.sin(angle)

# Time Span
t_span = (0, 10000)
t_eval = np.linspace(0, 10000, 1000)

# Solve Differential Equations
sol = solve_ivp(equations, t_span, [x0, vx0, y0, vy0], t_eval=t_eval, method='RK45')

# Extract Results
x_trajectory = sol.y[0]
y_trajectory = sol.y[2]

# Plot Trajectory
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x_trajectory, y_trajectory, label='Payload Trajectory')

# Draw Earth
earth = plt.Circle((0, 0), R_earth, color='blue', fill=True, alpha=0.3, label='Earth')
ax.add_patch(earth)

ax.set_xlim(-2*R_earth, 2*R_earth)
ax.set_ylim(-2*R_earth, 2*R_earth)
ax.set_xlabel("x position (m)")
ax.set_ylabel("y position (m)")
ax.set_title("Payload Trajectory near Earth")
ax.legend()
ax.set_aspect('equal')
plt.show()
```

## Results and Analysis
- If the initial velocity is below orbital speed, the payload follows a ballistic trajectory and falls back to Earth.
- If the initial velocity reaches orbital speed, the payload will follow an elliptical orbit.
- If the velocity is at escape speed, the payload follows a parabolic trajectory.
- If the velocity exceeds escape velocity, the payload follows a hyperbolic trajectory and leaves Earth's gravitational influence.

These findings are critical for space mission planning, satellite deployment, and planetary exploration.
