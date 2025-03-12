import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, theta, g=9.81, time_resolution=0.01):
    """Simulates projectile motion given initial velocity and angle."""
    theta_rad = np.radians(theta)
    
    # Time of flight
    T = (2 * v0 * np.sin(theta_rad)) / g
    
    # Time array
    t = np.arange(0, T, time_resolution)
    
    # Equations of motion
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    
    return x, y, T

def plot_projectile_motion(v0, theta_values, g=9.81):
    """Plots projectile trajectories for different launch angles."""
    plt.figure(figsize=(10, 5))
    
    for theta in theta_values:
        x, y, _ = projectile_motion(v0, theta, g)
        plt.plot(x, y, label=f"{theta}°")
    
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.title("Projectile Motion for Different Angles")
    plt.legend()
    plt.grid()
    plt.show()

def plot_range_vs_angle(v0, g=9.81):
    """Plots the range as a function of launch angle."""
    angles = np.linspace(0, 90, 100)
    ranges = (v0**2 * np.sin(2 * np.radians(angles))) / g
    
    plt.figure(figsize=(8, 5))
    plt.plot(angles, ranges, 'r-', label="Range")
    plt.xlabel("Launch Angle (degrees)")
    plt.ylabel("Range (m)")
    plt.title("Range vs. Launch Angle")
    plt.legend()
    plt.grid()
    plt.show()

# Example Usage
initial_velocity = 20  # m/s
theta_values = [15, 30, 45, 60, 75]  # Different angles
plot_projectile_motion(initial_velocity, theta_values)
plot_range_vs_angle(initial_velocity)
plt.show()
