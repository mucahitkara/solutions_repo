# Measuring Earth's Gravitational Acceleration with a Pendulum

## Objective

The goal of this experiment is to measure the acceleration due to gravity, $g$, using a simple pendulum and to analyze the uncertainties in the measurements. This exercise emphasizes rigorous measurement practices, uncertainty analysis, and their role in experimental physics.

## Materials

- A string (1 or 1.5 meters long)
- A small weight (e.g., bag of coins, bag of sugar, key chain) mounted on the string
- Stopwatch (or smartphone timer)
- Ruler or measuring tape

## Procedure

### 1. Setup

- Attach the weight to the string and fix the other end to a sturdy support.
- Measure the length of the pendulum, $L$, from the suspension point to the center of the weight using a ruler or measuring tape.
- Record the resolution of the measuring tool and calculate the uncertainty as half the resolution:  
  $\Delta L = \frac{\text{Ruler Resolution}}{2}$.

### 2. Data Collection

- Displace the pendulum slightly (<15°) and release it.
- Measure the time for 10 full oscillations, $T_{10}$, and repeat this process 10 times. Record all 10 measurements.
- Calculate the mean time for 10 oscillations, $\overline{T}_{10}$, and the standard deviation, $\sigma_T$.
- Determine the uncertainty in the mean time as:  
  $\Delta T_{10} = \frac{\sigma_T}{\sqrt{n}}$, where $n = 10$.

## Calculations

### 1. Calculate the Period

The period of one oscillation, $T$, is calculated as:  
$T = \frac{T_{10}}{10}$,  
with the uncertainty in the period given by:  
$\Delta T = \frac{\Delta T_{10}}{10}$.

### 2. Determine $g$

The acceleration due to gravity, $g$, is determined using the formula for the period of a simple pendulum:  
$g = \frac{4\pi^2 L}{T^2}$.

### 3. Propagate Uncertainties

The uncertainty in $g$, $\Delta g$, is calculated using the error propagation formula:  
$\Delta g = g \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2 \frac{\Delta T}{T}\right)^2}$.

## Example Calculation

Let’s assume the following measured values for illustration:

- Length of the pendulum: $L = 1.000 \, \text{m}$, with a ruler resolution of $0.001 \, \text{m}$, so $\Delta L = \frac{0.001}{2} = 0.0005 \, \text{m}$.
- Mean time for 10 oscillations (from 10 trials): $\overline{T}_{10} = 20.00 \, \text{s}$, with a standard deviation $\sigma_T = 0.10 \, \text{s}$.

### Step 1: Calculate the Period

$T = \frac{\overline{T}_{10}}{10} = \frac{20.00}{10} = 2.000 \, \text{s}$,  

$\Delta T_{10} = \frac{\sigma_T}{\sqrt{n}} = \frac{0.10}{\sqrt{10}} \approx 0.0316 \, \text{s}$,  

$\Delta T = \frac{\Delta T_{10}}{10} = \frac{0.0316}{10} \approx 0.00316 \, \text{s}$.

### Step 2: Determine $g$

$g = \frac{4\pi^2 L}{T^2} = \frac{4 \pi^2 (1.000)}{(2.000)^2} = \frac{4 \pi^2 (1.000)}{4.000} \approx 9.870 \, \text{m/s}^2$.

### Step 3: Propagate Uncertainties

$\Delta g = g \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2 \frac{\Delta T}{T}\right)^2}$,

$\frac{\Delta L}{L} = \frac{0.0005}{1.000} = 0.0005$,  

$\frac{\Delta T}{T} = \frac{0.00316}{2.000} \approx 0.00158$,

$2 \frac{\Delta T}{T} = 2 \times 0.00158 = 0.00316$,  

$\Delta g = 9.870 \sqrt{(0.0005)^2 + (0.00316)^2} = 9.870 \sqrt{0.00000025 + 0.00000999} \approx 9.870 \times 0.0032 \approx 0.032 \, \text{m/s}^2$.

Thus, the measured value of $g$ is:  
$g = 9.87 \pm 0.03 \, \text{m/s}^2$.

## Analysis

### 1. Comparison with Standard Value

The standard value of $g$ is $9.81 \, \text{m/s}^2$. The measured value, $9.87 \pm 0.03 \, \text{m/s}^2$, is slightly higher but within a reasonable range, considering the uncertainty. The difference could be due to experimental factors such as air resistance, small-angle approximation errors, or local variations in $g$.

### 2. Discussion

- **Effect of Measurement Resolution on $\Delta L$**: The resolution of the ruler directly affects $\Delta L$. A ruler with a resolution of $0.001 \, \text{m}$ gives a small uncertainty, but a less precise tool (e.g., resolution of $0.01 \, \text{m}$) would increase $\Delta L$ to $0.005 \, \text{m}$, impacting the uncertainty in $g$.
- **Variability in Timing and Its Impact on $\Delta T$**: The standard deviation in timing, $\sigma_T$, reflects variability in the measurements, possibly due to human reaction time or inconsistent pendulum motion. A larger $\sigma_T$ increases $\Delta T$, which significantly affects $\Delta g$ because of the $2 \frac{\Delta T}{T}$ term in the error propagation formula.
- **Assumptions and Experimental Limitations**: The experiment assumes a small-angle approximation (<15°) for the pendulum motion, negligible air resistance, and a point mass. Deviations from these assumptions (e.g., large swings, air drag, or a non-ideal pendulum) could introduce systematic errors.

## Deliverables

### 1. Tabulated Data

| $L$ (m) | $\Delta L$ (m) | $T_{10}$ Measurements (s) | $\overline{T}_{10}$ (s) | $\sigma_T$ (s) | $\Delta T$ (s) | $g$ (m/s²) | $\Delta g$ (m/s²) |
|---------|----------------|---------------------------|------------------|---------------|----------------|------------|-------------------|
| 1.000   | 0.0005         | 20.00, 20.02, 19.98, ...  | 20.00            | 0.10          | 0.00316        | 9.87       | 0.03              |

### 2. Discussion on Sources of Uncertainty

- **Length Measurement**: The uncertainty in $L$ is small due to the high resolution of the ruler, but any misalignment or stretching of the string could introduce systematic errors.
- **Timing Variability**: Human reaction time in starting and stopping the stopwatch contributes to $\sigma_T$. Using a more precise timing method (e.g., a photogate) could reduce this uncertainty.
- **Environmental Factors**: Air resistance and temperature variations might affect the pendulum’s motion, though these effects are typically small for a simple setup.
- **Impact on Results**: The uncertainty in $T$ has a larger impact on $\Delta g$ due to the $T^2$ term in the formula for $g$. Improving timing precision would yield a more accurate result.

This experiment demonstrates the importance of careful measurement and uncertainty analysis in determining a fundamental physical constant like $g$.