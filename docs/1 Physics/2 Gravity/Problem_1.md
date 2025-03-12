```python
import numpy as np
import matplotlib.pyplimot as plt

```


```python
# Gravitational Constant (m^3/kg/s^2)
G = 6.67430e-11

# Mass of the Sun (kg)
M_sun = 1.989e30

# Function for Kepler’s Third Law: T^2 = (4π^2 * r^3) / (G * M_sun)
def orbital_period(radius):
    return np.sqrt((4 * np.pi**2 * radius**3) / (G * M_sun))

# Example planets in the Solar System (Distance from the Sun in meters)
planets = {
    "Mercury": 5.79e10,
    "Venus": 1.082e11,
    "Earth": 1.496e11,
    "Mars": 2.279e11,
    "Jupiter": 7.785e11,
    "Saturn": 1.429e12,
    "Uranus": 2.871e12,
    "Neptune": 4.498e12
}

# Compute orbital periods (in years)
orbital_periods = {planet: orbital_period(r) / (60 * 60 * 24 * 365) for planet, r in planets.items()}

# Extracting values for plotting
radii = np.array(list(planets.values()))
periods = np.array(list(orbital_periods.values()))

# Plot Kepler’s Third Law: log(T^2) vs log(r^3)
plt.figure(figsize=(8,6))
plt.scatter(np.log10(radii**3), np.log10(periods**2), color="blue", label="Planets")
plt.xlabel("log(r^3) (log of radius cubed)")
plt.ylabel("log(T^2) (log of period squared)")
plt.title("Kepler's Third Law: Orbital Period vs Radius")
plt.legend()
plt.grid()
plt.show()
# Plot Orbital Radius vs Orbital Period
plt.figure(figsize=(8,6))
plt.scatter(radii, periods, color="green", label="Planets")
plt.xlabel("Orbital Radius (m)")
plt.ylabel("Orbital Period (years)")
plt.title("Orbital Period vs Orbital Radius")
plt.legend()
plt.grid()
plt.show()

# 2D Visualization of Circular Orbits
fig, ax = plt.subplots(figsize=(6,6))
for planet, radius in planets.items():
    circle = plt.Circle((0,0), radius, fill=False, label=planet)
    ax.add_patch(circle)

# Sun at the center
ax.scatter(0, 0, color="yellow", marker="o", s=100, label="Sun")

# Setting limits and labels
ax.set_xlim(-5e12, 5e12)
ax.set_ylim(-5e12, 5e12)
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")
ax.set_title("Circular Orbits of Planets in the Solar System")
ax.legend()
ax.set_aspect('equal')
plt.grid()
plt.show()


```


    
![png](Problem_1_files/Problem_1_1_0.png)
    



    
![png](Problem_1_files/Problem_1_1_1.png)
    



    
![png](Problem_1_files/Problem_1_1_2.png)
    



```python

```
