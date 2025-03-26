# Problem 2 - Estimating Pi using Monte Carlo Methods

## 🔷 Motivation:

Monte Carlo simulations are a powerful class of computational techniques that use randomness to solve problems or estimate values.  
One of the most elegant applications is estimating the value of \(\pi\) through geometric probability.

By randomly generating points and analyzing their positions relative to a geometric shape, we can approximate \(\pi\) in an intuitive and visually engaging way.

This problem connects fundamental concepts of **probability**, **geometry**, and **numerical computation**.  
It also provides a gateway to understand how randomness can be harnessed to solve complex problems in physics, finance, and computer science.

---

## 🔷 Task:

### 🔹 PART 1: Estimating \(\pi\) Using a Circle

#### 1. Theoretical Foundation:

- Explain how the ratio of points inside a circle to the total number of points in a square can be used to estimate \(\pi\).
- Derive the formula:  
  \[
  \pi \approx 4 \cdot \left(\frac{\text{points inside circle}}{\text{total points}}\right)
  \]  
  for a unit circle.

#### 2. Simulation:

- Generate random points in a 2D square bounding a unit circle.
- Count the number of points falling inside the circle.
- Estimate \(\pi\) based on this ratio.

#### 3. Visualization:

- Create a plot showing the randomly generated points.
- Distinguish between those **inside** and **outside** the circle.

#### 4. Analysis:

- Investigate how accuracy improves as the number of points increases.
- Discuss convergence rate and computational considerations.

---

### 🔹 PART 2: Estimating \(\pi\) Using Buffon’s Needle

#### 1. Theoretical Foundation:

- Describe Buffon’s Needle problem: estimate \(\pi\) based on the probability of a needle crossing parallel lines.
- Derive the formula:  
  \[
  \pi \approx \frac{2 \cdot \text{needle length} \cdot \text{number of throws}}{\text{distance between lines} \cdot \text{number of crossings}}
  \]

#### 2. Simulation:

- Simulate the random dropping of a needle on a plane with parallel lines.
- Count how many times the needle crosses a line.
- Estimate \(\pi\) using the formula.

#### 3. Visualization:

- Create a graphical representation of the simulation.
- Show needle positions relative to the lines.

#### 4. Analysis:

- Explore how the number of drops affects accuracy.
- Compare convergence with the circle-based method.

---

## 🔷 Deliverables:

1. A Markdown document with:
   - Clear explanations of both methods
   - Discussion of theoretical foundations and results

2. Python scripts/notebooks:
   - Code for circle-based Monte Carlo simulation
   - Code for Buffon’s Needle simulation

3. Graphical outputs:
   - Plots of random points (circle method)
   - Visualizations of needle positions (Buffon’s method)

4. Analysis:
   - Tables/graphs showing convergence vs iterations
   - Comparison of both methods in terms of accuracy & efficiency

---

## 🔷 Hints and Resources:

- Use **NumPy** for random generation  
- Use **Matplotlib** for visualizations  
- Ensure uniform random point generation (for circle method)  
- In Buffon’s Needle:
  - Pay attention to geometry: needle length vs distance between lines  
  - Start with small iteration counts, then increase for convergence
