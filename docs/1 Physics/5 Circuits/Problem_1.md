# Problem 1 - Equivalent Resistance Using Graph Theory

## 🔷 Motivation:

Calculating equivalent resistance is a fundamental problem in electrical circuits, essential for understanding and designing efficient systems.  
While traditional methods involve iteratively applying series and parallel resistor rules, these approaches can become cumbersome for complex circuits with many components.

Graph theory offers a powerful alternative:  
By representing a circuit as a graph—where **nodes** correspond to junctions and **edges** represent resistors (with weights as resistance values)—we can systematically simplify even the most intricate networks.

This method enables:
- Streamlined calculations  
- Algorithmic automation for circuit solvers  
- Applications in optimization, simulation, and network design

Studying equivalent resistance through graph theory not only has practical value, but also deepens our understanding of the interplay between **electrical** and **mathematical** systems.

---

## 🔷 Task Options:

### Option 1: Simplified Task – Algorithm Description

- Describe the algorithm for calculating equivalent resistance using graph theory
- Provide **pseudocode** that:
  - Identifies **series** and **parallel** connections
  - Iteratively reduces the graph to a **single equivalent resistance**
  - Explains how nested combinations are handled

---

### Option 2: Advanced Task – Full Implementation

- Implement the algorithm in any programming language (e.g., Python)

The implementation should:
- Accept a **circuit graph** as input
- Handle **arbitrary resistor configurations** including nested series/parallel
- Output the **final equivalent resistance**
- Be tested with multiple examples:
  - Simple combinations
  - Nested setups
  - Complex cyclic graphs

---

## 🔷 Deliverables:

1. A detailed **pseudocode** (preferably a working **implementation**)  
2. Description of how your solution handles:
   - Complex circuit topologies  
   - At least **three test cases**  
3. A brief analysis on:
   - Algorithm efficiency  
   - Potential improvements

---

## 🔷 Hints and Resources:

- Use **iterative graph simplification**:
  - Detect linear chains → series reduction  
  - Identify cycles → parallel reduction

- Consider libraries such as:
  - **networkx** (Python) for graph manipulation

- Algorithms to consider:
  - **DFS (Depth-First Search)**  
  - Other traversal techniques for pattern detection

Choose the task that matches your comfort level, but ensure your solution is well-structured and clear.


