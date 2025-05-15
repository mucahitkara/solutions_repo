# Calculating Equivalent Resistance Using Graph Theory

## Motivation

Calculating equivalent resistance is a fundamental problem in electrical circuits, essential for understanding and designing efficient systems. While traditional methods involve iteratively applying series ($R_{\text{series}} = R_1 + R_2$) and parallel ($R_{\text{parallel}} = \frac{R_1 R_2}{R_1 + R_2}$) resistor rules, these approaches can become cumbersome for complex circuits with many components. Graph theory offers a powerful alternative, providing a structured and algorithmic way to analyze circuits.

By representing a circuit as a graph—where nodes correspond to junctions and edges represent resistors with weights equal to their resistance values—we can systematically simplify even the most intricate networks. This method not only streamlines calculations but also opens the door to automated analysis, making it particularly useful in modern applications like circuit simulation software, optimization problems, and network design.

Studying equivalent resistance through graph theory is valuable not only for its practical applications but also for the deeper insights it provides into the interplay between electrical and mathematical concepts. This approach highlights the versatility of graph theory, demonstrating its relevance across physics, engineering, and computer science.

---

## Task: Full Implementation in Python

We’ll implement an algorithm in Python using `networkx` to:

1. Accept a circuit graph as input.
2. Handle arbitrary resistor configurations, including nested series and parallel combinations.
3. Output the final equivalent resistance.
4. Test with three examples: simple series, simple parallel, and nested configurations.

---

## Explanation

The Python implementation:

1. **Series Reduction**: Identifies nodes with degree 2 (indicating series resistors), sums their resistances ($R_{\text{eq}} = R_1 + R_2$), and replaces them with a single edge.
2. **Parallel Reduction**: Detects multiple edges between two nodes (indicating parallel resistors), computes their equivalent resistance ($R_{\text{eq}} = 1 / (1/R_1 + 1/R_2 + \dots)$), and replaces them with one edge.
3. **Iteration**: Repeatedly applies these reductions until only the source and sink nodes remain with one edge.

Nested combinations are handled naturally through iteration—each reduction simplifies the graph, potentially revealing new series or parallel opportunities.

---

## Example Applications

### Example 1: Simple Series Circuit

- **Graph**: $S \rightarrow A \rightarrow T$
- **Edges**: $(S, A)$ with $R_1 = 2\Omega$, $(A, T)$ with $R_2 = 3\Omega$
- **Step 1**: Series reduction at $A$:
  $R_{\text{eq}} = 2 + 3 = 5\Omega$
- **Result**: $R_{\text{eq}} = 5\Omega$

### Example 2: Simple Parallel Circuit

- **Graph**: $S \rightarrow T$ with two edges
- **Edges**: $R_1 = 4\Omega$, $R_2 = 6\Omega$
- **Step 1**: Parallel reduction:
  $R_{\text{eq}} = \frac{4 \cdot 6}{4 + 6} = \frac{24}{10} = 2.4\Omega$
- **Result**: $R_{\text{eq}} = 2.4\Omega$

### Example 3: Nested Configuration

- **Graph**: $S \rightarrow A \rightarrow B \rightarrow T$, with parallel edges between $A$ and $B$
- **Edges**: $(S, A)$ with $2\Omega$, $(A, B)$ with $3\Omega$ and $6\Omega$ (parallel), $(B, T)$ with $4\Omega$
- **Step 1**: Parallel reduction $(A, B)$:
  $R_{AB} = \frac{3 \cdot 6}{3 + 6} = \frac{18}{9} = 2\Omega$
- **Step 2**: Series reduction $S \rightarrow A \rightarrow B$:
  $R_{SA} = 2 + 2 = 4\Omega$
- **Step 3**: Series reduction $S \rightarrow B \rightarrow T$:
  $R_{\text{eq}} = 4 + 4 = 8\Omega$
- **Result**: $R_{\text{eq}} = 8\Omega$

---

## Efficiency Analysis

- **Time Complexity**:

  - Series reduction: $O(|V|)$ per call to check node degrees.
  - Parallel reduction: $O(|V|^2)$ to check all node pairs.
  - Iterations: Up to $O(|V|)$ reductions.
  - Total: $O(|V|^3)$ in the worst case.
  
- **Space Complexity**: 

  - $O(|V| + |E|)$ for storing the graph.

### Potential Improvements

1. **Graph Traversal**: Use DFS or BFS ($O(|V| + |E|)$) to detect patterns faster.
2. **Data Structures**: Use adjacency lists for quicker edge lookups.
3. **Delta-Wye Transform**: Add support for non-series/parallel circuits with:
   $R_a = \frac{R_1 R_2 + R_2 R_3 + R_3 R_1}{R_1}$

---

## Python Implementation

```python
import networkx as nx

def reduce_series(G):
    """Reduce series connections in the graph."""
    for node in list(G.nodes()):  # Iterate over a copy of nodes
        if G.degree(node) == 2:
            neighbors = list(G.neighbors(node))
            u, w = neighbors[0], neighbors[1]
            if G.has_edge(u, node) and G.has_edge(node, w):
                R_uv = G[u][node]['weight']
                R_vw = G[node][w]['weight']
                R_new = R_uv + R_vw  # Series combination: R_eq = R1 + R2
                G.remove_node(node)
                if not G.has_edge(u, w):  # Avoid duplicate edges
                    G.add_edge(u, w, weight=R_new)
                return True
    return False

def reduce_parallel(G):
    """Reduce parallel connections in the graph."""
    for u, v in list(G.edges()):
        edges = list(G.get_edge_data(u, v).values())
        if len(edges) > 1:  # Multiple edges exist
            resistances = [edge['weight'] for edge in edges]
            if any(R == 0 for R in resistances):  # If any resistor is zero, equivalent resistance is zero
                R_new = 0
            else:
                R_new = 1 / sum(1/R for R in resistances)  # Parallel combination: 1/R_eq = 1/R1 + 1/R2 ...
            G.remove_edges_from(list(G.edges(u, v)))  # Remove all parallel edges
            G.add_edge(u, v, weight=R_new)
            return True
    return False

def compute_equivalent_resistance(G, source, sink):
    """Compute equivalent resistance between source and sink."""
    G = G.copy()  # Work on a copy of the graph
    while len(G.nodes()) > 2 or G.number_of_edges() > 1:
        if reduce_series(G):
            continue
        if reduce_parallel(G):
            continue
        break  # If no reduction was possible, exit the loop
    
    if G.has_edge(source, sink):
        return G[source][sink]['weight']
    else:
        raise ValueError("No direct connection between source and sink after reduction.")

# Test the examples
def test_circuits():
    # Example 1: Simple Series
    G1 = nx.Graph()
    G1.add_edge('S', 'A', weight=2)
    G1.add_edge('A', 'T', weight=3)
    print("\nExample 1 - Simple Series (2Ω + 3Ω):")
    R_eq1 = compute_equivalent_resistance(G1, 'S', 'T')
    print(f"Equivalent Resistance = {R_eq1:.2f} Ω")

    # Example 2: Simple Parallel
    G2 = nx.Graph()
    G2.add_edge('S', 'T', weight=4)
    G2.add_edge('S', 'T', weight=6)
    print("\nExample 2 - Simple Parallel (4Ω || 6Ω):")
    R_eq2 = compute_equivalent_resistance(G2, 'S', 'T')
    print(f"Equivalent Resistance = {R_eq2:.2f} Ω")

    # Example 3: Nested Configuration
    G3 = nx.Graph()
    G3.add_edge('S', 'A', weight=2)
    G3.add_edge('A', 'B', weight=3)
    G3.add_edge('A', 'B', weight=6)
    G3.add_edge('B', 'T', weight=4)
    print("\nExample 3 - Nested (2Ω in series with (3Ω || 6Ω) in series with 4Ω):")
    R_eq3 = compute_equivalent_resistance(G3, 'S', 'T')
    print(f"Equivalent Resistance = {R_eq3:.2f} Ω")

if __name__ == "__main__":
    test_circuits()
```

### Example 1 - Simple Series (2Ω + 3Ω):

- Equivalent Resistance = 5.00 Ω

### Example 2 - Simple Parallel (4Ω || 6Ω):

- Equivalent Resistance = 6.00 Ω

### Example 3 - Nested (2Ω in series with (3Ω || 6Ω) in series with 4Ω):

 - Equivalent Resistance = 12.00 Ω