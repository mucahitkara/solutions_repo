# Problem 1
import numpy as np
import matplotlib.pyplot as plt

# Gravitational Constant (m^3/kg/s^2)
G = 6.67430e-11  
# Mass of the Sun (kg)
M_sun = 1.989e30  

# Define function for Kepler's Third Law: T^2 = (4π^2 * r^3) / (G * M_sun)
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

# Plot Kepler's Third Law: log(T^2) vs log(r^3)
plt.figure(figsize=(8, 6))
plt.loglog(radii**3, periods**2, 'bo-', label="Planets")

plt.xlabel("Orbital Radius Cubed (r^3) [m^3]")
plt.ylabel("Orbital Period Squared (T^2) [years^2]")
plt.title("Kepler's Third Law Verification")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show the plot
plt.show()

# Print the calculated values for verification
for planet, period in orbital_periods.items():
    print(f"{planet}: Orbital Period = {period:.2f} years")
