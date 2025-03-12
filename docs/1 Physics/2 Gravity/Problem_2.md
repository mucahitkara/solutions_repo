# Problem 2# Escape Velocities and Cosmic Velocities

## Introduction
Escape velocity is a crucial concept in understanding how objects can overcome the gravitational pull of celestial bodies. The first, second, and third cosmic velocities define the minimum speeds required to:
- Orbit a planet (first cosmic velocity)
- Escape a planet’s gravity (second cosmic velocity)
- Escape a star system (third cosmic velocity)

These velocities are essential for satellite launches, planetary exploration, and interstellar travel.

## Mathematical Derivation

1. **First Cosmic Velocity (Orbital Velocity)**:
   \[
   v_1 = \sqrt{\frac{G M}{R}}
   \]
   where:
   - \( G \) is the gravitational constant (6.67430 × 10⁻¹¹ m³/kg/s²)
   - \( M \) is the mass of the celestial body
   - \( R \) is the radius of the celestial body

2. **Second Cosmic Velocity (Escape Velocity)**:
   \[
   v_2 = \sqrt{2 \frac{G M}{R}}
   \]
   This is derived from energy conservation, requiring an object’s kinetic energy to counteract gravitational potential energy.

3. **Third Cosmic Velocity (Solar Escape Velocity)**:
   \[
   v_3 = \sqrt{2 \frac{G M_{sun}}{d} + v_2^2}
   \]
   This velocity allows an object to escape from the gravitational influence of a star (like the Sun) considering its initial velocity from a planetary surface.

## Python Simulation

The following Python script calculates and visualizes the cosmic velocities for Earth, Mars, and Jupiter:

```python
import numpy as np
import matplotlib.pyplot as plt

# Universal Gravitational Constant (m^3 kg^-1 s^-2)
G = 6.67430e-11 

# Dictionary of celestial bodies with mass (kg) and radius (m)
celestial_bodies = {
    "Earth": {"mass": 5.972e24, "radius": 6.371e6},
    "Mars": {"mass": 6.417e23, "radius": 3.3895e6},
    "Jupiter": {"mass": 1.898e27, "radius": 6.9911e7}
}

def escape_velocity(mass, radius):
    return np.sqrt(2 * G * mass / radius)

def orbital_velocity(mass, radius):
    return np.sqrt(G * mass / radius)

def solar_escape_velocity(mass, radius, sun_mass, sun_distance):
    return np.sqrt(2 * G * sun_mass / sun_distance + escape_velocity(mass, radius)**2)

# Compute velocities
velocities = {}
for planet, data in celestial_bodies.items():
    ve = escape_velocity(data["mass"], data["radius"])  # Second cosmic velocity
    v1 = orbital_velocity(data["mass"], data["radius"])  # First cosmic velocity
    v3 = solar_escape_velocity(data["mass"], data["radius"], 1.989e30, 1.5e11)  # Third cosmic velocity (approx.)
    velocities[planet] = {"v1": v1, "v2": ve, "v3": v3}

# Plot results
fig, ax = plt.subplots()
planets = list(velocities.keys())
v1_values = [velocities[p]["v1"] for p in planets]
v2_values = [velocities[p]["v2"] for p in planets]
v3_values = [velocities[p]["v3"] for p in planets]

ax.bar(planets, v1_values, label="First Cosmic Velocity")
ax.bar(planets, v2_values, bottom=v1_values, label="Second Cosmic Velocity")
ax.bar(planets, v3_values, bottom=np.array(v1_values) + np.array(v2_values), label="Third Cosmic Velocity")

ax.set_ylabel("Velocity (m/s)")
ax.set_title("Comparison of Cosmic Velocities")
ax.legend()
plt.show()
```

## Results and Analysis
- The first cosmic velocity is the smallest, allowing objects to remain in orbit.
- The second cosmic velocity is higher, enabling objects to leave planetary gravity.
- The third cosmic velocity is the highest, required to exit a star system.

These velocities play a vital role in space missions, from launching satellites to planning interstellar travel.
