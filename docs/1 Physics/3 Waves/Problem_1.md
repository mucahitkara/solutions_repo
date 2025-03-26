# Problem 1 - Interference Patterns on a Water Surface

## 🔷 Motivation:

Interference occurs when waves from different sources overlap, creating new patterns.  
On a water surface, this can be easily observed when ripples from different points meet, forming distinctive interference patterns.  
These patterns can show us how waves combine in different ways, either reinforcing each other or canceling out.

Studying these patterns helps us understand wave behavior in a simple, visual way.  
It also allows us to explore important concepts, like the relationship between wave phase and the effects of multiple sources.  
This task offers a hands-on approach to learning about wave interactions and their real-world applications.

---

## 🔷 Task:

A circular wave on the water surface, emanating from a point source located at \((x_0, y_0)\), can be described by the Single Disturbance equation:

\[
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cdot \cos(kr - \omega t + \phi)
\]

**Where:**
- \(\eta(x, y, t)\) = Displacement of the water surface at point \((x, y)\) and time \(t\)  
- \(A\) = Amplitude  
- \(k = \frac{2\pi}{\lambda}\) = Wave number, related to wavelength \(\lambda\)  
- \(\omega = 2\pi f\) = Angular frequency, related to frequency \(f\)  
- \(r = \sqrt{(x - x_0)^2 + (y - y_0)^2}\) = Distance to source  
- \(\phi\) = Initial phase

---

## 🔷 Problem Statement:

Analyze the interference patterns formed on the water surface due to the superposition of waves emitted from point sources placed at the vertices of a chosen regular polygon.

---

## 🔷 Steps to Follow:

1. **Select a Regular Polygon:**  
   Choose a regular polygon (e.g., equilateral triangle, square, pentagon).

2. **Position the Sources:**  
   Place point wave sources at the vertices of the selected polygon.

3. **Wave Equations:**  
   Write wave equations for each source, considering their positions.

4. **Superposition of Waves:**  
   \[
   \eta_{\text{sum}}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)
   \]
   where \(N\) = number of sources (polygon vertices)

5. **Analyze Interference Patterns:**  
   Examine \(\eta_{\text{sum}}(x, y, t)\) over time and space. Identify:
   - Constructive interference (amplification)
   - Destructive interference (cancellation)

6. **Visualization:**  
   Graphically represent wave patterns using simulations.

---

## 🔷 Considerations:

- All sources emit waves with **same amplitude \(A\)**, **wavelength \(\lambda\)**, and **frequency \(f\)**
- Waves are **coherent**, maintaining constant phase difference
- Visualization tools like **Python + Matplotlib** are recommended

---

## 🔷 Deliverables:

1. A **Markdown** document with embedded **Python script / notebook**
2. A clear explanation of interference patterns for your chosen polygon
3. **Graphical results** showing constructive & destructive regions

