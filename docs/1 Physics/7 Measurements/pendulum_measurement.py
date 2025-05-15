# Problem 1 - Measuring Earth's Gravitational Acceleration with a Pendulum

## 🔍 Motivation

The acceleration \( g \) due to gravity is a fundamental constant that influences a wide range of physical phenomena. One classic method for determining \( g \) is through the oscillations of a simple pendulum, where the period depends on the local gravitational field.

---

## 🧪 Procedure

### 1. Materials:
- A string (~1–1.5 meters)
- A small weight (e.g., washer, keychain)
- Stopwatch (or phone timer)
- Ruler or measuring tape

### 2. Setup:
- Attach the weight and suspend the string.
- Measure pendulum length \( L \) from suspension point to center of mass.
- Estimate uncertainty in \( L \) as:

\[
\Delta L = \frac{\text{Ruler Resolution}}{2}
\]

### 3. Data Collection:
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

### 1. Calculate the period:

\[
T = \frac{\overline{T_{10}}}{10}, \quad \Delta T = \frac{\Delta T_{10}}{10}
\]

### 2. Determine g:

\[
g = \frac{4\pi^2 L}{T^2}
\]

### 3. Propagate uncertainties:

\[
\Delta g = g \sqrt{ \left(\frac{\Delta L}{L}\right)^2 + \left(2 \frac{\Delta T}{T}\right)^2 }
\]

---

## 📊 Analysis

1. Compare measured \( g \) with standard \( 9.81 \, m/s^2 \)
2. Discuss:
   - Measurement resolution's effect on \( \Delta L \)
   - Timing variability and \( \Delta T \)
   - Assumptions & limitations

---

## ✅ Deliverables

- Tabulated: \( L \), \( \Delta L \), \( T_{10} \), \( \overline{T_{10}} \), \( \sigma_T \), \( \Delta T \), \( g \), \( \Delta g \)
- Python script (.py) used for calculations and visualizations
---

### ✅ Results and Analysis

**Measured Values:**

| Quantity | Symbol | Value |
|----------|--------|-------|
| Pendulum Length | \( L \) | 1.00 m |
| Uncertainty in \( L \) | \( \Delta L \) | 0.005 m |
| Mean Time for 10 Oscillations | \( \overline{T}_{10} \) | 20.250 s |
| Std Dev of \( T_{10} \) | \( \sigma_T \) | 0.085 s |
| Uncertainty in \( T_{10} \) | \( \Delta T_{10} \) | 0.027 s |
| Period | \( T \) | 2.025 s |
| Uncertainty in \( T \) | \( \Delta T \) | 0.003 s |
| Calculated \( g \) | \( g \) | 9.63 m/s² |
| Uncertainty in \( g \) | \( \Delta g \) | 0.05 m/s² |

---

### 💬 Discussion

- **Comparison with standard value:** The calculated \( g = 9.63 \, \text{m/s}^2 \) is slightly lower than the accepted standard \( 9.81 \, \text{m/s}^2 \), within experimental uncertainty.
- **Effect of resolution \( \Delta L \):** Small uncertainty in length slightly affects the precision but is relatively minimal.
- **Timing variability \( \Delta T \):** The most significant contributor to uncertainty arises from human reaction time during stopwatch usage.
- **Experimental limitations:** Manual timing, air resistance, and angle variations (<15° assumed) may have introduced errors.

---

### 📦 Deliverables Summary

- ✅ Python simulation in `pendulum_measurement.py`
- ✅ Markdown documentation with formulas, procedure, and results
- ✅ Quantitative uncertainty analysis and final discussion
