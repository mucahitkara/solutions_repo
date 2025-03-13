# Orbital Period and Orbital Radius

## Introduction
The relationship between the square of the orbital period and the cube of the orbital radius, known as **Kepler's Third Law**, is a fundamental principle of celestial mechanics. This relationship allows us to understand planetary motions and gravitational interactions on both local and cosmic scales. 

Kepler’s Third Law states that for an object in a circular orbit around a massive central body:
\[
T^2 \propto R^3
\]
where:
- \(T\) is the orbital period (time taken to complete one orbit)
- \(R\) is the orbital radius (distance from the central body)

This law is crucial for calculating planetary masses, satellite trajectories, and space missions.

## Mathematical Derivation
Using Newton’s Law of Gravitation:
\[
F = \frac{G M m}{R^2}
\]
and equating it to the centripetal force required for circular motion:
\[
\frac{G M m}{R^2} = \frac{m v^2}{R}
\]
Solving for the velocity \(v\):
\[
v = \sqrt{\frac{G M}{R}}
\]
Since the orbital period \(T\) is related to the velocity by:
\[
T = \frac{2 \pi R}{v}
\]
Substituting for \(v\):
\[
T^2 = \frac{4 \pi^2 R^3}{G M}
\]
Thus, confirming Kepler’s Third Law:
\[
T^2 \propto R^3
\]

## Python Simulation
The following Python script simulates circular orbits and verifies Kepler’s Third Law numerically.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M_sun = 1.989e30  # Mass of the Sun (kg)

# Define planets with their average orbital radii (m) and periods (s)
planets = {
    "Mercury": (5.79e10, 7.60e6),
    "Venus": (1.08e11, 1.94e7),
    "Earth": (1.50e11, 3.15e7),
    "Mars": (2.28e11, 5.94e7),
    "Jupiter": (7.78e11, 3.74e8),
    "Saturn": (1.43e12, 9.29e8),
    "Uranus": (2.87e12, 2.65e9),
    "Neptune": (4.50e12, 5.20e9)
}

# Extract data for plotting
radii = np.array([data[0] for data in planets.values()])
periods = np.array([data[1] for data in planets.values()])

# Verify Kepler’s Third Law
kepler_ratio = periods**2 / radii**3

# Plot results
plt.figure(figsize=(8, 6))
plt.scatter(radii, periods**2, label="T^2 vs R^3 Data", color='blue')
plt.plot(radii, (4 * np.pi**2 / (G * M_sun)) * radii**3, linestyle='--', label="Kepler’s Law Fit", color='red')
plt.xlabel("Orbital Radius (m)")
plt.ylabel("Orbital Period Squared (s²)")
plt.title("Verification of Kepler’s Third Law")
plt.legend()
plt.grid()
plt.show()
```

## Results and Analysis
- The simulation confirms that the square of the orbital period is proportional to the cube of the orbital radius.
- The scatter plot and theoretical curve demonstrate Kepler’s Third Law in action.
- This relationship is fundamental for space missions, satellite deployment, and astrophysics.

Understanding Kepler’s laws helps scientists estimate planetary masses, satellite orbits, and even exoplanetary systems in distant galaxies.
