"""CONNECTIONS — verified topology/dynamics experiment.

Model:
- 8 binary nodes
- 3-regular simple graph
- synchronous rule f(self_state, active_neighbor_count)
- all 256 local rules
- all 256 initial states

Requires: networkx, numpy
"""

from itertools import combinations
import json
import networkx as nx
import numpy as np


N = 8
DEGREE = 3


def generate_regular_graphs(n=N, degree=DEGREE):
    """Generate all labelled regular graphs by recursive degree completion,
    then keep one representative of each isomorphism class."""
    edges = list(combinations(range(n), 2))
    reps = []

    def rec(pos, deg, chosen):
        if pos == len(edges):
            if all(d == degree for d in deg):
                g = nx.Graph()
                g.add_nodes_from(range(n))
                g.add_edges_from(chosen)
                if nx.is_connected(g) or True:
                    if not any(nx.is_isomorphic(g, h) for h in reps):
                        reps.append(g.copy())
            return
        u, v = edges[pos]
        remaining = len(edges) - pos - 1
        if all(d <= degree for d in deg):
            # Skip edge.
            if all(d + remaining >= degree for d in deg):
                rec(pos + 1, deg, chosen)
            # Take edge.
            if deg[u] < degree and deg[v] < degree:
                nd = deg[:]
                nd[u] += 1
                nd[v] += 1
                rec(pos + 1, nd, chosen + [(u, v)])

    rec(0, [0] * n, [])
    return reps


def all_rules():
    # 8 truth-table inputs: self=0/1, k=0..3.
    return range(256)


def apply_rule(rule, self_state, k):
    idx = self_state * 4 + k
    return (rule >> idx) & 1


def step(state, g, rule):
    out = 0
    for i in range(N):
        s = (state >> i) & 1
        k = sum((state >> j) & 1 for j in g.neighbors(i))
        out |= apply_rule(rule, s, k) << i
    return out


def cycle_from(start, g, rule):
    seen = {}
    state = start
    t = 0
    while state not in seen:
        seen[state] = t
        state = step(state, g, rule)
        t += 1
    return state, t - seen[state]


def analyse_graph(g):
    result = []
    for rule in all_rules():
        attractors = {}
        for start in range(1 << N):
            key, cycle_len = cycle_from(start, g, rule)
            attractors[(key, cycle_len)] = attractors.get((key, cycle_len), 0) + 1

        max_cycle = max(k[1] for k in attractors)
        result.append({
            "rule": rule,
            "attractors": len(attractors),
            "basin_sizes": sorted(attractors.values(), reverse=True),
            "max_cycle": max_cycle,
        })
    return result


def graph_metrics(g):
    lap = nx.laplacian_matrix(g).toarray().astype(float)
    eig = np.linalg.eigvalsh(lap)
    connected = nx.is_connected(g)
    return {
        "nodes": g.number_of_nodes(),
        "edges": g.number_of_edges(),
        "degree": sorted(dict(g.degree()).values())[0],
        "connected": connected,
        "triangles": sum(nx.triangles(g).values()) // 3,
        "clustering": nx.average_clustering(g),
        "lambda2": float(eig[1]) if connected else 0.0,
        "diameter": nx.diameter(g) if connected else None,
    }


def main():
    graphs = generate_regular_graphs()
    print("non_isomorphic_graphs:", len(graphs))

    for idx, g in enumerate(graphs):
        metrics = graph_metrics(g)
        data = analyse_graph(g)
        avg_max_cycle = float(np.mean([x["max_cycle"] for x in data]))
        max_cycle = max(x["max_cycle"] for x in data)
        multi = sum(x["attractors"] > 1 for x in data)
        metrics.update({
            "graph_index": idx,
            "average_max_cycle": avg_max_cycle,
            "maximum_cycle": max_cycle,
            "rules_with_multiple_attractors": multi,
        })
        print(json.dumps(metrics, sort_keys=True))

if __name__ == "__main__":
    main()
