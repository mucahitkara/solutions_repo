# Problem 1 - Measuring Earth's Gravitational Acceleration with a Pendulum

## 🎯 Motivation

The acceleration \( g \) due to gravity is a fundamental constant that influences a wide range of physical phenomena. One classic method for determining \( g \) is through the oscillations of a simple pendulum, where the period of oscillation depends on the local gravitational field. This experiment emphasizes rigorous measurement practices, uncertainty analysis, and their role in experimental physics.

---

## 🧪 Procedure

### 1. Materials
- A string (~1–1.5 meters)
- A small weight (e.g., washer, keychain)
- Stopwatch (or phone timer)
- Ruler or measuring tape

### 2. Setup
- Attach the weight and suspend the string.
- Measure pendulum length \( L \) from suspension point to center of mass.
- Estimate uncertainty in \( L \) as:  
  \[
  \Delta L = \frac{\text{Ruler Resolution}}{2}
  \]

### 3. Data Collection
- Pull pendulum to <15° and release.
- Measure \( T_{10} \) for 10 full oscillations, 10 times.
- Compute:
  - Mean time: \( \overline{T_{10}} \)
  - Standard deviation: \( \sigma_T \)
  - Uncertainty:
    \[
    \Delta T_{10} = \frac{\sigma_T}{\sqrt{n}}, \quad n = 10
    \]

---

## 🧮 Calculations

```python
import numpy as np

# Length and uncertainty
L = 1.20  # meters
delta_L = 0.005  # meters

# 10 measurements of 10 oscillations (seconds)
T10_values = np.array([22.5, 22.3, 22.4, 22.6, 22.4, 22.3, 22.5, 22.4, 22.3, 22.6])
T10_mean = np.mean(T10_values)
sigma_T = np.std(T10_values, ddof=1)

# Time for one oscillation
T = T10_mean / 10
delta_T = (sigma_T / np.sqrt(len(T10_values))) / 10

# Calculate g
g = (4 * np.pi**2 * L) / T**2
delta_g = g * np.sqrt((delta_L / L)**2 + (2 * delta_T / T)**2)

print(f"g = {g:.3f} m/s² ± {delta_g:.3f} m/s²")
```

---

## 📊 Visualization

```python
import matplotlib.pyplot as plt

plt.hist(T10_values, bins=5, color='skyblue', edgecolor='black')
plt.axvline(T10_mean, color='red', linestyle='--', label=f"Mean = {T10_mean:.2f} s")
plt.title("Distribution of 10-Oscillation Timings")
plt.xlabel("Time for 10 Oscillations (s)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🧠 Analysis

- Compare your calculated \( g \) with **9.81 m/s²**
- Discuss:
  - Effect of ruler resolution on \( \Delta L \)
  - Variability in timing \( \Delta T \)
  - Small-angle approximation, air resistance, and other assumptions

---

## ✅ Deliverables

- All calculated values: \( L, \Delta L, \overline{T_{10}}, \sigma_T, \Delta T, g, \Delta g \)
- Visualization of timing histogram
- Markdown explanation and analysis
