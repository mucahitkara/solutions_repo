import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 20  # initial velocity in m/s
g = 9.81  # gravitational acceleration in m/s^2

# Angles in degrees
angles = np.linspace(0, 90, 91)
angles_rad = np.radians(angles)

# Range formula: R = v^2 * sin(2*theta) / g
ranges = (v0**2 * np.sin(2 * angles_rad)) / g

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(angles, ranges)
plt.title("Projectile Range vs Launch Angle")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid(True)
plt.tight_layout()
plt.savefig("range_vs_angle.png")
plt.show()
